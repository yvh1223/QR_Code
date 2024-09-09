

Guest Check-In Process Automation
This process outlines how to automate capturing guest details, generating QR codes, and sending sign-in emails for event check-ins.

**Steps Overview
**

Step 1: Capture Guest Information
Task: Collect guest details, including their email addresses.
1.1: Email is mandatory for each guest.
1.2: Owners will also provide the number of bands to be given to each guest.
1.3: As some guests may make last-minute payments, these steps need to be repeated often. Inform owners that QR codes will be sent in batches to streamline the process.
1.4: Email subject headers should include the keyword "QR-Code - SOMETHING" for easier identification.
1.5: Gmail accounts can send up to 500 emails per day, which is important to note when batching emails.

Step 2: Google Form for Attendance Tracking
Task: Create a Google Form and capture sample responses using the guest's first and last names for later use in attendance tracking.

Step 3: Generate Sign-In Links
Task: For each guest, generate an individual sign-in link using their name and the event's Google Form for check-in tracking.

Step 4: Prevent Duplicate Check-Ins
Task: Validate guest check-ins to prevent duplicate entries by cross-referencing previous sign-ins to ensure guests are only checked in once.

**Best Practices
**

Send emails in small batches, e.g., only 10 emails at a time.


**Send Email - QR Code - Template
**https://docs.google.com/spreadsheets/d/1XPdaIcgDndq-At378ooiwkPq1uIGf4-ZPXqJ3A7EuzQ/edit?gid=0#gid=0


**Sample code (Google Script to send Email) : 
**https://github.com/yvh1223/QR_Code/blob/main/Gscript.py


