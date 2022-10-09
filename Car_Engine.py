# input('>')
# print('start - to start the car')
# print('stop - to stop the car')
# print('quit - to exit the car')
# choice = input('>')
#
# while choice.lower()!='quit':
#     if choice.lower() == 'start':
#         print('Car started !')
#     elif choice.lower()=='stop':
#         print('Car stopped!')
#     elif choice.lower() =='quit':
#         print('Exited!')
#         break;
#     else:
#         print("I don't understand!")
#     choice = input('>')


# choice = input('>')
# start_c = 0
# stop_c = 0
#
# while choice.lower()!='quit':
#     if choice.lower() == 'start':
#         start_c +=1
#         if start_c >1:
#             print("Car has already started.")
#         else:
#               print('Car started !')
#
#     elif choice.lower()=='stop':
#         stop_c +=1
#         if stop_c>1:
#             print('Car has already stopped.')
#         else:
#              print('Car stopped!')
#     elif choice.lower()=='help':
#         print("""
# start - start the car
# stop  - stop the car
# quit  - exited """
# )
#     else:
#         print("I don't understand!")
#     choice = input('>')


choice = input('>')
start_c = False

while True:
    if choice.lower() == 'start':
        #  If start true hoi
        if start_c :
             print('Car has already started !')
        # If false hoi
        else:
            start_c = True
            print("Car started !")

    elif choice.lower()=='stop':
        # If start false hoi
        if not start_c:
             print('Car has already stopped!')
        # if start true hoi
        else:
            start_c  = False
            print('Car stopped.')

    elif choice.lower()=='help':
        print("""
start - start the car
stop  - stop the car
quit  - exited """
)
    elif choice.lower() =='quit':
         print('Exited!')
         break;
    else:
        print("I don't understand!")
    choice = input('>')
