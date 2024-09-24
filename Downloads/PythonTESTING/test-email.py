import time
import schedule
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, content, to_email):
    # Email credentials
    from_email = "lessi.living@gmail.com"
    password = "xcadgnycdqznapvk"  # Use an app-specific password if using Gmail

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(content, 'plain'))

    # Setup the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Start TLS encryption
    server.login(from_email, password)

    # Send the email
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)

    # Close the server
    server.quit()

    print(f"Email sent to {to_email}")


# Content for the weekly email

def weekly_email():
    subject = "Weekly Update from Medebound"
    content = "This is your weekly email content. Include the dynamic content here!"
    to_email = "xl2104@gmail.com"

    send_email(subject, content, to_email)


# Schedule the job to run every week
schedule.every().thursday.at("17:59").do(weekly_email)

# Keep the script running to execute the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(60)  # Sleep to prevent CPU overuse
