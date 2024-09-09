# Guest Check-In and QR Code Email Automation

This project outlines the steps to automate guest check-ins using QR codes and email communication. It involves collecting guest information, generating QR codes from Google Form responses, and sending emails using Google Apps Script.

## Process Overview

### Step 1: Collect Guest Information

**Task**: Collect the guest's first name, last name, and email address.

- **Required Fields**:
  - First Name
  - Last Name
  - Email Address (mandatory)
  
**Notes**:
- The guest's email address is required to send the QR code.
- Event owners may also provide the number of wristbands or tickets assigned to each guest.
- Inform event owners that guests making last-minute payments will need to have QR codes sent in batches.

**Constraints**:
- Gmail accounts have a limit of **500 emails per day**, so plan accordingly for batch sending.

### Step 2: Create a Google Form for Attendance

**Task**: Create a Google Form to collect responses for guest check-ins.

1. **Form Fields**:
   - First Name
   - Last Name
   - Email Address

2. **Sample Response**:
   After setting up the form, make a few sample entries. This will generate a unique response URL for each guest.

3. **Use Case**:
   The sample response URL will be used later to generate a QR code for each guest’s check-in.

### Step 3: Generate QR Codes

**Task**: Generate a QR code for each guest based on their Google Form response URL.

- The Google Form submission will generate a unique URL.
- Use this URL to create a QR code using a QR code generation API such as `qrserver.com`.

**Example**:
QR Code API: https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=Google_Form_Response_URL


**Send Email - QR Code - Template
**https://docs.google.com/spreadsheets/d/1XPdaIcgDndq-At378ooiwkPq1uIGf4-ZPXqJ3A7EuzQ/edit?gid=0#gid=0


Step 4: Send QR Codes via Email
Task: Send an email to each guest with their unique QR code.

Use Google Apps Script to automate the email-sending process.
The script will generate a custom email for each guest containing their name, event details, and QR code.
Google Apps Script:
https://github.com/yvh1223/QR_Code/blob/main/Gscript.py

## Batch Processing

- **Send emails in batches of 50** to avoid exceeding Gmail limits.
- **Clean up the spreadsheet** after sending emails to avoid duplicate entries.

## Step 5: Prevent Duplicate Check-Ins

**Task**: Validate and prevent duplicate check-ins.

- When a guest scans their QR code, the system should log the check-in.
- Ensure that guests cannot check in more than once by validating the guest’s status in the spreadsheet linked to the Google Form.

## Step 6: Customize and Maintain

- **Customizations**: The Google Apps Script allows you to customize the subject and content of the emails.
- **Spreadsheet Management**: Regularly update and maintain the spreadsheet with guest details, QR codes, and check-in statuses.

## Best Practices

- **Batch Emails**: Limit email batches to **50 guests at a time** to avoid exceeding Gmail's daily limits.
- **Use Unique QR Codes**: Ensure each guest receives a unique QR code for their check-in.
- **Regular Cleanup**: Clean up the spreadsheet after processing to avoid re-sending emails or duplicating QR codes.

## Example Spreadsheet Structure

| First Name | Last Name | Full Name | Email Address    | Subject                         | Google Form Link               | QR Code URL                    | QR Code Image                 |
|------------|-----------|-----------|------------------|---------------------------------|---------------------------------|--------------------------------|-------------------------------|
| Y          | H         | Y-H       | yh@gmail.com      | QR Code - Dallas Boys Party 2024 | [Google Form](#)                | [QR Code](#)                   | QR Code Image                 |
| C          | S         | C-S       | cs@gmail.com      | QR Code - Dallas Boys Party 2024 | [Google Form](#)                | [QR Code](#)                   | QR Code Image                 |

Excel sheet formule: 
  Google Form Link =
   "https://docs.google.com/forms/d/e/1FAIpQLSco8pvBHP5GXSpdGTOmKlevsM5t1U-00-ruKEnvuOBx4gJ-dg/formResponse?entry.232573758="&C2
  QR Code URL =
  "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data="&F2
 QR Code Image =
  =image(G2)

**Sample Google Form (To capture Check-ins): 
**https://docs.google.com/forms/d/1NWSpi2RLNuTU46MK03S3fw3EDvzzwo1opzhZhrvz_NU/edit

**Sample Google Sheet to Send emails: 
**
https://docs.google.com/spreadsheets/d/1XPdaIcgDndq-At378ooiwkPq1uIGf4-ZPXqJ3A7EuzQ/edit?gid=0#gid=0
