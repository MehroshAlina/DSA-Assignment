#Q4. Write a program to print the first non-repeated character from a string?

str = "this string is for testing non repeated characters"
str_map = {}

for i in range(len(str)):
    curr_char = str[i]

    if curr_char not in str_map:
        str_map[curr_char] = 0

    str_map[curr_char] += 1

for x in str_map:
    if str_map[x] == 1:
        print("This is the first non-repeated character:",x)
        break

