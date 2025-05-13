# Angry Birds Simulation 🐦 

*A Python console-based program inspired by the classic Angry Birds*

## Group Information
**Course:** CS 121: ACP  
**Group 8**  
**Group Members:**
| Name | GitHub |
|------|----------------|
| Aeron Almira | [ALfish152](https://github.com/ALfish152)|
| Rjay Arazula | [rjay29](https://github.com/rjay29)|
| Aaron Mercado | [Aa-ronMer-cado](https://github.com/Aa-ronMer-cado)
| Sheri Lou Hong | [vixea118](https://github.com/vixea118)

## 🎯 About the Project
This program simulates the Angry Birds game in a text-based console environment. Players can select different bird types, each with unique abilities, and see their ASCII art representations along with special ability descriptions.

## ✨ Key Features
- **7 Unique Bird Types** with special abilities
- **Interactive Console Menu** for bird selection
- **ASCII Art Visuals** for each bird
- **Object-Oriented Design** with inheritance
- **Special Ability System** for each bird type

## 🐦 Bird Types
1. **Red Bird** - Standard bird with no special ability
2. **Blue Bird** - Splits into three smaller birds
3. **Yellow Bird** - Accelerates with incredible speed
4. **Black Bird** - Explodes on impact
5. **White Bird** - Drops an explosive egg
6. **Green Bird** - Boomerang effect
7. **Big Red Bird** - Causes massive damage

## 🚀 How to Run
1. Ensure you have Python 3.x installed
2. Clone/download the repository
3. Run the main Python file:
   ```bash
   python angry_birds.py
4. Follow the on-screen instructions:
    - Enter a number (1-7) to select a bird
    - View the bird's ASCII art
    - See its special ability in action
    - Choose to play again or quit


# 📊Class Diagram
![UML DIAGRAM](https://github.com/user-attachments/assets/7eb3bdf6-ba22-45b9-a227-a3dfbc2d1350)


## 📋 Code Structure
```python
# Base class
class AngryBird:
    # Common attributes and methods
    ...

# Derived classes (one per bird type)
class RedBird(AngryBird):
    ...

class BlueBird(AngryBird):
    ...
```
## 🖼️ Sample Output

```python
Welcome to Angry Birds!
Choose a bird to launch:
1. Red Bird
2. Blue Bird
3. Yellow Bird
4. Black Bird
5. White Bird
6. Green Bird
7. Big Red Bird

Enter your bird (1-7) or 'q' to quit: 2

[ASCII art of Blue Bird]
You chose Blue Bird!
Blue Bird launched!
Blue Bird splits into three smaller birds!

Pick another bird? (y/n):
```
# 🙏 Acknowledgements
- Inspired by the original Angry Birds game by Rovio Entertainment
- ASCII art sourced from various online creators
- Thanks to our CS 121 instructor for guidance
