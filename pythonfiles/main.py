#This is my personal little F1 Manager Simulator, which I'm building to learn more about coding and improve my python
#and json knowledge.

#To play the game you can write commands underneath the ______ Line that always shows up


#All the necessary imports
import math
import json
import time

from math import *
from json import *
from time import *





#load the json files into the code
#here the 
with open("GamescoreDB.json", "r") as databaseforteaminfosfile:
    GamescoreDB = json.load(databaseforteaminfosfile)
    
with open("DriversDB.json", "r") as DriversDBfile:
    DriversDB = json.load(DriversDBfile)






#This Function creates empty space so new content can be added
def makespace():
    i = 0
    while i < 46:
        print()
        i = i +1



#this is the function that resets json data for the team info. uses the global gamestoragenumber variabel
def resetjsongamescore(storagenumber):
    with open("GamescoreDB.json", "r") as databaseforteaminfosfile:
        GamescoreDB = json.load(databaseforteaminfosfile)
    
    #first we need to change the data back to zero
    GamescoreDB["StorageforTeams"][storagenumber]["HasData"] = False
    
    #now we have to overwrite the json data with json.dump()
    with open("GamescoreDB.json", "w") as file:
        json.dump(GamescoreDB, file, indent=4)
        
   
    #goes back to the Choose Screen
    game_choose_screen()
    



#The hub screen that is shown to the user. It uses the global gamestoragenumber variabal to load the right Gamescrore 
#from the json files.
def hub_screen(storagenumber):
    makespace()
    
    #Ascii Art that also includes the variables to load data
    print("                     _______                     _    _       _     ")
    print("                    |__   __|                   | |  | |     | |    ")
    print("                       | | ___  __ _ _ __ ___   | |__| |_   _| |__  ")
    print("                       | |/ _ \/ _` | '_ ` _ \  |  __  | | | | '_ \ ")
    print("                       | |  __/ (_| | | | | | | | |  | | |_| | |_) |")
    print("                       |_|\___|\__,_|_| |_| |_| |_|  |_|\__,_|_.__/ ")
    print("--------------------------------------------------------------------------------------------------")
    print("Welcome to the", GamescoreDB["StorageforTeams"][storagenumber]["Teamname"], "Headquarter")
    print()
    print()
    print()
    print("                    ':.                                    Car          ")
    print("                      []_____                            0=[_]=0        ")
    print("                     /\  HQ  \                             /T\          ")
    print("                 ___/  \__/\__\__                         |(o)|         ")
    print("             ---/\___\ |''''''|__\-- ---                 0=\_/=0        ")
    print("                ||'''| |''||''|''|                        __V__         ")
    print()
    print()
    print()
    print("                  ____[]__                                              ")
    print("                 /\       \                      _____                  ")
    print("                //_\  Dr   \                    |  __ \                 ")
    print("               //___\  iv   \                   | |__) |__ _  ___ __    ")                             
    print("              /______\  er   \                  |  _  // _` |/ __/ _ \  ")
    print("             /_I_II__I\_______\                 | | \ \ (_| | (_|  __/  ")
    print("             I_I|  |___I______I                 |_|  \_\__,_|\___\___|  ")
    print()
    print()
    print()
    print("                                          exit")

    print()
    print()
    print("You can go to a location on the screen by typing the name of it")
    print("---------------------------------------------------------------------------------------------------")
    user_command = str(input())
    
    #we still need to make and then link to the other functions 
    if user_command == "exit":
        game_choose_screen()
    else:
        print("Sry only HQ Car Driver Race or exit are valid commands right now!")
        sleep(4)
        hub_screen(storagenumber)
 



#the screen is for the user to choose one of the three game storages 
def game_choose_screen():
    
    
    #this is a function inside the game_choose_screen function that lets the user choose between playing and deleting
    #after the user  choosed sth we run the necessary function with passing the storage number variable 
    #to select the right storage
    def user_choose():
        print("Type play to load into your Gamescore or type delete to delete the GameScore forever")
        print("If you wanna create a new Gamescore type create. Only works with an empty Gamescore")
        print("__________________________________________________________________________________________")
        
        #looks for the user input
        user_command = str(input())
        if user_command == "play":
            can_be_played = GamescoreDB["StorageforTeams"][storagenumber]["HasData"]
            if can_be_played == True:
                hub_screen(storagenumber)
                
            else:
                print("Sry this is a Gamescore with an empty storage. Type create to create a fresh one")
                sleep(4)
                game_choose_screen()
               
                
                
        elif user_command == "delete":
            resetjsongamescore(storagenumber)
            
            
        elif user_command == "create":
            cant_be_created = GamescoreDB["StorageforTeams"][storagenumber]["HasData"]
            if cant_be_created == True:
                print("Sry there is data inside this Gamescore. Delete it first to create a new game. ")
                sleep(4)
                game_choose_screen()
            else:
                #here we need to link to the function to create the game and also pass the storagenumber with it
                print("This Feature is still in production")
                sleep(1)
                game_choose_screen()
                
                
        else:
            print("Sry thats not a valid command! Only play or delete is a valid command")
            sleep(4)
            user_choose() 
        
    
    

    
    
    #first we have to look if there is already some data in the storages (HasData Atribute in json file type boolean in file databaseforteaminfos.json)
    if GamescoreDB["StorageforTeams"][0]["HasData"] == False: #Here we look into the first storage
        StorageOne = "Empty Space"
    else:
        StorageOne= GamescoreDB["StorageforTeams"][0]["Teamname"]
    
    
    if GamescoreDB["StorageforTeams"][1]["HasData"] == False: #Here we look into the second storage
        StorageTwo = "Empty Space"
    else:
        StorageTwo= GamescoreDB["StorageforTeams"][1]["Teamname"]
    
    
    if GamescoreDB["StorageforTeams"][2]["HasData"] == False: #Here we look into the third storage
        StorageThree = "Empty Space"
    else:
        StorageThree= GamescoreDB["StorageforTeams"][2]["Teamname"]
        
    
    
    
    makespace()
    print("              _____ _                             _____                      ")
    print("             / ____| |                           / ____|                     ")
    print("            | |    | |__   ___   ___  ___  ___  | |  __  __ _ _ __ ___   ___ ")
    print("            | |    | '_ \ / _ \ / _ \/ __|/ _ \ | | |_ |/ _` | '_ ` _ \ / _ \ ")
    print("            | |____| | | | (_) | (_) \__ \  __/ | |__| | (_| | | | | | |  __/")
    print("             \_____|_| |_|\___/ \___/|___/\___|  \_____|\__,_|_| |_| |_|\___|")
    print("--------------------------------------------------------------------------------------------------")
    print("        Choose between 3 game scores. If it has a name your already played with it.")
    print("        If it says Empty Space. There is no game score then")
    print()
    print()
    print()
    print("                          Gamescore 1: ", StorageOne )
    print()
    print("                          Gamescore 2: ", StorageTwo)
    print()
    print("                          Gamescore 3: ", StorageThree)
    print()
    print()
    print("Just type the number of the Gamescore you wanna go on playing or edit. Type exit to leave.")
    print("__________________________________________________________________________________________")
        
    
    #here we get the input for which storage the player chooses and
    #we give the variable storagenumber an int that will be used in the user_choose function
    user_command = str(input())
    if user_command == "exit":
        return 0
    elif user_command == "1":
        storagenumber = 0
        user_choose()
    elif user_command == "2":
        storagenumber = 1
        user_choose()
    elif user_command =="3":
        storagenumber = 2
        user_choose()
    else:
        print("Sry thats not a valid command! Only 1,2 or 3 is a valid command")
        sleep(4)
        game_choose_screen()






#the screen that shows as soon as the game start
def gamestartscreen():
    makespace()
    print("                 _____                            _____                   ")
    print("                |  __ \                           |  __ \                 ")
    print("                | |__) |   __ _    ___    ___     | |  | |   __ _   _   _ ")
    print("                |  _  /   / _` |  / __|  / _ \    | |  | |  / _` | | | | |")
    print("                | | \ \  | (_| | | (__  |  __/    | |__| | | (_| | | |_| |")
    print("                |_|  \_\  \__,_|  \___|  \___|    |_____/   \__,_|  \__, |")
    print("                                                                     __/ |")
    print("                                                                    |___/ ")
    print()
    print()
    print("Hello and Welcome to Race-Day. I hope u have fun while playing and enjoy it.")
    print()
    print("You can resize the Window as you wish. It wont be wider then the two || lines")
    print("|                                                                                        |")
    print("For the line at the bottom go down one more line cause here u gonna write your commands")
    
    #makes some space
    i = 0
    while i < 29:
        print("|")
        i = i+1
    
    #print out what the user can do 
    print("| If you resized your window type start to play the game")
    print("__________________________________________________________________________________________")
    
    
    #looks for the user input
    user_command = str(input())
    if user_command == "start":
        makespace()
        game_choose_screen()
    else:
        print("Sry thats not a valid command! Only start is a valid command right now")
        sleep(4)
        gamestartscreen()
    
    



#starting the programm
gamestartscreen()
