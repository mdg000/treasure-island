print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to LOST Island.")
print("Your mission is to not get LOST.") 

choice1 = input("\nYou find yourself on the edge of the beach. You notice the brush is too thick to head inland, do you want to explore to the left or right?\n\n Choose: (right / left)  ").lower()


if choice1 == "left":
  print("\nYou walk along the beach until you find a path into the interior of the island\n")
  
  choice2 = input("\nYou find a river that blocks your path. It looks dangerous, do you attempt to cross, or should you take a break and rest?\n\n Choose: (cross / rest). ").lower()

  if choice2 == "rest":

    choice3 = input("\nYou take a rest and manage to find a way to cross the river safely after noticing the current has subsided. Not far from the other side of the river, you see a hatch, an empty cabin, and a dimly lit cave. Where should you go?\n\n Choose: (hatch / cabin / cave) ").lower()

    if choice3 == "hatch":

      print("\nYou carefully approach the hatch and open it. You see a ladder and climb down it. Inside is quite nice, and you meet a fellow named Desmond. He teaches you how to push a button at a desk and tells you he has some errands to run and will be back later. Congradulations, You Won!\n")

    elif choice3 == "cave":

      print("\nAs soon as you step inside the cave, the smoke monster appears and kills you. Game Over.\n")

    elif choice3 == "cabin":

      print("\nYou enter the cabin and make yourself at home. You lay down on a couch and pass out. Hours later, you are murdered in your sleep by The Man in Black. Game over.\n")
    
    else:
      print("\nYou died from indecision. Game over.\n")

  else:
    print("\nYou were gobbled up by man-eating turtles. Game over.\n")

else:
  print("\nYou were captured by the others. Game Over.\n")


