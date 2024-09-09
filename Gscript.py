function setPasswords() {
  var scriptProperties = PropertiesService.getScriptProperties();
  scriptProperties.setProperty('EXECUTION_PASSWORD', 'RCB');
}

function sendEmails() {
  var ui = SpreadsheetApp.getUi();
  var response = ui.prompt('Execution Password', 'Please enter the password to send emails:', ui.ButtonSet.OK_CANCEL);

  if (response.getSelectedButton() == ui.Button.OK) {
    var password = response.getResponseText();
    var scriptProperties = PropertiesService.getScriptProperties();
    var storedPassword = scriptProperties.getProperty('EXECUTION_PASSWORD');

    if (password === storedPassword) {
      var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
      var startRow = 2;  
      var numRows = sheet.getLastRow() - 1;
      var dataRange = sheet.getRange(startRow, 1, numRows, 8);
      var data = dataRange.getValues();

      for (var i = 0; i < data.length; ++i) {
        var row = data[i];
        var emailAddress = row[3];
        var subject = row[4];
        var qrCodeUrl = row[6];
        
        if (emailAddress && subject && qrCodeUrl) {
          var htmlBody = `
            <p>Hello Friends,</p>
            <p>Welcome to the 10th Anniversary Party of Dallas Boys,</p>
            <p><b>Please scan the QR code upon arrival at the front desk.</b></p>
            <div>
              <img src="${qrCodeUrl}" alt="QR Code" />
            </div>
            <p>Please do not share the QR code with anyone else unless you are transferring the ticket.</p>
            <p><b>Date and Time:</b><br>When: <b>Friday, Nov 31st, 2025 (5:30 PM - 11:30 PM)</b><br>Where: <b>Grandion Event Venue, 1810 Parkwood Blvd, Frisco, TX 75034</b> <a href="https://maps.app.goo.gl/sample">Location</a></p>
          `;
          
          MailApp.sendEmail({
            to: emailAddress,
            subject: subject,
            htmlBody: htmlBody
          });
        }
      }
      
      ui.alert('Emails sent successfully.');
    } else {
      ui.alert('Incorrect password. Access denied.');
    }
  } else {
    ui.alert('Action cancelled.');
  }
}
