import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    gmail_user = 'heon0128@gmail.com' # Gmail 주소 입력
    gmail_password = 'myqu clkf ghwy kesb' # Gmail 앱 비밀번호 입력

    # 이메일 메시지 구성
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    # Gmail SMTP 서버를 사용하여 이메일 전송
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_email, msg.as_string())
        server.close()

        print('이메일 전송 성공')
    except Exception as e:
        print(f'이메일 전송 실패: {e}')
