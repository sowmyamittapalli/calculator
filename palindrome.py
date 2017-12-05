s1 = str(raw_input("enter a string: "))
s2 = str()
length = len(s1)
for i in range(0,length):
    s2=s2+(s1[length-1])
    length = length-1
if s1 == s2:
    print ("it is a palindrome")
else:
    print ("It is not a palindrome")






