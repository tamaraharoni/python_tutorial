
isphilendrom = True
string = input('please enter a string')
string = string.replace(' ','')
last_index = len(string)+1
print(last_index)

revers = string[-1:-(last_index):-1]
print(revers)
isphilendrom = string == revers
if isphilendrom :
	print("ok")
else :
	print("not")
	