
#תרגיל 3.4.2

string = input("pleas enter a sentence ")
start_letter = string[0:1]
if len(string) > 1 :
	newstring = start_letter + string[1:].replace(start_letter,'e')
else :
	newstring = start_letter

print(newstring)