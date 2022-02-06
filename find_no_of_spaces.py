


Data = ''' THIS IS DATAA




KKK


HELLO'''

#Write a python code to find  out number of spaces in the above data;

l = list(Data)
count=0
for i in l:
	if i==' ':
		count += 1
print(l)
print("No. of spaces = "+str(count))