# CS121LabAct

# CS 121  Lab Activity 3
This is a project by *Group 8 in CS 121: ACP*

# 🐦 Angry Birds
### This team project is derive or inspired by the classic game **Angry Birds.**

# Group Members
| Name | GitHub Username|
|------|----------------|
| Aeron Almira | [ALfish152](https://github.com/ALfish152)|
| Rjay Arazula | [rjay29](https://github.com/rjay29)|
| Aaron Mercado | [Aa-ronMer-cado](https://github.com/Aa-ronMer-cado)
| Sheri Lou Hong | [vixea118](https://github.com/vixea118)

## Features

- **Base Class (`AngryBird`)**:
  - Common attributes: `name`, `size`, `speed`, and `image` (ASCII art).
  - Common methods:
    - `launch()`: Simulates launching the bird.
    - `activate_ability()`: Activates the bird's special ability.
    - `print_image()`: Displays the bird's ASCII art.

- **Bird Types (Derived Classes)**:
  Each bird inherits from the base class and has a unique special ability:
  - **Red Bird**: No special ability.
  - **Blue Bird**: Splits into three smaller birds.
  - **Yellow Bird**: Accelerates with incredible speed.
  - **Black Bird**: Explodes.
  - **White Bird**: Drops an egg.
  - **Green Bird**: Acts as a boomerang.
  - **Big Red Bird**: Causes massive damage on impact.

- **Interactive Console**:
  - Choose a bird to launch by entering a number (1-7).
  - View the bird's ASCII art.
  - Activate the bird's special ability.
  - Option to pick another bird or quit the game.
#

# Code Snippet

```python
birds = {
        '1': RedBird(),
        '2': BlueBird(),
        '3': YellowBird(),
        '4': BlackBird(),
        '5': WhiteBird(),
        '6': GreenBird(),
        '7': BigRedBird()
    }

print("Welcome to Angry Birds!")
while True:
    print("Choose a bird to launch:")
    print("1. Red Bird \n2. Blue Bird\n3. Yellow Bird\n4. Black Bird\n5. White Bird\n6. Green Bird\n7. Big Red Bird")
    choice = input("Enter your bird (1-7) or 'q' to quit: ").strip()
    if choice.lower() == 'q':
        print("Goodbye!")
        break
    if choice not in birds:
        print("Invalid choice. Please Try again.\n")
        continue

    selected_bird = birds[choice]
    selected_bird.print_image()
    print(f"You chose {selected_bird.name}!")
    selected_bird.launch()
    selected_bird.activate_ability()
    
    while True:
        play_again = input("\nPick another bird? (y/n): ").lower().strip()
        
        if play_again == 'n':
            print("Goodbye!")
            exit()
        elif play_again == 'y':
            print("\n============================================================\n")
            break
        else:
            print("Invalid choice. Please try again.")

```


# ASCII Image
```python
class RedBird(AngryBird):
    def __init__(self):
        super().__init__("Red Bird", "medium", "normal", """
              %#+*#                
           %##%%#*+*#              
          %#*****%***              
             ###*********#         
          ##**************++#      
        #%#*****************+=#    
       %##********************++#  
      %###*********************++% 
     #####********@@@%##****##%@@* 
     %####********@@@@@@@@@@@@@@@+#
  %@@%####********#%::-@@-=#%-:=#**
 %@@%%###########*##-....--:...##*#
%@@%%%#####*####***###**+==--*##**#
%  @@%######**********++++===--***%
   %% %#######**+-::::-*++++++===# 
       %######=--::::::::--::::*   
         %##+======---------=*     
            #****++==++**##        
""")
    def activate_ability(self):
        print(f"{self.name} has no special ability!")
```



![Sample Screenshot](image.png)


😓
- Main List
    - SubList
        - Another list

1. Test
