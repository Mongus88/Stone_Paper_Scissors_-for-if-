import random

choiches = ["kő", "papír", "olló"]
user_score = 0
computer_score = 0

for i1 in range(3):
    user_choice = input("kő, papír vagy olló?")
    if user_choice not in choiches:
        print(f"Hiba: A '{user_choice}' nem választható! A gép kap egy pontot.")
        computer_score += 1
        continue
    computer_choice = random.choice(choiches)
    print(computer_choice)
    if user_choice == computer_choice:
        print ("Döntetlen")
    elif user_choice == "kő" and computer_choice == "olló" or \
         user_choice == "papír" and computer_choice == "kő" or \
         user_choice == "olló" and computer_choice == "papír":
        print ("Nyertél")
        user_score += 1
    else:
        print ("Vesztettél")
        computer_score += 1
print(f"\nEredmény:\nTe {user_score} - Gép {computer_score}")
