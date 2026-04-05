"""
Kevin Nelson
Module 01 Lab Assignment
 
This program asks for the number of friends then the name of each friend before outputing information of said friends
"""

friend_names = []
friend_acronym = ""
friend_amount = int(input("Enter the number of friends to input: "))

for i in range(friend_amount):
    friend_name = input(f"Enter the name of friend {i + 1}: ")
    friend_names.append(friend_name)

print(f"Your best friend is named {friend_names[0]}")
print(f"Your least-best friends name is {friend_names[friend_amount - 1]}")

for i in range(len(friend_names)):
    name = friend_names[i]
    letter = str.upper(name[0])

    friend_acronym += letter

print(f"The acronym of your friend's names is {friend_acronym}")