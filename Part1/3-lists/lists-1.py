bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
message = "My first bicycle was a " + bicycles[2] + "."
print(message)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
