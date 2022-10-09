while True:
    try:
        age=int(input("Age in month: "))
        per_year = int(input("How many months per year: "))
        years = age/per_year
        print(years)
        break
    except ValueError:
        print("Invalid type")
    except ZeroDivisionError:
        print("Can't be zero.")

