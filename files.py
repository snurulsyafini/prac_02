# 1)
# out_file = open("name.txt", "w")
# name = input("What's your name?: ")
# print(name, file=out_file)
# out_file.close()

# 2)
# out_file = open("name.txt", "r")
# name = out_file.readline()
# print(name)
# out_file.close()

# 3)
# total = 0
# in_file = open("numbers.txt", "r")
# number_1 = in_file.readline()
# number_2 = in_file.readline()
# for number in in_file:
#     total = total + int(number_1) + int(number_2)
#     print(total)
# in_file.close()

# 4)
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    numbers = in_file.readlines()
    for number in numbers:
        total = total + int(number)
    print(total)
in_file.close()

