

string = input("please enter phelindrom ")
str_len = len(string)
string = string.lower()

while str_len <2 :
    string = input("the string is too short. plz enter a new one ")
    str_len = len(string)
	
i = 0
isphelindrom = true

while i <= (str_len // 2)
    if string[i] == string[str_len-i-1]:
		i = i + 1
	else:
		i = str_len
		isphelindrom = false
		
if isphelindrom :
	print("OK")
else :
	print("NOT")
