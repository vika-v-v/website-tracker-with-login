import hashlib
import requests
import smtplib
import time
from email.message import EmailMessage

def fetch_page(url, login_url, username, password):
    session = requests.Session()

    payload = {
        'username': username, 
        'password': password
    }

    session.post(login_url, data=payload)

    response = session.get(url)
    return response.text

def get_content_hash(content):
    content_hash = hashlib.md5()
    content_hash.update(content.encode('utf-8'))
    return content_hash.hexdigest()

def has_content_changed(old_hash, new_hash):
    return old_hash != new_hash

def send_email(subject, body, to, gmail_user, gmail_password):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = gmail_user

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()

def main():
    url = 'https://your-website'  
    login_url = 'https://login-url'
    username = 'username-for-login'
    password = 'password-for-login'
    check_interval = 60 * 60  # Check every hour
    gmail_user = 'your-email@gmail.com'
    gmail_password = 'your-email-password'
    to = 'recipient-email@gmail.com'
    
    old_hash = None

    while True:
        try:
            new_content = fetch_page(url, login_url, username, password)
            new_hash = get_content_hash(new_content)

            if old_hash and has_content_changed(old_hash, new_hash):
                send_email('Website changed', f'The website you are tracking was changed', to, gmail_user, gmail_password)

            old_hash = new_hash
        except Exception as e:
            print(e)

        time.sleep(check_interval)

if __name__ == "__main__":
    main()
