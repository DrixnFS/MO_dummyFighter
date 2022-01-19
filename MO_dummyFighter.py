import time, pyautogui, random, threading, os
import win32api, win32con
from pynput.keyboard import Key, Listener

class DummyFighter:
    def __init__(self):
        self.attack_sequence = ['up', 'up', 'left', 'down', 'right', 'down', 'left', 'down', 'up', 'right'] # Attack sequence in which orders attacks are going to be executed, feel free to change it
        self.sequence_downtime = 5 # set the time in seconds you want as downtime to turn off the bot and the downtime between attack sequences
        self.sitdown_key = ')' # Set what key the sitdown is mapped to
        self.draw_weapon_key = 'x' # Set what key is mapped to draw your weapon
        self.combat_iterations = 30 # set after how many attack sequences you want the character to sitdown and regain stamina reserves
        self.sitdown_timer = 120 # set how long you want your character to sitdown to replenish said reserves
        self.attack_charge_time = .6 # Set how long it takes to charge the attack, if it varies for the different weapons use the time it takes to fully charge yours
        self.attack_interval = 1 # Set how big of an interval has to be between each attack, can be taken as swing animation timer, if it varies for the different weapons use the time it take to take another swing with yours


        # !!!! DO NOT EDIT ANYTHING UNDER THIS LINE IF YOU DO NOT PERFECTLY KNOW HOW EVERYTHING WORKS, ONLY CHANGE THE VARIABLES ABOVE TO ALTER THE BEHAVIOR !!! #

        self.__screen_x_res = 0
        self.__screen_y_res = 0

        pb = threading.Thread(target=self.__panicButton)
        pb.start()

        print('!--- You have 10 seconds to activate Mortal Online 2 window and have your weapon out ---!')
        time.sleep(10);
        self.startFighting();

    def __panicButton(self):
        def on_press(key):
            if(key == Key.f5):
                print('--Stopping the script based on user input--')
                os._exit(0)

        # Collect events until released
        with Listener(on_press=on_press,) as listener:
            listener.join()

    def startFighting(self):
        self.__getScreenResolution()

        iteration = 1
        print('- Starting to fight the Training Dummy -')
        while iteration <= self.combat_iterations:
            print(f'--Starting combat sequence, iteration {iteration}--')
            for attack in self.attack_sequence:
                self.__doAttack(attack)
                time.sleep(self.attack_interval)
            print(f'!-- Attack sequnce is done, waiting for {self.sequence_downtime} seconds. It is safe to exit the macro with CTRL+C --!')
            time.sleep(self.sequence_downtime)
            iteration += 1
        else:
            self.__doSitdown()
            return False

    def __getScreenResolution(self):
        print('--Getting the screen resolution--');
        self.__screen_x_res = win32api.GetSystemMetrics(0)
        self.__screen_y_res = win32api.GetSystemMetrics(1)

    def __doAttack(self, attack):
        print(f'--Attacking training dummy with {attack} Attack--')
        x_pos = 0
        y_pos = 0
        match attack:
            case 'up':
                y_pos = -1
            case 'down':
                y_pos = 1
            case 'left':
                x_pos = -1
            case 'right':
                x_pos = 1
                
        pyautogui.mouseDown()
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x_pos/self.__screen_x_res*65535), int(y_pos/self.__screen_y_res*65535), 0, 0)
        if(self.__rngChargedHit()):
            time.sleep(self.attack_charge_time)
        pyautogui.mouseUp()

    def __rngChargedHit(self, p=.5):
        return True if random.random() < p else False

    def __doSitdown(self):
        print(f'--sitting down for {self.sitdown_timer}. It is safe to exit the macro with CTRL+C--')
        pyautogui.press(self.sitdown_key)
        time.sleep(self.sitdown_timer)
        pyautogui.press(self.draw_weapon_key)
        time.sleep(1)
        self.startFighting()

DummyFighter()