def send_email(message,recipient,sender = "univerity.help@gmail.com"):
    if("@"and(".com"or".ru"or".net")) not in (recipient or sender) or("@" or(".com"or"ru"or".net")) not in (recipient or sender):
        print(f"Невозможно отправить письмо с адреса {sender}на адрес {recipient}")
    elif recipient == sender:
        print(f"Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса{sender} на адрес {recipient}.")
    elif sender !="university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com', "univerity.help@gmail.com")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.info@gmail.com', 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru',  'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'vasyok1337@gmail.com',  "university.help@gmail.com")