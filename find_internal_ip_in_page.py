import re

#open text file in read mode
text_file = open("C:\ip_search.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()

# ip contains a list of strings of all IPs
ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', data)

final = []

for s in ip:
	x = s.split(".")
	#print(x)
	rangeten = (int(x[0]) == 10)
	rangeoneseventwo = (int(x[0]) == 172) and (int(x[1]) >= 16) and (int(x[1]) <= 31)
	rangeoneninetwo = (int(x[0]) == 192) and (int(x[1]) == 168)

	if rangeten or rangeoneseventwo or rangeoneninetwo:
		print(x)
	else:
	    if final.count(s) == 0:
		    final.append(s)

print(final)

