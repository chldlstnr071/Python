#1
x=input("number1 : ")
y=input("number2 : ")
str1=input("word : ")

print(x, y, str1)

#2
x=int(input("integer : "))
y=float(input("real number : "))
str1=input("word : ")
print("%d, %f, %s"%(x, y, str1))

#3
a=int(input("number1 : "))
b=int(input("number2 : "))
print(a%b, a//b, a**b)

#4
str2=input("studentnumber : ")
print(str2.replace(str2[0:4], '2999'))

#5
str3="ABCDEF"
print(':'.join(str3))
print(':'.join(str3).split(':'))
