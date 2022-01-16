# MO_dummyFighter

Mortal Online 2 Training Dummy Fighter

Fighter that uses varios attacks to look human-like, sequence in which attacks are made can be changed at will so two instances of this macro can attack completly differently

This fighter macro has elements of RNG so it combines charged and fast hits at random pace

The macro does 30 iterations of combat sequence and then sits down to replenish stamina reserves so if you wanna leave it overnight, reserves will be refilled and it will keep on fighting dem dummies
Number of these iterations can be changed by editing value in self.combat_iterations

As the macro works like a auto-clicker the only "safe" time to stop the script is when there is a downtime between sequences or when character is sitting. Terminal is sayin when its waiting, for how long and when it is safe to stop. It is possible to stop anytime but it can be annoying as hell as the macro uses your mouse.

ONLY WORKS ON WINDOWS!
## How to use
- You need a Python 3 installed on your device (https://www.python.org/downloads/)
- After python 3 is on your device youll need pyautogui library (https://pyautogui.readthedocs.io/en/latest/)
- After you have Python 3 installed, install win32 python module so the macro can move the mouse around in the game. pywin32, instalattion command in your terminal is: py -m pip install pywin32
- Then you simply have to open terminal in the folder where the script is located at, have MO2 running and execute the python file, all the instructions and logs will follow in the terminal
- To end the macro press CTRL + C while the terminal in which the script was executed is active. 
- This script will use your mouse so PC will not be usable! Once every attack sequence is done, script is paused for 5 seconds opening a window for you to stop it.
- Its adviced to use this script while your game is borderless or windowed

## How it works
Simply fights the Traning dummy with different kinds of attack to level all your desired skills

## How to setup
- Stand in front of Training dummy with your desired weapon in the hand ready to atack
- self.attack_sequence = ['up', 'up', 'left', 'down', 'right', 'down', 'left', 'down', 'up', 'right'] # Attack sequence in which orders attacks are going to be executed, feel free to change it
- self.sequence_downtime = 5 # set the time in seconds you want as downtime to turn off the bot and the downtime between attack sequences
- self.sitdown_key = ')' # Set what key the sitdown is mapped to
- self.draw_weapon_key = 'x' # Set what key is mapped to draw your weapon
- self.combat_iterations = 30 # set after how many attack sequences you want the character to sitdown and regain stamina reserves
- self.sitdown_timer = 120 # set how long you want your character to sitdown to replenish said reserves