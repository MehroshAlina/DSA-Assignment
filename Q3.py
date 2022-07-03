#Q3. Write a program to check if two strings are a rotation of each other?

str1 = "HELLO"
str2 = "LOHEL"

if len(str1) != len(str2):
    print("str2 is not a rotation of str1")
else:
    str1 = str1 + str1
    if str2 in str1:
        print("str2 is a rotation of str1")
    else:
        print("str2 is not a rotation of str1")
