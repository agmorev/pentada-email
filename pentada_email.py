import smtplib
from email.message import EmailMessage
import pandas as pd
import time


# Reading list of
df = pd.read_excel('email_list.xlsx', sheet_name=0)

try:
    server = smtplib.SMTP_SSL('mail.pentada-trans.com', 465)
    server.ehlo()
    server.login('office@pentada-trans.com', 'Zur*^29583wsPk')

    # Iterate through the list of emails and send a message to each email
    for index, row in df.iterrows():
        print(row['Пошта'])
        try:
            msg = EmailMessage()
            msg.set_content('''
Шановні учасники зовнішньоекономічної діяльності!
Незважаючи на війну та непрості економічні реалії наша компанія ПТ "ПЕНТАДА ТРАНС" продовжує працювати.
Ми видаємо фінансові гарантії нашим клієнтам для забезпечення критично важливої логістики товарів.

Тому якщо ви:
❓ надаєте митно-брокерські послуги
❓ переміщуєте товари в режимі транзиту
❓ імпортуєте або експортуєте товари
❓ надаєте послуги міжнародних перевезень

Економте час та кошти‼️ Користайтесь ⚙️ електронними ⚙️ митними фінансовими гарантіями‼️

⚡ видача, обіг та вивільнення фінансових гарантій виключно в електронному вигляді
⚡ не потрібно резервувати кошти на рахунках митниці
⚡ не потрібно витрачати час бухгалтерів та керівника
⚡ не потрібно залучати кредитні ресурси для операційної діяльності
⚡ лише пряма взаємодія гаранта з вашим митним брокером та митницею
⚡ цілодобова підтримка
⚡ видача фінансової гарантії за 3-5 хвилин

Для суб’єктів високої ділової активності під усі особливості логістики та обсяги поставок. Гарантія «Стандарт», «Універсальна» та «Ліміт без обмежень».

Деталі: http://bit.ly/3r0wHB2

‼️‼️‼️
Для забезпечення зручної та комфортної роботи пропонуємо скористатися безкоштовним Telegram-застосунком PentadaBot https://t.me/pentada_bot (для пошуку в месенджері @pentada_bot)
Деталі у додатку до цього повідомлення.
‼️‼️‼️

З повагою
уповноважений фінансовий гарант
ПТ "ПЕНТАДА ТРАНС"

Наші контакти:
Оформлення фінансових гарантій (24/7):
☎️ +38 (067) 447 60 66 (оператори)
📧 zayavka_gd@pentada-trans.com

Інші питання:
☎️ +38 (067) 476 97 80
☎️ +38 (067) 476 97 91
☎️ +38 (067) 321 36 65
📧 office@pentada-trans.com

Наша веб-сторінка:
💻 http://www.pentada-trans.com/

Ми в соцмережах:
Facebook: https://www.facebook.com/pentadatrans/
Telegram: https://t.me/pentada_bot (для пошуку в месенджері @pentada_bot)
            ''')
            msg['Subject'] = 'МИТНИЦЯ: митні гарантії - НІ депозитам!!!'
            msg['From'] = "office@pentada-trans.com"
            msg['To'] = row['Пошта']
            with open("commercial_offer.pdf", 'rb') as fp:
                pdf_data = fp.read()
                ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                msg.add_attachment(pdf_data, maintype=maintype, subtype=subtype, filename='commercial_offer.pdf')
            server.send_message(msg)
            print(str(index), "Пошту відправлено для {}".format(row['Пошта']))
            time.sleep(10)
        except:
            time.sleep(10)
            continue
except Exception as exception:
    print('Something went wrong with connecting to server....{}'.format(exception))
print('All emails sent!')