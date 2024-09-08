function setPasswords() {
  var scriptProperties = PropertiesService.getScriptProperties();
  scriptProperties.setProperty('EXECUTION_PASSWORD', 'RCB');
}

function sendEmails() {
  var ui = SpreadsheetApp.getUi();
  var response = ui.prompt('Execution Password', 'Please enter the password to send emails:', ui.ButtonSet.OK_CANCEL);

  // Check if the user clicked "OK" and entered the correct password
  if (response.getSelectedButton() == ui.Button.OK) {
    var password = response.getResponseText();
    var scriptProperties = PropertiesService.getScriptProperties();
    var storedPassword = scriptProperties.getProperty('EXECUTION_PASSWORD');

    if (password === storedPassword) {  
      var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
      var startRow = 2;  // First row of data to process
      var numRows = sheet.getLastRow() - 1;  // Number of rows to process
      var dataRange = sheet.getRange(startRow, 1, numRows, 8);  // Adjust the number of columns to include all needed columns
      var data = dataRange.getValues();
      
      for (var i = 0; i < data.length; ++i) {
        var row = data[i];
        var emailAddress = row[3];  // Fourth column (D)
        var subject = row[4];       // Fifth column (E)
        var qrCodeUrl = row[6];     // Seventh column (G)
        
        if (emailAddress && subject && qrCodeUrl) {  // Ensure no empty values
          var htmlBody = `
            <p>ನಮಸ್ಕಾರ ಗೆಳೆಯರೆ,</p>
            <p>ಡಲ್ಲಾಸ್ ಬಾಯ್ಸ್ - 10 ನೇ ವಾರ್ಷಿಕೋತ್ಸವದ ಪಾರ್ಟಿಗೆ ಸುಸ್ವಾಗತ,</p>
            <p>ಕುಡಿಯೋಣ ಮತ್ತು ಕುಣಿಯೋನಾ ಮತ್ತು ಮಸ್ತ್ ಮಜಾ ಮಾಡೋನಾ</p>
            <p><b>Please scan the QR code upon arrival at the front desk.</b></p>
            <div>
              <img src="${qrCodeUrl}" alt="QR Code" />
            </div>
            <p>Please do not share the QR with anyone else, unless if you are transfering the ticket.</p>
            <p><b>Date and Time</b><br>When: <b>Friday, May 31st, 2024 (5:30 PM - 11:30 PM)</b><br>Where: <b>Grandion Event Venue, 1810 Parkwood Blvd, Frisco, TX 75034</b> <a href="https://maps.app.goo.gl/attRRkquu3VjQBsz8">Location</a></p>
            
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
