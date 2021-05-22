phoneNumber = input('Type in youre phone number (without "+" at the beggining): ')

# проверка на наличие цифр. Сделал 2 функции if, так как нужны разные виды ошибок
# так же добавил проверку телефонного кода, поэтому нужно вводить 12 символов
# (в международном формате)
if phoneNumber.isdigit() == True:
    if len(phoneNumber) == 12:
        print('Congratulations! You entered your phone number correctly!')
        # проверка телефонного кода Украины
        if phoneNumber[:3] == '380':
            print('You are from Ukraine!')
    else:
        print('Invalid phone number! It must be only 12 characters long!')
else:
    print('Invalid phone number! It must contain only only numerical characters!')
