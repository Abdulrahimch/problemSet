# gain = [-5,1,5,0,-7]

# new_list = [0,-5,-4,]
# l: list
def find_highest_altitude(l):
    l.insert(0, 0)
    for i in range(1, len(l) - 1):
        l[i+1] = l[i] + l[i+1]
    print(l)
    return max(l)


l1 = [-5, 1, 5, 0, -7]
l2 = [-4, -3, -2, -1, 4, 3, 2]

print('the hiest_altitude for l1 is: : ', find_highest_altitude(l1))
print('the hiest_altitude for l2 is: : ', find_highest_altitude(l2))
