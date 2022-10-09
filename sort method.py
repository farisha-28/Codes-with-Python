# list sort ascending order

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# list descending order

cars = ['Ford', 'BMW', 'Volvo']
# print(cars.sort(reverse=True))
cars.sort(reverse=True)
print(cars)

# depending on length
def myFunc(f):
  return len(f)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)


def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)

# dictionary

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)