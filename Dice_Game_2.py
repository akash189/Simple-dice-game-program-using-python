# Dice game
# import random module to genrate random value
import random as rd
d = {}
print("Enter no. of players")
nm = int(input())
print("Enter", nm, "name")
i = 0
# while loop for getting n number of player
while i < nm:
    pl_name = input()
    d[pl_name] = 0
    i = i+1

print(d)
print()
ls1 = list(d.keys())
j = 0
# Looping 5 times
# This loop for playing 5 round
while j < 5:
    r = j+1
    print("======= Round", r, "=======")
    k = 0
    c = []
    while k < nm:
        print()
        print("Your turn : ", ls1[k])
        input("press enter to roll dice")
        a = rd.randint(1, 6)
        print("You got = ", a)
        ls = list(d.values())
        # print(ls)
        cv = ls[k]
        b = cv+a
        d[ls1[k]] = b
        # print(d)
        if a == 6:
            print(ls1[k], "you got one more chance press enter to roll dice")
            input()
            new = rd.randint(1, 6)
            ne = a+new
            b = b+new
            c.append(ne)
            d[ls1[k]] = b
            print("you got", new)
        else:
            c.append(a)
        k = k+1

    print()

    print("Round", r, "score is")
    print()
    l = 0
    while l < nm:
        print(ls1[l], "=", c[l])
        l = l+1
    print()
    j = j+1
# print total score
print("Total score is")
ls = list(d.values())
total = 0
while total < nm:
    print(ls1[total], "=", ls[total])
    total = total+1
# count maximum score
mx = max(ls)
count = ls.count(mx)
ind = ls.index(mx)
print()
# Winning condition
if count > 1:
    ind1 = ls.index(mx, ind+1)
    print(ls1[ind], "and", ls1[ind1], "won")
else:
    print(ls1[ind], "won")
