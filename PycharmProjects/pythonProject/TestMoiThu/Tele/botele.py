from telegram.ext import Application, CommandHandler, ContextTypes
import imaplib
import email
from email.header import decode_header

# Thông tin bot và email
TELEGRAM_TOKEN = '6842308601:AAE1ZmD8FdMojPsaOKN4LG1ppi7XlPJ81oY'
CHAT_ID = '-1002236822280'
EMAIL_ACCOUNT = '20210463@eaut.edu.vn'
EMAIL_PASSWORD = 'NgoLongVu19092003'
EMAIL_SERVER = 'imap.gmail.com'
# Kết nối tới email
mail = imaplib.IMAP4_SSL(EMAIL_SERVER)
mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
mail.select('inbox')

async def check_mail(update, context):
    status, messages = mail.search(None, 'UNSEEN')
    for num in messages[0].split():
        typ, data = mail.fetch(num, '(RFC822)')
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = decode_header(msg['subject'])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                body = msg.get_payload(decode=True).decode()
                # Gửi nội dung tới nhóm Telegram
                await context.bot.send_message(chat_id=CHAT_ID, text=f"New email: {subject}\nContent: {body}")

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    check_mail_handler = CommandHandler('check_mail', check_mail)
    application.add_handler(check_mail_handler)
    application.run_polling()

if __name__ == "__main__":
    main()
