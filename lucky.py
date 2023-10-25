with open("mydefaults.ini.txt") as ini_file:
    contents = ini_file.read()
    letter_count = 0
    number_count = 0
    for char in contents:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            number_count += 1

print("Number of letters:", letter_count)
print("Number of digits:", number_count)
