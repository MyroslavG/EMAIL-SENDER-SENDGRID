import sendgrid
from sendgrid.helpers.mail import Mail

api_key = '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'

def send_email(sender_email, recipient_email, subject, message):
    # Create a Mail object
    email = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject=subject,
        plain_text_content=message)

    try:
        # Send the email
        sg = sendgrid.SendGridAPIClient(api_key=api_key)
        response = sg.send(email)
        print('Email sent successfully!')
    except Exception as e:
        print('Error sending email:', str(e))

send_email('povodyrshop@gmail.com', 'povodyrshop@gmail.com', 'Hello', 'Bla bla')