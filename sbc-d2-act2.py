from random import randint

# User input
p1 = input("Enter '0' for unfold or '1' for fold: ")
p1 = int(p1)  # Convert user input to integer

# Random choices for C2 and C3
c2 = randint(0, 1)
c3 = randint(0, 1)

# Display the choices
choices = {0: "unfold", 1: "fold"}
print(f"P1: {choices[p1]}")
print(f"C2: {choices[c2]}")
print(f"C3: {choices[c3]}")

# Determine the winner
if (p1 == 0 and c2 == 1 and c3 == 1) or (p1 == 1 and c2 == 0 and c3 == 0):
    print("You win")
elif (p1 == 1 and c2 == 0 and c3 == 1) or (p1 == 0 and c2 == 1 and c3 == 0):
    print("C2 wins")
elif (p1 == 1 and c2 == 1 and c3 == 0) or (p1 == 0 and c2 == 0 and c3 == 1):
    print("C3 wins")
else:
    print("It's a tie")
