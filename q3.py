def common_member_check(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                print("True")
                break
        if l1[i] == l2[j]:
            break

print("1st set:")
l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]
common_member_check(l1,l2)

print("2nd set:")
l3 = [1,2,3,4,5]
l4 = [6,7,8,9]
common_member_check(l3,l4)
