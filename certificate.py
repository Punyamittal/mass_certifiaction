import pandas as pd
import smtplib
from email.message import EmailMessage

# Load recipient data
data = pd.read_csv('participants.csv')  # Must have columns: First Name, Last Name, Email

# Email credentials
EMAIL_ADDRESS = 'punya.m215@gmail.com'
EMAIL_PASSWORD = 'ogdj daaa sskv hktu'
def send_invitation(first, last, recipient_email):
    full_name = f"{first} {last}"

    # Create the email
    msg = EmailMessage()
    msg['Subject'] = 'Invitation to Join YSOC — Youth Society of Coders'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email

    # Invitation message
    msg.set_content(f"""
Dear {full_name},

We’re excited to invite you to join **YSOC — the Youth Society of Coders**, a vibrant community of passionate innovators, developers, and problem solvers.

YSOC aims to bring together students who love technology, coding, and creativity — providing a space to collaborate, learn, and build impactful projects together.  
As a member, you’ll get access to:
- Regular coding sessions and workshops  
- Hackathons and innovation challenges  
- Mentorship from experienced developers  
- Networking opportunities with like-minded peers  

If you're ready to elevate your skills and be part of something bigger, we’d love to have you on board!

👉 **Join Now:** [Insert Registration Link Here]

Let’s build the future, one line of code at a time.

Warm regards,  
**Team YSOC**  
Youth Society of Coders
""")

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"✅ Invitation sent to: {full_name} ({recipient_email})")

# Send invitation to all participants
for _, row in data.iterrows():
    send_invitation(row['First Name'], row['Last Name'], row['Email'])
