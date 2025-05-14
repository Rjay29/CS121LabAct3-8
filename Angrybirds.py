from abc import ABC, abstractmethod

class AngryBird(ABC):
    def __init__(self, name, size, speed, image):
        self.name = name
        self.size = size
        self.speed = speed
        self.image = image
    
    def launch(self):
        print(f"{self.name} is launched at {self.speed} speed!")
    @abstractmethod
    def activate_ability(self):
        pass
    def print_image(self):
        print(self.image)

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

class BlueBird(AngryBird):
    def __init__(self):
        super().__init__("Blue Bird", "small", "fast", """
          .:-:....                 
        ..#+==+#=...               
       ...=%+====#..               
     .:%+====**===#...             
     .#*==========+#%%%*....       
     ...::#%*+===========#%:..     
       .##++===============#%.     
     ..%*++====+#+..:#***::+#%:..  
     .%*++====+*..  ..:#.....+#..  
    .+#+++====*-...=@+==:.%#+.#+.  
   ..%+++=====*++#*===*+**-+#**%.  
.##.:%+++======#+++*#------=%*#%.  
:%@@#%++++=====+%+-----------:*%...
.%%+:+*+++=======**==*%#+=----::+..
..-@@@%++++========#*==-===#%##..-:
 .*@#..%+++++========*%%#+==%%...  
  -%.. .+%+++++===========*%*.     
  ...  ...-%%*+++++++++#%%=...     
          ....:+##%%#*-.....       
""")
    def activate_ability(self):
        print(f"{self.name} splits into three smaller birds!")

class YellowBird(AngryBird):
    def __init__(self):
        super().__init__("Yellow Bird", "small", "very fast", """
                  @%               
              @@%  @%              
                @@%%%%             
              %%%%%%%%             
               %%%++%%%            
              %%+-::+*-*           
              *=-:::::::*          
             #--:::::::::=         
            *--::::::::::::+       
           +--::::::::::::::=      
         #=--::::::::::::::::-#    
   %%    +--:+######**-::**######  
     %%#=--:::::-.-*=-+===*=.-::+  
%%%%%%%+--::::::::-=++++=====-:::* 
  %%%%+---::::::::::-+++==+----:::+
     +=------:::::::::::::::::::::=
      #+=--------::::::::::::--==*#
""")
    
    def activate_ability(self):
        print(f"{self.name} accelerate with incredible speed!")

class BlackBird(AngryBird):
    def __init__(self):
        super().__init__("Black Bird", "large", "slow", """
    %**#*=-*                       
      #**=--%                      
          %%%#                     
            %%#                    
              %#                   
               %                   
                %                  
            #%%%%%%%####           
        %%%%%%%%%%%%%%%%###        
     %%%###########%%%%%%########* 
   #%%%%%%%**#.+#=#%%%%%%+****#*## 
  %%%%%%%%%###+=-*##+=-----=+#%##  
 %%%%%%%%%%%%#*+************=-:%## 
%%%%%%%%%%%%%%%*++++++=---#%%%%%%##
%%%%%%%%%%%%%%%%%%*+++==#%%%%%%%%##
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##
 %@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%# 
  %@@%%%%%%%%%%%%%%%%%%%%%%%%%%%#  
   #%@@%%%%%%%%%%#**********#%%%   
     %%@@@%%%#***************#     
       *%%%################        
           #####%%%%###            
""")
    
    def activate_ability(self):
        print(f"{self.name} explodes!")

class WhiteBird(AngryBird):
    def __init__(self):
        super().__init__("White Bird", "medium", "normal", """
             +---*  --*            
               ##%%##**            
              ---=%###%            
              -=*##**#*+           
               +=+:=#:..:*=+#      
            *=-:--=-::..::+=-=     
           =-:::.=:...:-....:.-    
          -::::.-....#+-*#..::.:+  
         -::::...-....:=+-::::..:= 
        =::::.:::::::====----:::.: 
 ===*  +::::.::::::..====-----::.:-
*=--=##-::::..::::..-=====---::...=
 ##*#%#=::::........-======---:...-
+--=# =-:::.........-=====----....:
+++   +-::::.........:====-=-.....-
      *-::::......................=
       +-::::....................:=
         =-:::.....::::::::::...-= 
          *=-::---::::::::::::=+   
              *+==========+*       
""")
    
    def activate_ability(self):
        print(f"{self.name} drops an egg!")

class GreenBird(AngryBird):
    def __init__(self):
        super().__init__("Green Bird", "medium", "normal", """
     ```         @@@@@@                       
                @@@@@                        
              @@@@@@@@@@@                    
             @@@@@@@@@@@@                    
              @@@@@@@@                       
        @@@ @@%%####%%%@  @#***+++==+*%@     
        @@@@@#*++++++*##*++===========--=#   
        @@#==+#%*+##*+===================-+@ 
@    @ @@*:...:-###+======================-+@
@@  @@ @*#:...:-#=%#####%#########*****+++=-@
@@@@@@@%+*#=--=#*=#+++++++++++++++++++++++*#@
@@@@@@@#+++******-#+++++++++++++++++++++++#@ 
 @@@@@@*++++++**##****%*****##*****+***#%@   
@@@@@@@#+++**=:........:=***%@               
    @@@@**+-..............-*@                
        @#=-............:=%@                 
          @@%**+=--=++*#@@       
""")
    
    def activate_ability(self):
        print(f"{self.name} turns into a boomerang and comes back!")

class BigRedBird(AngryBird):
    def __init__(self):
        super().__init__("Big Red Bird", "extra large", "very slow", """
            %###*#                 
           #*########%%            
         %#################        
       %#################%##*      
     %####################%%%#*    
    %##########################+*  
   %############################*# 
  %##%###########################**v
  %%%##%%##########################
 @%%%%#############################
@@%%%%########%####%######%########
 @%%%%#######%%####%%@@@@%%########
  %%%%##############*-==-*######## 
   %#############*+==++++=+*#####  
    %%#######*=--------------*#%   
       %###*-----------------+     
           #*++===-----=+#         
""")
    
    def activate_ability(self):
        print(f"{self.name} causes massive damage on impact!")

birds = {
        '1': RedBird(),
        '2': BlueBird(),
        '3': YellowBird(),
        '4': BlackBird(),
        '5': WhiteBird(),
        '6': GreenBird(),
        '7': BigRedBird()
    }
def main():
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
                
if __name__ == "__main__":
    main()
