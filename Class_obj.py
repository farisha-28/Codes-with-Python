class Drama:
    def place(self):
        print("Turkish.")
    def alluring(self):
        print('Istanbul.')

Drama_1 = Drama()
Drama().place()
print(Drama().alluring())

Drama_2 = Drama()
Drama_2.a = 30
print(Drama_2.a)