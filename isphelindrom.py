

string = input("please enter phelindrom ")

string = string.replace(' ','')
str_len = len(string)

while str_len < 2 :
    string = input("the string is too short. plz enter a new one ")
    string = string.replace(' ','')
    str_len = len(string)
	
string = string.lower()
i = 0
isphelindrom = True
endloop = str_len // 2
while i <= str_len // 2 :
    if string[i] == string[str_len-i-1]:
        i = i + 1
    else:
        isphelindrom = False
        i = str_len
		
if isphelindrom :
    print("OK")
else :
    print("NOT")
