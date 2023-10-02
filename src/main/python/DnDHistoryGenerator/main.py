from characters.Characters import Character
from configuration.Configuration import Configuration
from interaction.Choices import Choices
from history.Automatas import MainHistoryAutomata
from history.Grammar import Grammar

configuration = Configuration()
choices = Choices()

def main():
    configurateSesion()
    while(True):
        choices.present_choices()
        Grammar().party_description(configuration.ListofCharacters)
        eleccion = choices.validateInputRegrex(input())

        False
        



def configurateSesion():
    option = input()
    if option == "1":
        configuration.generate_default_configuration()
    elif option == "2":
        configuration.generate_custom_configuration()
    elif option == "3":
        configuration.exit()
    else:
        print("Please select a valid option")
        configurateSesion()
 




if __name__ == "__main__":
    main()
