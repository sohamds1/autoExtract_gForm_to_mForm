<div align="left" style="position: relative;">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>AUTOEXTRACT_GFORM_TO_MFORM</h1>
<p align="left">
	<em><code>❯ REPLACE-ME</code></em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/sohamds1/autoExtract_gForm_to_mForm?style=flat-square&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/sohamds1/autoExtract_gForm_to_mForm?style=flat-square&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/sohamds1/autoExtract_gForm_to_mForm?style=flat-square&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/sohamds1/autoExtract_gForm_to_mForm?style=flat-square&color=0080ff" alt="repo-language-count">
</p>
<p align="left">Built with the tools and technologies:</p>
<p align="left">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat-square&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
</p>
</div>
<br clear="right">

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<code>❯ REPLACE-ME</code>

---

## 👾 Features

<code>❯ REPLACE-ME</code>

---

## 📁 Project Structure

```sh
└── autoExtract_gForm_to_mForm/
    ├── LICENSE
    ├── LICENSE.chromedriver
    ├── THIRD_PARTY_NOTICES.chromedriver
    ├── auto-forms.py
    ├── automate_extract_gForm.js
    ├── chromedriver.exe
    ├── questions.xlsx
    └── questions_fifth.xlsx
```


### 📂 Project Index
<details open>
	<summary><b><code>AUTOEXTRACT_GFORM_TO_MFORM/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/sohamds1/autoExtract_gForm_to_mForm/blob/master/automate_extract_gForm.js'>automate_extract_gForm.js</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sohamds1/autoExtract_gForm_to_mForm/blob/master/auto-forms.py'>auto-forms.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sohamds1/autoExtract_gForm_to_mForm/blob/master/LICENSE.chromedriver'>LICENSE.chromedriver</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/sohamds1/autoExtract_gForm_to_mForm/blob/master/THIRD_PARTY_NOTICES.chromedriver'>THIRD_PARTY_NOTICES.chromedriver</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with autoExtract_gForm_to_mForm, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python, JS


### ⚙️ Installation

Install autoExtract_gForm_to_mForm using one of the following methods:

**Build from source:**

1. Clone the autoExtract_gForm_to_mForm repository:
```sh
❯ git clone https://github.com/sohamds1/autoExtract_gForm_to_mForm
```

2. Navigate to the project directory:
```sh
❯ cd autoExtract_gForm_to_mForm
```

3. Install the project dependencies:

echo 'INSERT-INSTALL-COMMAND-HERE'



### 🤖 Usage
Run autoExtract_gForm_to_mForm using the following command:
echo 'INSERT-RUN-COMMAND-HERE'

### 🧪 Testing
Run the test suite using the following command:
echo 'INSERT-TEST-COMMAND-HERE'

---
## 📌 Project Roadmap
🚀 Project Roadmap: Automated MCQ Form Generation System
🔹 Phase 1 — Google Apps Script Automation
🎯 Goal: Automate MCQ question creation in Google Forms from a Google Sheet
🧠 Key Learnings:

Understanding how Google Apps Script interacts with Google Forms and Sheets using built-in APIs.

Learning JavaScript-like syntax (Apps Script = JS + Google Services).

Designing a script that:

Reads each question + options + correct answer from Google Sheet.

Creates MCQs one by one.

Assigns one point per correct answer automatically.

⚙️ Tech Stack:

Google Apps Script (JavaScript runtime)

Google Forms API

Google Sheets

📄 Deliverable:

Script file (Code.gs) that takes:

var form = FormApp.openById('FORM_ID');
var sheet = SpreadsheetApp.openById('SHEET_ID').getSheetByName('Sheet1');


and auto-creates questions.

🧩 Outcome:

✅ Fully automated quiz creation in Google Forms using only cloud tools — zero local setup.
This became your proof-of-concept (POC) that such automation is possible.

🔹 Phase 2 — Transition to Microsoft Forms
🎯 Goal: Replicate Google automation for Microsoft Forms, which has no open API for free users.
⚠️ Challenge:

Microsoft Forms doesn’t expose a Forms API for personal accounts.

Power Automate + Graph API require Microsoft 365 Business.

Needed a workaround for free accounts.

💡 Decision:

Use Python + Selenium WebDriver to simulate browser actions — effectively creating a robotic UI automation layer.

🔹 Phase 3 — Python + Selenium Prototyping
🎯 Goal: Build a working script that:

Reads questions from Excel

Opens Microsoft Forms in Chrome

Automatically fills questions, options, and answers

⚙️ Tech Stack:

Python 3.12

Selenium WebDriver

Pandas + OpenPyXL

ChromeDriver

🧠 Features Added:

Excel parsing with pandas

Dynamic form creation

Option typing

Correct answer marking

Form navigation

Basic error handling

📄 Deliverable:

auto_forms.py

⚡ Outcome:

✅ First working version that could fill questions, but relied on old Microsoft UI (<textarea> elements).
⚠️ UI update broke the script → required refactoring.

🔹 Phase 4 — Microsoft Forms 2025 UI Adaptation
🎯 Goal: Make the script compatible with the new “DesignPageV2” Microsoft Forms interface.
🧠 Key Fixes:

Replaced outdated XPath selectors (<textarea>) with <div role="textbox">.

Added intelligent retries (safe_find()).

Introduced scroll automation (scroll_to_bottom()).

Implemented try-except for resilience.

Detected new “Add question” button labels dynamically.

📄 Deliverable:

auto_forms_stable.py

💡 Additional Improvements:

Screenshot after each question (for visual debugging)

“Resume” functionality (recovers after crashes)

Headless toggle (for faster, invisible runs)

🔹 Phase 5 — Correct Answer Automation
🎯 Goal: Mark the correct answer automatically in quiz mode.
⚙️ Implementation:

Detected tick mark buttons beside options (aria-label='Mark as correct answer').

Mapped option text to correct answer from Excel.

Matched and clicked dynamically.

📄 Deliverable:

auto_forms_debug_final.py

⚡ Challenges Solved:

New Microsoft Forms stores option text differently (value vs .text).

Script now normalizes both before matching.

🔹 Phase 6 — Points Automation
🎯 Goal: Assign 1 point per question automatically.
🧮 Implementation:

Added new block:

points_field = driver.find_element(By.XPATH, "//input[@aria-label='Points']")
points_field.send_keys("1")


Ensures each question = 1 point, ready for grading.

📄 Deliverable:

auto_forms_debug_points.py

🧩 Outcome:

✅ Full automation flow from Excel → Microsoft Forms
Each question:

Added dynamically

Filled with options

Correct answer ticked

1 point assigned

🔹 Phase 7 — Optional Future Enhancements (Road Ahead)
🧱 Potential Add-Ons:
Enhancement	Description
🧩 Dynamic Points	Read a “Points” column from Excel and assign variable scores
💾 Result Summary	Generate a success/failure report (CSV or console)
🧭 Auto-login	Use MSAL (Microsoft Auth Library) for secure login automation
🧠 AI Validation	Use LLM to auto-validate whether options are logically correct
🌐 Web Dashboard	Build a Streamlit or Flask dashboard to trigger automation from UI
📊 Progress Tracker	Show real-time completion % in terminal
🎓 Knowledge Stack Summary
Category	Technologies / Concepts Learned
Automation Frameworks	Google Apps Script, Selenium WebDriver
Programming Languages	JavaScript, Python
Browser Automation	ChromeDriver, XPath, dynamic DOM handling
File Handling	Excel automation (pandas + openpyxl)
Debugging	Live element inspection, exception handling
Data-driven Testing	External question banks as input datasets
UI Adaptation	Adjusting scripts to evolving web structures
Workflow Design	Resume logic, wait management, and retries
🏁 Final Outcome

You have built a Cross-Platform Form Automation Framework capable of:

Platform	Method	Works Without API?	Output
Google Forms	Google Apps Script	✅	Instant quiz creation from Sheets
Microsoft Forms	Python + Selenium	✅	Quiz with options, answers, and points

✅ End result: A completely automated MCQ Form Generator, compatible with both Google and Microsoft ecosystems.

📦 Project Files (Chronological Order)
File	Description
google_form_auto.gs	Initial Apps Script prototype for Google Forms
auto_forms.py	First working Selenium prototype
auto_forms_stable.py	New-UI compatible, screenshot version
auto_forms_debug_final.py	Clean, visible Chrome version
auto_forms_debug_points.py	Adds “1 point per question” functionality
🪜 Project Timeline Summary
Phase	Focus	Output
1	Google Apps Script Form Creation	100% working Google Form quiz automation
2	Microsoft Forms Exploration	Found lack of API support
3	Selenium Automation Prototype	Basic working automation
4	New UI Compatibility	Stable & UI-proof version
5	Correct Answer Selection	Quiz mode enabled
6	Points Assignment	Fully functional quiz automation
7	(Upcoming) Dashboard & Reports	Optional improvements
🚀 Vision Forward

This can evolve into:

A Form Automation SaaS Tool (teachers upload Excel → get form links)

A QA Tool for generating knowledge tests automatically

A training assessment generator for Future X Academy’s LMS platform (perfect integration opportunity 😉)

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/sohamds1/autoExtract_gForm_to_mForm/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/sohamds1/autoExtract_gForm_to_mForm/issues)**: Submit bugs found or log feature requests for the `autoExtract_gForm_to_mForm` project.
- **💡 [Submit Pull Requests](https://github.com/sohamds1/autoExtract_gForm_to_mForm/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/sohamds1/autoExtract_gForm_to_mForm
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/sohamds1/autoExtract_gForm_to_mForm/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=sohamds1/autoExtract_gForm_to_mForm">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
