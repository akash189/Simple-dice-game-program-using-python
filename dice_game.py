# Dice game
# import random module to genrate random value
import random as rd
win = ""
pl = []
print("Enter no. of players you want to play")
nm = int(input())
print("Enter the", nm, "name")
i = 0
# while loop for getting n number of player
while i < nm:
    pn = input()
    pl.append(pn)
    i = i+1
print(pl)
j = 0
# Looping 10 times
# This loop for playing 10 round
while j < 10:
    print("======= Round", j + 1, "=======")
    i = 0
    while i < nm:
        print(pl[i], "your turn")
        input("Press enter to roll dice")
        dic = rd.randint(1, 6)  # genrate random value
        print(pl[i], ":-", dic)
        if dic == 6:
            print("hey,congrats", pl[i], " you got 6 play one more time")
            input("To play press Enter")
            dic1 = rd.randint(1, 6)  # genrate random value
            print(dic1)
            if dic1 == 6:
                win = "win"
                print(pl[i], "won")
            else:
                print("ohh its", dic1, ",Better luck next time\n")
        print()
        i = i + 1

    if win == "win":
        break
    j = j+1
