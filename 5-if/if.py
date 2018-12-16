cars = ['ford', 'chevy','honda','tesla','bmw']

for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.lower())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',}
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
