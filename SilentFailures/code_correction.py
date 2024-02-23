try:
    x = 1 / "st"
except (ZeroDivisionError, ValueError, TypeError):
    pass

filename = input("Enter name of the file to read: ")

try:
    with open (filename, "r") as f:
        contents = f.read()
except FileNotFoundError:
    pass

print(contents)