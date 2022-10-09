phone = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
}
digit = input('Phone: ')
output = ""
for value in digit:

    # Passing ! for that value which doesnt exist in dictionary
    output += phone.get(value," ! ")+" "
print(output)