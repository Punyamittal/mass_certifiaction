import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import smtplib
from email.message import EmailMessage
import os

# Load participant data
data = pd.read_csv('participants.csv')

# Certificate template and font settings
template_path = 'template.png'
font_path = "C:/Windows/Fonts/times.ttf"  # Times New Roman font path on Windows
font_size = 50  # Adjusted to fit within the line
output_dir = 'certificates'
os.makedirs(output_dir, exist_ok=True)

# Email credentials
EMAIL_ADDRESS = 'hackhub.team51@gmail.com'
EMAIL_PASSWORD = 'umjr tpcb bpdk kkoc'

def generate_and_send_cert(first, last, recipient_email):
    full_name = f"{first} {last}"

    cert = Image.open(template_path)
    draw = ImageDraw.Draw(cert)
    
    # Try to load font, with fallback
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        print(f"Font loading failed: {e}")
        # Use default font as fallback
        font = ImageFont.load_default()

    # Get text width for centering
    bbox = draw.textbbox((0, 0), full_name, font=font)
    text_width = bbox[2] - bbox[0]

    # Adjust coordinates to center text on dotted line
    x = (cert.width - text_width) // 2
    y = 250  # Move the name higher

    # Draw the text in black
    draw.text((x, y), full_name, fill='black', font=font)

    cert_filename = f"{output_dir}/{full_name.replace(' ', '_')}.png"
    cert.save(cert_filename)

    # Compose and send email
    msg = EmailMessage()
    msg['Subject'] = 'Your Certificate of Participation for HackHub 25'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg.set_content(f"""
Dear {full_name},

Congratulations on your achievement!

Please find your certificate attached as a token of appreciation for your participation in HackHub 2025. We were thrilled to have you as part of the event and commend your dedication and innovation.

Wishing you all the best in your future endeavors.

Sincerely,  
Team HackHub
""")

    # Attach the generated certificate (not the template)
    with open(cert_filename, 'rb') as f:
        certificate_data = f.read()
        msg.add_attachment(certificate_data, maintype='image', subtype='png', filename=f"{full_name.replace(' ', '_')}_Certificate.png")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"✅ Sent to: {full_name} ({recipient_email})")

# Only send to first 10 for testing
for _, row in data.iterrows():
    generate_and_send_cert(row['First Name'], row['Last Name'], row['Email'])
