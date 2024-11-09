# Email configuration
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your SMTP server
EMAIL_PORT = 587  # Common port for TLS
EMAIL_USER = # Your email address
EMAIL_PASSWORD = # Your email password
EMAIL_SUBJECT = 'Seeking Job Opportunities'  # Subject of the email
LINKEDIN_URL = 'https://www.linkedin.com/in/username'  # Your LinkedIn profile URL
RESUME_PATH = 'path/to/resume'  # Path to your resume file

EMAIL_BODY = '''\
Hello,

I hope this message finds you well. My name is [Your Name], and I am currently seeking job opportunities as a [Position] at [Company Name]. I am very interested in the work your company is doing and believe my skills and experiences align well with your team.

I have attached my resume for your review, and you can also view my LinkedIn profile here: {linkedin_url}. I would greatly appreciate any guidance or opportunities you might have available.

Thank you for your time, and I look forward to hearing from you.

Best regards,
[Yor Name]
'''  # Sample email body

# Path to the Excel file containing email addresses
EXCEL_FILE_PATH = 'path/to/your/excel-file'  # Update with your actual file path
