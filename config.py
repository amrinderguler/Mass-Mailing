# Email configuration
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your SMTP server
EMAIL_PORT = 587  # Common port for TLS
EMAIL_USER = 'amrindersingh292004@gmail.com'  # Your email address
EMAIL_PASSWORD = 'ssrc xwrh hgfr pfwo'  # Your email password
EMAIL_SUBJECT = 'Seeking Job Opportunities'  # Subject of the email
LINKEDIN_URL = 'https://www.linkedin.com/in/amrinderguler'  # Your LinkedIn profile URL
RESUME_PATH = 'Assets\Amrinder_Singh-Resume.pdf'  # Path to your resume file

EMAIL_BODY = '''\
Hello,

I hope this message finds you well. My name is Amrinder, and I am currently seeking job opportunities as a Python Developer at Test.it. I am very interested in the work your company is doing and believe my skills and experiences align well with your team.

I have attached my resume for your review, and you can also view my LinkedIn profile here: {linkedin_url}. I would greatly appreciate any guidance or opportunities you might have available.

Thank you for your time, and I look forward to hearing from you.

Best regards,
Amrinder Singh
'''  # Sample email body

# Path to the Excel file containing email addresses
EXCEL_FILE_PATH = 'Assets\Book1.xlsx'  # Update with your actual file path
