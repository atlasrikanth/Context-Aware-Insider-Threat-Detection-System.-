import smtplib
from email.mime.text import MIMEText

def send_alert(user_id, activity):
    subject = "Insider Threat Alert"
    body = f"Suspicious activity detected: User {user_id} performed {activity}."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "security@company.com"
    msg['To'] = "admin@company.com"

    # Send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("your_email@gmail.com", "your_password")
        server.sendmail("your_email@gmail.com", "admin@company.com", msg.as_string())

# Example usage
send_alert(1, "file_access")