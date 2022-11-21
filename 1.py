def base3_num(num):  
    quo = num/3    
    rem = num%3
    if quo == 0:   
        return ""
    else:
        return base3_num(int(quo)) + str(int(rem))
number = int(input())
print(base3_num(number))