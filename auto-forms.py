import time
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# ==============================
# CONFIGURATION
# ==============================
EXCEL_FILE = "questions_fifth.xlsx" #Enter the excel file with the format presented
FORM_URL = "" #Enter your Microsoft Form edit URL
WAIT = 1
RESUME_FILE = "resume_index.txt"
# ==============================

# Create resume file if needed
start_index = 0
if os.path.exists(RESUME_FILE):
    try:
        with open(RESUME_FILE, "r") as f:
            start_index = int(f.read().strip())
    except:
        start_index = 0

print(f"➡️ Starting from question {start_index + 1}")

# Load Excel data
data = pd.read_excel(EXCEL_FILE)

# Setup Chrome (visible for debugging)
options = Options()
options.add_experimental_option("detach", True)  # Keeps Chrome open after run
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Open Form
driver.get(FORM_URL)
input("👉 Log in to Microsoft Forms and open your edit page, then press ENTER here...")

def safe_find(xpath, timeout=10):
    """Find element safely with retry."""
    for _ in range(timeout):
        try:
            return driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            time.sleep(1)
    raise NoSuchElementException(f"Could not find element: {xpath}")

def scroll_to_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

# ==============================
# MAIN LOOP
# ==============================
for index, row in data.iloc[start_index:].iterrows():
    q_no = index + 1
    question = str(row["Question"])
    options_list = [str(row["Option1"]), str(row["Option2"]), str(row["Option3"])]
    correct_answer = str(row["CorrectAnswer"]).strip()

    print(f"\n🧠 Adding question {q_no}: {question}")

    with open(RESUME_FILE, "w") as f:
        f.write(str(index))

    scroll_to_bottom()

    # Add new question
    try:
        add_btn = driver.find_element(
            By.XPATH, "//button[contains(., 'Add new question') or contains(., 'Add question')]"
        )
        add_btn.click()
    except Exception:
        scroll_to_bottom()
        add_btn = safe_find("//button[contains(., 'Add new question') or contains(., 'Add question')]")
        add_btn.click()
    time.sleep(WAIT)

    # Select "Choice" question type
    try:
        choice_btn = driver.find_element(By.XPATH, "//button[contains(., 'Choice')]")
        choice_btn.click()
    except NoSuchElementException:
        pass
    time.sleep(WAIT)

    # Enter question text
    try:
        q_box = driver.find_element(By.XPATH, "//div[@role='textbox' and contains(@aria-label, 'Question')]")
        q_box.click()
        q_box.send_keys(Keys.CONTROL, "a")
        q_box.send_keys(Keys.BACKSPACE)
        q_box.send_keys(question)
    except Exception as e:
        print(f"⚠️ Could not write question: {e}")
    time.sleep(WAIT)

    # Add options dynamically
    option_boxes = driver.find_elements(By.XPATH, "//div[@role='textbox' and contains(@aria-label, 'Option')]")
    for i, opt in enumerate(options_list):
        while i >= len(option_boxes):
            try:
                add_option_btn = driver.find_element(By.XPATH, "//button[contains(., 'Add option')]")
                add_option_btn.click()
                time.sleep(1)
                option_boxes = driver.find_elements(By.XPATH, "//div[@role='textbox' and contains(@aria-label, 'Option')]")
            except Exception:
                break
        try:
            option_boxes[i].click()
            option_boxes[i].send_keys(Keys.CONTROL, "a")
            option_boxes[i].send_keys(Keys.BACKSPACE)
            option_boxes[i].send_keys(opt)
        except Exception as e:
            print(f"⚠️ Error filling option {i+1}: {e}")
        time.sleep(0.5)

    # ✅ Select Correct Answer
    try:
        option_boxes = driver.find_elements(By.XPATH, "//div[@role='textbox' and contains(@aria-label, 'Option')]")
        option_texts = []
        for box in option_boxes:
            val = box.get_attribute("value") or box.text
            option_texts.append(val.strip().lower())

        correct_index = -1
        for i, val in enumerate(option_texts):
            if correct_answer.lower() == val:
                correct_index = i
                break

        if correct_index != -1:
            checkmarks = driver.find_elements(
                By.XPATH, "//button[@aria-label='Mark as correct answer' or contains(@aria-label, 'Correct answer')]"
            )
            if correct_index < len(checkmarks):
                driver.execute_script("arguments[0].scrollIntoView(true);", checkmarks[correct_index])
                checkmarks[correct_index].click()
                print(f"✅ Marked option {correct_index+1} as correct ({correct_answer})")
            else:
                print("⚠️ Checkmark button count mismatch.")
        else:
            print(f"⚠️ Could not find matching option for correct answer: {correct_answer}")
    except Exception as e:
        print(f"⚠️ Error while marking correct answer: {e}")

    # 🧮 Assign 1 Point
    try:
        points_field = driver.find_element(By.XPATH, "//input[@aria-label='Points']")
        driver.execute_script("arguments[0].scrollIntoView(true);", points_field)
        points_field.click()
        points_field.send_keys(Keys.CONTROL, "a")
        points_field.send_keys(Keys.BACKSPACE)
        points_field.send_keys("1")
        points_field.send_keys(Keys.ENTER)
        print("🏅 Assigned 1 point to this question.")
    except Exception as e:
        print(f"⚠️ Could not assign points: {e}")

    print(f"✅ Finished question {q_no}")
    time.sleep(WAIT + 1)

print("\n🎉 All questions added successfully with 1 point each!")
if os.path.exists(RESUME_FILE):
    os.remove(RESUME_FILE)
driver.quit()
