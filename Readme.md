# 🎓 Automated Certificate Generator

This is a Python-based mass certificate generator that automates the process of creating personalized participation certificates using a certificate **template image** and a **CSV file** containing participant details.

## 📁 Project Structure

📦certificate-generator/
┣ 📄 generate_certificates.py
┣ 📄 template.png
┣ 📄 participants.csv
┣ 📁 output/
┃ ┗ 📄 [Generated Certificates]
┗ 📄 README.md

markdown
Copy
Edit

## 📋 CSV Format

Ensure your `participants.csv` includes the following columns:

First Name,Last Name,Email,Portfolio Url,Submitted Project?,Project URLs,
City,State,Country,Project Count,College/University Name,Job Specialty,
Registered At,Do you have teammates?,Who told you about this hackathon?

markdown
Copy
Edit

At minimum, `First Name` and `Last Name` are required for certificate generation.

## 🖼 Template Format

- Your certificate **template image** should have a blank line or designated area where the name will be printed.
- Supported formats: `.png`, `.jpg`

## ⚙️ How It Works

1. Reads participant data from `participants.csv`.
2. Places each participant's full name on the certificate template.
3. Saves individual certificates to the `output/` folder.

## 🛠 Dependencies

Make sure you have Python 3 installed. Then run:

```bash
pip install pillow pandas
🚀 Usage
bash
Copy
Edit
python generate_certificates.py
✍️ Customization
Modify the font style, size, and position inside the generate_certificates.py script to match your template layout.

You can also add more information (e.g., project name, college) on the certificate if needed.

📂 Output
Generated certificates are saved in the output/ folder as:

csharp
Copy
Edit
[FirstName_LastName]_certificate.png
🧑‍💻 Author
Developed for Hackathon organizers looking to automate post-event tasks efficiently.

Feel free to fork, contribute, or customize!

yaml
Copy
Edit

---

Let me know if you'd like me to write the `generate_certificates.py` script too.
# ysoc_invite
