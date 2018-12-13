
#תרגיל 3.4.2

string = input("pleas enter a sentence ")
length_haf = len(string)//2
print("length of haf sting: ")
print(length_haf)
result = string[0:length_haf].lower() + string[length_haf:].upper()

print(result)
