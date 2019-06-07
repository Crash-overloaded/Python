#!/usr/bin/python3


string=input("Enter a string:--")
string_list=[]
new_string_list=[]
new_string=""
# converting string into list of characters
for i in range(0,len(string)):
	string_list.append(string[i])

# checking duplicates in new list
for i in string_list:
	if i not in new_string_list:
		new_string_list.append(i)

# priting output string by joining list characters
print("Output String="+new_string.join(new_string_list))
