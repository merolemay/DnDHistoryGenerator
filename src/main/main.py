from characters.Characters import Character
from configuration.Configuration import Configuration
from interaction.Choices import Choices
from history.Automatas import MainHistoryAutomata
from history.Grammar import Grammar

userName = ""
configuration = Configuration()
choices = Choices()

def main():
    askForUserName()
    welcome()
    configurateSesion()
    Grammar().party_description(configuration.ListofCharacters)
    print("Your character, a Lawful Good adventurer, finds themselves at the edge of an enchanted forest. The forest is known to be a dangerous place, but there are rumors that a group of innocent villagers has been captured by malevolent creatures deep within")
    print("Do you wish to enter the forest? (Y/N)")
    eleccion = input()
    while not choices.validateInputYesorNo(eleccion):
        eleccion = input()
    print("")
    print("You enter the forest and find a fork in the road. One path leads to a cave, the other to a small hut. Which do you choose? (Cave/Hut)")
    eleccion = input()
    while not choices.validateInputRegrex(eleccion):
        eleccion = input()
    print("")
    print("You enter the cave and find a group of goblins. They are holding the villagers captive. Do you wish to fight them? (Y/N)")
    eleccion = input()
    while not choices.validateInputYesorNo(eleccion):
        eleccion = input()
    print("")
    print("You fight the goblins and free the villagers. Do you wish to escort them out of the forest? (Y/N)")
    eleccion = input()
    while not choices.validateInputYesorNo(eleccion):
        eleccion = input()
    print("")
    print("You escort the villagers out of the forest and they thank you for your help. You have completed your quest.")
    print("")
    print("The End")
    print("")
    print("Would you like to play again? (Y/N)")
    eleccion = input()
    while not choices.validateInputYesorNo(eleccion):
        eleccion = input()
    print("")
    if eleccion == "Y" or eleccion == "y":
        main()
    else:
        print("Thank you for playing!")
        exit()
    
   
        
    
        
        
       

    
def welcome():
    print("Welcome to the D&D History Generator" + " " + userName)
    print("Please select an option:")
    print("1. Start Playing")
    print("2. Exit")
    
def configurateSesion():
    option = input()
    if option == "1":
        configuration.generate_default_configuration()
    elif option == "2":
        configuration.exit()
    else:
        print("Please select a valid option")
        configurateSesion()
 

def setUserName(name):
    global userName
    userName = name

def askForUserName():
    print("How would you like to be call for this sesion?")
    name = input()
    setUserName(name)
    return name

def getUserName():
    return userName

if __name__ == "__main__":
    main()
