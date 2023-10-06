from characters.Characters import Character
from configuration.Configuration import Configuration
from interaction.Choices import Choices
from history.Automatas import MainHistoryAutomata
from history.Grammar import Grammar
from history.Transductors import TransductorParty
from finals.Finals import Finals

userName = ""
configuration = Configuration()
choices = Choices()

def main():
    askForUserName()
    welcome()
    configurateSesion()
    startPlaying()
   
        
       
def startPlaying():
       while True:
        Grammar().party_description(configuration.ListofCharacters)
        print("")
        print("You and your party are scorting a caravan of goods to a nearby town. You are ambushed by a group of bandits. Do you wish to fight them or hide? (Fight/Hide)")
        eleccion = input()
        while not choices.validateInputRegrex(eleccion):
            eleccion = input()
        if eleccion == "hide" or eleccion == "Hide":
            print(TransductorParty().partyNegativeReaction(eleccion))
            print("You hide the bandits defeat your party and take then to their camp. You follow them and see that they are part of a tribe. Do you wish to approach the tribe or not? (Approach/Not)")
            print("1. Aprroach")
            print("2. Not")
            eleccion = input()
            while not choices.validatedInputNumber(eleccion):
                eleccion = input()
            print("")
        if eleccion == "fight" or eleccion == "Fight":
            print(""+TransductorParty().partyPostiveReaction(eleccion))
            Finals().bad_ending()
            print("")
            print("Would you like to play again? (Y/N)")
            eleccion = input()
            while not choices.validateInputYesorNo(eleccion):
                eleccion = input()
            print("")
            if eleccion == "Y" or eleccion == "y":
                startPlaying()
            else:
                print("Thank you for playing!")
                exit()
        print("You aproach their camp and put your eyes on an entry point. Do you wish to enter stealthly or fighting? (Hide/Fight)")
        eleccion = input()
        while not choices.validateInputRegrex(eleccion):
            eleccion = input()
        if eleccion == "Stealth" or eleccion == "stealth":
            print("You manage to get into their camp without being notice and you manage to free your party, now you can save the caravan people fighting or hide, what you do? (Hide/Fight)")
            eleccion = input()
            while not choices.validateInputRegrex(eleccion):
                eleccion = input()
            if eleccion == "Hide" or eleccion == "hide":
                Finals().neutral_ending()
                print("")
                print("Would you like to play again? (Y/N)")
                eleccion = input()
                while not choices.validateInputYesorNo(eleccion):
                    eleccion = input()
                print("")
                if eleccion == "Y" or eleccion == "y":
                    startPlaying()
                else:
                    print("Thank you for playing!")
                    exit()
            else:
                print("You fight the bandits and manage to save the caravan people, but you are wounded and need to rest")
                Finals().good_ending()
                print("")
                print("Would you like to play again? (Y/N)")
                eleccion = input()
                while not choices.validateInputYesorNo(eleccion):
                    eleccion = input()
                print("")
                if eleccion == "Y" or eleccion == "y":
                    startPlaying()
                else:
                    print("Thank you for playing!")
                    exit()
        else:
            print("You enter the camp fighting and manage to free your party, now you can save the caravan people fighting or hide, what you do? (Hide/Fight)")
            eleccion = input()
            while not choices.validateInputRegrex(eleccion):
                eleccion = input()
            if eleccion == "Hide" or eleccion == "hide":
                print("You manage to hide and escape with your party, but the caravan people are killed by the bandits")
                print("The End")
                print("")
                print("Would you like to play again? (Y/N)")
                eleccion = input()
                while not choices.validateInputYesorNo(eleccion):
                    eleccion = input()
                print("")
                if eleccion == "Y" or eleccion == "y":
                    startPlaying()
                else:
                    print("Thank you for playing!")
                    exit()
            else:
                print("You fight the bandits and manage to save the caravan people, but you are wounded and need to rest")
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
