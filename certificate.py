import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import smtplib
from email.message import EmailMessage
import os
data = pd.read_csv('participants.csv')  
template_path = 'template.png'     
font_path = 'arial.ttf'               
font_size = 60
output_dir = 'certificates'
os.makedirs(output_dir, exist_ok=True)
EMAIL_ADDRESS = 'hackhub.team51@gmail.com'
EMAIL_PASSWORD = 'umjr tpcb bpdk kkoc'  
def generate_and_send_cert(first, last, recipient_email):
    full_name = f"{first} {last}"
    cert = Image.open(template_path)
    draw = ImageDraw.Draw(cert)
    font = ImageFont.truetype(font_path, font_size)
    text_width, _ = draw.textsize(full_name, font=font)
    x = (cert.width - text_width) // 2
    y = 600 
    draw.text((x, y), full_name, fill='black', font=font)
    cert_filename = f"{output_dir}/{full_name.replace(' ', '_')}.png"
    cert.save(cert_filename)
    msg = EmailMessage()
    msg['Subject'] = 'Your Certificate of Participation'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_email
    msg.set_content(f"Hi {full_name},\n\nPlease find your certificate attached. Congratulations!\n\nBest,\nTeam HackHub")
    with open(cert_filename, 'rb') as f:
        msg.add_attachment(f.read(), maintype='image', subtype='png', filename=os.path.basename(cert_filename))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"✅ Sent to: {full_name} ({recipient_email})")
for _, row in data.iterrows():
    generate_and_send_cert(row['First Name'], row['Last Name'], row['Email'])
