weight = input("Weight: ")
decision = input("Pound (L)bs or K(g): ")
if decision.upper() == 'K':
    in_pounds =float(weight) /.45
    print(f'You are {in_pounds} pounds.')
elif decision.upper() == 'L':
    in_kg = float(weight)*.45
    print(f'You are {in_kg} kgs.')
else:
    print("You don't even exist !! -_-")