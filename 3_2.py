def send_email(message, recipient, *args, sender='university.help@gmail.com'):
    sobaka = '@'
    end = ('.com', '.net', '.ru')
    flag = False
    if sobaka in recipient:
        for _ in end:
            if _ in recipient:
                flag = True
    if flag is False:
        error = ('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient, '.')
        return error
    sobaka = '@'
    end = ('.com', '.net', '.ru')
    flag = False
    if sobaka in recipient:
        for _ in end:
            if _ in recipient:
                flag = True
    if flag is False:
        error = ('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient, '.')
        return error
    if recipient == sender:
        error1 = ('Нельзя отправить письмо самому себе!')
        return error1
    sender = 'university.help@gmail.com'
    check_sender = 'university.help@gmail.com'
    flag = True
    if check_sender in sender:
        if _ in sender:
            if _ in check_sender:
                flag = False
    if not flag:
        service_message = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, 'на адрес', recipient
        return service_message
    else:
        success = ('Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient,'.')
        return success


print(send_email('Hello, World', 'bobr_kurwa@mail.ru'))
