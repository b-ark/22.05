#  решил сделать программу "многоразовой"
#  переменная "keyword" - ключ для остановки программы
keyword = 'y'

while keyword == 'y' or keyword == 'Y':
    startStr = input('Type in your string: ')

    if len(startStr) >= 2:
        result = startStr[0:2] + startStr[-2:]
        print('\n', startStr, ' ---> ', result, sep='')
    else:
        print('')
        
    keyword = input('Do you want to try again? ("y" - yes, "n" - no) ')
    
    #  фраза для пользователей, которые не читают иснтрукцию :)
    if keyword != 'y' and keyword != 'Y' and keyword != 'n' and keyword != 'N':
        print('I will consider this as "no"')
