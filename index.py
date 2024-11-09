from flask import Flask, request, jsonify
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD, EMAIL_SUBJECT, EMAIL_BODY, LINKEDIN_URL, RESUME_PATH, EXCEL_FILE_PATH

app = Flask(__name__)

@app.route('/send_emails', methods=['POST'])
def send_emails():
    # Load email addresses from the specified Excel file
    df = pd.read_excel(EXCEL_FILE_PATH)
    email_list = df['Email'].tolist()  # Assuming the column is named 'Email'

    # Set up the SMTP server
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)

        for email in email_list:
            # Create a multipart email
            msg = MIMEMultipart()
            msg['Subject'] = EMAIL_SUBJECT
            msg['From'] = EMAIL_USER
            msg['To'] = email
            
            # Attach the email body
            body = EMAIL_BODY.format(linkedin_url=LINKEDIN_URL)
            msg.attach(MIMEText(body, 'plain'))

            # Attach the resume
            with open(RESUME_PATH, 'rb') as resume_file:
                resume_attachment = MIMEApplication(resume_file.read(), _subtype='pdf')
                resume_attachment.add_header('Content-Disposition', 'attachment', filename='resume.pdf')
                msg.attach(resume_attachment)

            # Send the email
            server.sendmail(EMAIL_USER, email, msg.as_string())

    return jsonify({"status": "Emails sent successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
