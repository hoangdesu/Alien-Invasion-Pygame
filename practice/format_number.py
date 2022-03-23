def format_numer(num):
    # ??
    # return the number in the type of string with commas
    num_str = str(num)
    result = ""
    ctr = 1
    for i in range(len(num_str) - 1, -1, -1):
        result = num_str[i] + result
        
        if ctr % 3 == 0 and i != 0:
            result = "," + result
        ctr += 1
        
    return result
    
# 1234567
# result += num_str[i]
# => result = result + num_str[i]

numA = 12346789231321
print(format_numer(numA)) # -> "1,234"

numA = 1234
print(format_numer(numA)) # -> "1,234"

numA = 123231321
print(format_numer(numA)) # -> "1,234"

numA = 123461
print(format_numer(numA)) # -> "1,234"


numA = 82768237682764827
print(format_numer(numA)) # -> "1,234"



numA = 1233428934923847239874
print(format_numer(numA)) # -> "1,234"


# numB = 98765432
# print(format_numer(numB)) -> "98,765,432"


# 98,723,984,729,384,792,387

# "brian".
# +


# numA = 123
# res = "," + str(numA)
# print(res)

# 123456789 -> [123, 456, 789]
# split()
# join()