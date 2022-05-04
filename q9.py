#Part (a)

def max_num(n):
    max_n = -100
    
    for elm in n:
        if elm > max_n:
            max_n = elm
    return(max_n)

#Part (b)

def sum_list(n):
    sum_n = 0
    
    for elm in n:
        sum_n += elm
    return(sum_n)

#Part (b)

def mul_list(n):
    mul_n = 1
    
    for elm in n:
        mul_n *= elm
    return(mul_n)


inp_list=[]
no_elm = int(input("Enter the length of the list : "))
for i in range(no_elm):
    num = int(input("Enter number " + str(i+1) + ' : '))
    inp_list.append(num)

print("\n(a)\n")
print("Max value among", inp_list, " is", max_num(inp_list))

print("\n(b)\n")
print("Sum of values of", inp_list, " is", sum_list(inp_list))

print("\n(c)\n")
print("Product of values of", inp_list, " is", mul_list(inp_list))
