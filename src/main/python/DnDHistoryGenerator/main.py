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
    while(True):
        Grammar().party_description(configuration.ListofCharacters)
        choices.present_choices()
        eleccion = choices.validateInputRegrex(input())
        if eleccion:
            MainHistoryAutomata().run(configuration.ListofCharacters, eleccion)
        else:
            choices.present_choices()
            Grammar().party_description(configuration.ListofCharacters)
            eleccion = choices.validateInputRegrex(input())
            MainHistoryAutomata().run(configuration.ListofCharacters, eleccion)


    
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
