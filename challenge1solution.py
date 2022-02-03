# Challenge 1 Solution
# By: Robert Hereth

import csv

# Opens file of data for task, creates two dictionaries
# Note: Code split into two different 'with' blocks due to error when running both dictionaries in one block
with open('data/MontanaCounties.csv', mode='r') as data:
    reader = csv.reader(data)
    pre_county_dict = {cols[2]: cols[0] for cols in reader}

with open('data/MontanaCounties.csv', mode='r') as data:
    reader = csv.reader(data)
    pre_seat_dict = {cols[2]: cols[1] for cols in reader}


# Searches both dictionaries to output info
def search_both(num):
    userinfo = [num, "c", "s"]
    userinfo[1] = search_county(userinfo[0])[1]
    userinfo[2] = search_seat(userinfo[0])[2]
    return userinfo


# Searches county dictionary
def search_county(num):
    userinfo = [num, "c", "s"]
    if userinfo[0] in pre_county_dict:
        userinfo[1] = pre_county_dict[userinfo[0]]
    return userinfo


# Searches seat dictionary
def search_seat(num):
    userinfo = [num, "c", "s"]
    if userinfo[0] in pre_seat_dict:
        userinfo[2] = pre_seat_dict[userinfo[0]]
    return userinfo


# Text at start of program
def pre_text():
    print("Welcome to the Montana County License Lookup Application!")
    print("Made by: Robert Hereth")
    print()


# User input session
def user_text():
    exitflag = False
    while not exitflag:
        print("Please enter what information you would like:")
        print("  'c' - County \n  's' - Seat \n  'b' - Both County and Seat\n  'e' - Exit Program")
        print()
        search = input()
        print()
        if search != 'c' and search != "s" and search != "b" and search != "C" \
                and search != "S" and search != "B" and search != "e" and search != "E":
            print("INVALID INPUT")
            print()
        elif search != "e" and search != "E":
            print("Please enter the license number you would like to look up: ")
            lnum = input()
            if search == "c" or search == "C":
                printinfo(search_county(lnum))
            elif search == "s" or search == "S":
                printinfo(search_seat(lnum))
            elif search == "b" or search == "B:":
                printinfo(search_both(lnum))
            else:
                print("BROKEN CODE")
        else:
            print("Thank you for using the Montana County License Lookup Application!")
            print("Have a great day!")
            exitflag = True


def printinfo(info):
    print()
    if info[1] == 'c' and info[2] == 's':
        print("INFO NOT FOUND: INVALID LICENSE NUMBER")
    else:
        print(f"License Number: {info[0]}")
        if info[1] != 'c':
            print(f"County: {info[1]}")
        if info[2] != 's':
            print(f"Seat: {info[2]}")
    print()


if __name__ == '__main__':
    pre_text()
    user_text()

