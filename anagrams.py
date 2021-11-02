
#Find the No. of anagrams in the string[starting index of anagrams]

str1 = "abcdecdbacb"
str2 = "cab"
s2 = set(str2)
l=0
index=[]
while l<len(str1)-2:
        i=l
        s1 = set(str1[i:3+i])
        if s1==s2:
            index.append(i)
        l = l+1

print(index)
