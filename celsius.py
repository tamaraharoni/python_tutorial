
is_good_input = True
temp = input("plz enter the temracher ")


ntemp = temp[0:(len(temp)-1)]
if ntemp.isnumeric() :
	numeric_temp = float(ntemp)
else :
	is_good_input = False
	print("the input shuold be numeric")
	
if is_good_input :	
	scale = temp[-1]
	if scale == 'f' or scale == 'F' :
		scale = 'F'
	elif scale == 'c' or scale == 'C':
		scale = 'C'
	else :
		is_good_input = False 
		print("please ad 'c' if it is celsius temp. or 'f', if it is faranhite")

if is_good_input :	
	
	if scale == 'F' :
		cel = numeric_temp * 1.8 +32
	else  :
		cel = (numeric_temp - 32) / 1.8 
	print (temp + " = "+str(cel) + scale)
		

			