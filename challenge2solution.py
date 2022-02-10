# Challenge 2 Solution
# By: Robert Hereth

# The base of the program is from Challenge 1 with modifications to how it is read and how data is processed

# Opens file of data for task, creates dictionary of current entries
myFile = open("data/cities.txt", "r")
city_num = {"City":"Plate Number"}
lines = myFile.readlines()
for l in lines:
    line = l.split(",")
    city_num.update({line[0].upper():line[1]})
myFile.close()


# Searches dictionary by city and returns whole entry as array
def search_num(city):
    userinfo = [city, "n"]
    if userinfo[0] in city_num:
        userinfo[1] = city_num[userinfo[0]]
    return userinfo


# Text at start of program
def pre_text():
    print("-------------------------------------------------------------------")
    print("Welcome to the Montana City License Lookup Application!")
    print("Made by: Robert Hereth")
    print("-------------------------------------------------------------------")
    print()


# Adds the new info to dictionary as well as the file
def not_found(city, num):
    myFile = open("data/cities.txt", "a")
    city_num[city] = num
    goods = f"{city},{num}\n"
    myFile.write(goods)
    myFile.close()


# User input session
def user_text():
    exitflag = False
    while not exitflag:
        print(f"Please enter what city you would like the plate prefix of\nor enter 'E' to exit:")
        print()
        print("** NOTE: All cities will display and save in full uppercase. **")
        print()
        search = input().upper()
        print()
        if search != "e" and search != "E":
            if search in city_num.keys():
                goods = [search, city_num[search]]
                printinfo(goods)
            else:
                print(f"The city provided, {search}, is not yet in this list.")
                print("If you would like to add it, please enter the plate prefix number.")
                print("If you would not like to add it to the list, type 'E': ")
                print()
                num = input()
                print()
                if num == "e" or num == "E":
                    print(f"{search} will not be added at this time.")
                    print()
                elif num.isnumeric():
                    print(f"Adding {search} with plate prefix {num} to database.\nPlease wait.")
                    not_found(search, num)
                    goods = [search, city_num[search]]
                    printinfo(goods)
                else:
                    print("INVALID INPUT: VALUE NOT NUMERIC")
            print()
        elif search == "e" or search == "E":
            print("Thank you for using the Montana County License Lookup Application!")
            print("Have a great day!")
            exitflag = True
        else:
            print("You shouldn't be here...")
            exitflag = True


# Prints out information in proper formatting
def printinfo(info):
    print()
    if info[1] == 'n':
        print("INFO NOT FOUND: INVALID ENTRY")
    else:
        print(f"City: {info[0]}")
        print(f"Plate Prefix: {info[1]}")
    print()


if __name__ == '__main__':
    pre_text()
    user_text()

