year = int(input())

if 1900<=year<=pow(10,5):

    def is_leap():
        if year%4!=0 or (year%100==0 and year%400!=0):
            return False
        else:
            return True

    is_it = is_leap()
    print(is_it)

