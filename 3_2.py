def send_email(message, recipient, *args, sender='university.help@gmail.com'):
    sobaka = '@'
    end = ('.com', '.net', '.ru')
    flag = False
    if sobaka in recipient:
        for _ in end:
            if _ in recipient:
                flag = True
    if flag is False:
        error = f'Невозможно отправить письмо с адреса {sender} на адрес{recipient}.'
        return error
    sobaka = '@'
    end = ('.com', '.net', '.ru')
    flag = False
    if sobaka in sender:
        for _ in end:
            if _ in sender:
                flag = True
    if flag is False:
        error = f'Невозможно отправить письмо с адреса {sender} на адрес{recipient}.'
        return error
    if recipient == sender:
        error1 = f'Нельзя отправить письмо самому себе!'
        return error1
    if sender != 'university.help@gmail.com':

        service_message = f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.'
        return service_message
    else:
        success = f'Письмо успешно отправлено с адреса с адреса {sender} на адрес {recipient}.'
        return success

print(send_email('ALLO, MAGNUS, ETO TI?', 'russ@fenrir.com'))
print(send_email('Hydra Dominatus!', 'korax@raven.com', sender='alfary@alfa.com'))
print(send_email('Perturabo, ti gde?', 'dorn@fallanga.warp'))
print(send_email('Ti poekhavshiy? Ty kuda pishseh?', 'guilimann@ultramar.com', sender='guilimann@ultramar.com'))
