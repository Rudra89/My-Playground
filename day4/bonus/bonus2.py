user_input = input("Add a new member: ").capitalize().strip()

file = open("day4/bonus/files/members.txt", "r")
members = file.readlines()
file.close()

file = open("day4/bonus/files/members.txt", "w")
members = members.append(user_input + "\n")
file.writelines(members)
file.close()