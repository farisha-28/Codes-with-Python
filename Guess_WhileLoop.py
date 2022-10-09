guess_number = 9
guess_limit = 3
number = 1
while number <= guess_limit:
    num = int(input('Guess: '))
    number += 1
    if num == guess_number:
        print('Done!')
        break
else:
    print('Sorry you Failed !')

i = 1
while i<=5:
    print(i*'*' )
    i += 1
