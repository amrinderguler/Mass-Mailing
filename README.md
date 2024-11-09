# Mass Mailing Application

This Flask application allows you to send mass emails with attachments using Gmail's SMTP server. It reads email addresses from an Excel file and sends a personalized email to each recipient.

## Features

- Load email addresses from an Excel file.
- Send personalized emails with a subject and body.
- Attach a resume or any other document to the email.
- Uses Gmail's SMTP server for sending emails.

## Prerequisites

- Python 3.x
- Flask
- Pandas
- Openpyxl (for reading Excel files)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/amrinderguler/Mass-Mailing
   cd Mass-Mailing
   ```

2. **Install the required packages:**
   ```bash
   pip install Flask pandas openpyxl
   ```

3. **Configure your email settings:**
   - Open `config.py` and update the following variables:
     - `EMAIL_USER`: Your Gmail address.
     - `EMAIL_PASSWORD`: Your Gmail password (consider using an App Password for security).
     - `RESUME_PATH`: Path to your resume file.
     - `EXCEL_FILE_PATH`: Path to the Excel file containing email addresses.
     - Also Update the Email Body

## Usage

1. **Run the application:**
   ```bash
   python index.py
   ```

2. **Send emails:**
   - Make a POST request to the `http://127.0.0.1:5000/send_emails` endpoint. You can use tools like Postman or cURL to send the request.

   Example using cURL:
   ```bash
   curl -X POST http://127
