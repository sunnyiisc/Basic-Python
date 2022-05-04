#Part (a)
print("(a)\n")
tuplex_a = (4, 6, 2, 8, 3, 1)
new_ele = int(input("Enter the new Number to add into the tuple :"))
tuplex_new = tuplex_a + (new_ele,)
print("New Tuple :", tuplex_new)

#Part (b)
print("\n(b)\n")
tuplex_b = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
string = ""
for i in range(len(tuplex_b)):
    string += tuplex_b[i]
print("The String of the Tuple", tuplex_b, "is :", string, "\nData type is", type(string))

#Part (c)
print("\n(c)\n")
tuplex_c = (2, 4, 5, 6, 2, 3, 4, 4, 7)
di = {}

for ele in tuplex_c:
    count_ele = tuplex_c.count(ele)
    if count_ele > 1:
        di[ele] = count_ele

print("For the tuple", tuplex_c, ":")
for i, j in di.items():
    print("The repeating element is", i,", which is repeating", j, "times")

#Part (d)
print("\n(d)\n")
tuplex_d = ((2, "w"),(3, "r"))
dictnry = {}
for i in range(len(tuplex_d)):
    dictnry[ tuplex_d[i][0] ] = tuplex_d[i][1]
print("Dictionary from Tuple is \n", dictnry)
