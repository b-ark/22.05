login = 'mihail'
login_temp = input('Type in your name: ')

if login_temp == login or login_temp.lower() == login:
    print('Correct! Logging you in...')
else:
    print('Unauthorized intrusion! Turning on the security system...')
