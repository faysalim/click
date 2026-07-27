// Google Apps Script — click logger backend.
//
// Setup:
// 1. Create a new Google Sheet.
// 2. Extensions -> Apps Script. Delete the placeholder code and paste this file's contents in.
// 3. Click Deploy -> New deployment -> type "Web app".
//    - Execute as: Me
//    - Who has access: Anyone
// 4. Deploy, copy the Web App URL it gives you (ends in /exec).
// 5. Paste that URL into LOGGER_URL in r.html.
//
// Every click will show up as a new row in this sheet's "Clicks" tab.

function doPost(e) {
  var sheet = getOrCreateSheet();
  var data = {};
  try {
    data = JSON.parse(e.postData.contents);
  } catch (err) {
    data = {};
  }

  sheet.appendRow([
    new Date(),
    data.id || "",
    data.contact || "",
    data.channel || "",
    data.url || "",
    data.referrer || "",
    data.ua || "",
  ]);

  return ContentService.createTextOutput(
    JSON.stringify({ ok: true })
  ).setMimeType(ContentService.MimeType.JSON);
}

function getOrCreateSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName("Clicks");
  if (!sheet) {
    sheet = ss.insertSheet("Clicks");
    sheet.appendRow([
      "Timestamp",
      "Code",
      "Contact",
      "Channel",
      "Destination URL",
      "Referrer",
      "User Agent",
    ]);
  }
  return sheet;
}
