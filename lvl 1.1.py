input_string = input("Enter a string: ")
n = int(input_string[0])
name = input_string[1:]

new_name = ""

for i in range(len(name)):
    if (i + 1) % n == 0:
        new_name += "z"
    else:
        new_name += name[i]

print(new_name)
