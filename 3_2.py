def send_email(message, recipeint, *, sender='university.help@gmail.com'):
    if '@' or '.com' or '.ru' or '.net' not in sender:
        if '@' or '.com' or '.ru' or '.net' not in recipeint:
            print('Невозможно отправить письмо с адреса на адрес')
    if sender == recipeint:
        print('Нельзя отправить сообщение самому себе')
    if sender =='university.help@gmail.com':
        print('Письмо успешно отправлено с адреса  на адрес .')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.')

print(send_email('Привет, друг!', 'friend@mail.com'))
