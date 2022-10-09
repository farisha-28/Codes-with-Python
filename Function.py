def yuksek(name,new):
    print(f'Hello. {name}{new}')
    print("Welcome Turkey.")

def cal_Ex(save,total,budget):
    print(f'Your bill is : {save}{total}{budget}')

print("Start")
yuksek(new='Farisha,',name='Engin!')
yuksek('Also Samiha.',"Sunshine")
print("Have you enjoyed ?")
cal_Ex('50$ ',total='50$ ',budget='100$ ')
print("Finished.")

def return_fun(value):
    return value*value
print(return_fun(3))

def cal_sum(value,num):
    print(value+num)
print(cal_sum(4,6))