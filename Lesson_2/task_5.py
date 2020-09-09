my_list = [7, 5, 3, 3, 2]
number = input("Enter mark or enter 'q' for exit: ")
while number != "q":
    i = 0
    number = int(number)
    while i <= len(my_list):
        if number >= my_list[i]:
            my_list.insert(i, number)
            i = len(my_list)
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
            i = len(my_list)
        i += 1
    print(my_list)
    number = input("Enter mark or enter 'q' for exit: ")
