def format_number_left(num):
    num_str = str(num)
    num_len = len(num_str)
    res = ""
    
    if num_len % 3 == 0:
        comma_pos = 0
    elif num_len % 3 == 1:
        comma_pos = 1
    elif num_len % 3 == 2:
        comma_pos = 2
    
    for i in range(num_len):
        if i % 3 == comma_pos and comma_pos != 0:
            res += ","
        res += num_str[i]
        
    return res

        
print(format_number_left(32918678))
print(format_number_left(123))
print(format_number_left(3299))
print(format_number_left(32918))
print(format_number_left(975883))
print(format_number_left(97588903))
print(format_number_left(975889038))


# 123            -> 0 len = 3
# 123,456        -> 0 len = 6
# 1,234,567      -> 1
# 12,345,678     -> 2
# 123,456,789    -> 0 len = 9