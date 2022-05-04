def second_smallest_finder(num):
    min_val = 100
    sec_min = 100

    for i in range(len(num)):
        if num[i] < min_val:
            min_val = num[i]

    for i in range(len(num)):
        if (num[i] < sec_min) and (num[i] != min_val):
            sec_min = num[i]
    
    return(sec_min)

def second_largest_finder(num):
    max_val = -100
    sec_max = -100

    for i in range(len(num)):
        if num[i] > max_val:
            max_val = num[i]
    
    for i in range(len(num)):
        if (num[i] > sec_max) and (num[i] != max_val):
            sec_max = num[i]

    return(sec_max)

num = [1,2,-8,-2,0]
print("(a) Second Smallest Number :", second_smallest_finder(num))
print("(b) Second largest Number  :", second_largest_finder(num))
