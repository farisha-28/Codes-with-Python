house_price = 1000000

good_credit = True

if good_credit:
    downPayment = 0.1*house_price
else:
    downPayment = 0.2*house_price
print(f'Down Payment is : ${downPayment}')

goodCredit = True
has_criminal_record = False
became_good = False
for_office = False

if goodCredit and has_criminal_record:
    print('Can rent the house.')
elif for_office or became_good:
    print("Can't buy the house")
elif goodCredit and not has_criminal_record:
    print("Can buy the house.")

# logical Operator exercise
name = 'Farisha Hussain iker casillas burak deniz engin Ozturk'
name_len = len(name)

if name_len < 3:
    print('Name must be 3 characters long.')
elif name_len >50:
    print("Name can be a maximum of 50 characters.")
else:
    print("Name looks good.")