function exportThreeOptionMCQsByID() {
  // 🔹 ENTER YOUR FORM AND SHEET IDs BELOW
  const FORM_ID = "";  // replace with your actual Form ID
  const SHEET_ID = "";    // replace with your actual Sheet ID

  // Open the form and spreadsheet by ID
  const form = FormApp.openById(FORM_ID);
  const spreadsheet = SpreadsheetApp.openById(SHEET_ID);
  const sheet = spreadsheet.getActiveSheet();

  // Optional: clear previous data
  sheet.clear();
  sheet.appendRow(["Question", "Option 1", "Option 2", "Option 3", "Correct Answer"]);

  // Get all items in the form
  const items = form.getItems();

  // Loop through all MCQ items
  items.forEach((item) => {
    if (item.getType() === FormApp.ItemType.MULTIPLE_CHOICE) {
      const mcq = item.asMultipleChoiceItem();
      const question = mcq.getTitle();
      const choices = mcq.getChoices();

      // Extract options
      const options = choices.map((c) => c.getValue());
      while (options.length < 3) options.push("");

      // Extract correct answer(s)
      const correctAnswer = choices
        .filter((c) => c.isCorrectAnswer())
        .map((c) => c.getValue())
        .join(", ");

      // Write the data into the sheet
      sheet.appendRow([question, options[0], options[1], options[2], correctAnswer]);
    }
  });

  Logger.log("✅ Export complete!");
}