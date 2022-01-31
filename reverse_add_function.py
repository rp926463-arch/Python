#The reverse and add function starts with a number, reverses its digits, and adds the reverse to the original. 
#If the sum is not a palindrome, repeat this procedure until it does. 

#Write a program that takes number and gives the resulting palindrome (if one exists). 
#If it took more than 1,000 iterations (additions) or yield a palindrome that is greater than 4,294,967,295, 
#assume that no palindrome exist for the given number.

'''
Input : 195
Output : 9339

Input : 265
Output: 45254

Input : 196
Output : No palindrome exist 
'''

#Python Program to implement reverse and add function

# Iterative function to reverse digits of num
def reversDigits(num):
	rev_num=0
	while (num > 0):
		rev_num = rev_num*10 + num%10
		num = num/10
	return rev_num

# Function to check whether the number is palindrome or not
def isPalindrome(num, rev_num):
	return (rev_num == num)

# Reverse and Add Function
def ReverseandAdd(num):
	rev_num = 0
	while (num <= 4294967295):
		# Reversing the digits of the number
		rev_num = reversDigits(num)

		# Adding the reversed number with the original
		num = num + rev_num

		# Checking whether the number is palindrome or not
		if(isPalindrome(num, rev_num)):
			print num
			break
		else:
			if (num > 4294967295):
				print "No palindrome exist"

# Driver Code
ReverseandAdd(195)
ReverseandAdd(265)
