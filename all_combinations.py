# Python3 program to find all combination of numbers
# from a given string of digits

def printCombinations(input, index, output, outLength):
	
	# no more digits left in input string
	if (len(input) == index):
		# print output string & return
		output[outLength] = '\0'
		print(*output[:outLength], sep = "")
		return
	# place current digit in input string
	output[outLength] = input[index]
	
	# separate next digit with a space
	#output[outLength + 1] = ' '
	printCombinations(input, index + 1,
					output, outLength + 1)
	
	# if next digit exists make a
	# call without including space
	if(len(input) != (index + 1)):
		printCombinations(input, index + 1,
						output, outLength + 1)

# Driver code
input = "1214"
output = [0]*100

# initialize output with empty string
output[0] = '\0'

printCombinations(input, 0, output, 0)
