from random import randint

print("FOLD AND UNFOLD GAME")
p1 = input("Enter '0' for unfold or '1' for fold: ")
p1 = int(p1)  

c2 = randint(0, 1)
c3 = randint(0, 1)

choices = {0: "unfold", 1: "fold"}
print(f"P1: {choices[p1]}")
print(f"C2: {choices[c2]}")
print(f"C3: {choices[c3]}")

if (p1 == 0 and c2 == 1 and c3 == 1) or (p1 == 1 and c2 == 0 and c3 == 0):
    print("You win")
elif (p1 == 1 and c2 == 0 and c3 == 1) or (p1 == 0 and c2 == 1 and c3 == 0):
    print("C2 win")
elif (p1 == 1 and c2 == 1 and c3 == 0) or (p1 == 0 and c2 == 0 and c3 == 1):
    print("C3 win")
else:
    print("It's a tie")
