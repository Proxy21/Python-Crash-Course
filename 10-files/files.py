with open('pi.txt') as file_objects:
    contents = file_objects.read()
    print(contents.rstrip())
