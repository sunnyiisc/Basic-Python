num = [1,2,-8,-2,0]

min_val = 100
sec_min = 100
max_val = -100
sec_max = -100

for i in num:
    if i > max_val:
        sec_max = max_val
        max_val = i
    elif i > sec_max and max_val != i:
        sec_max = i
    
    if i < min_val:
        sec_min = min_val
        min_val = i
    elif i < sec_min and min_val != i:
        sec_min = i

print("(a) Second Smallest Number :", sec_min)
print("(b) Second largest Number  :", sec_max)
