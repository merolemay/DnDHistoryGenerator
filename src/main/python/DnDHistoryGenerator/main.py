from characters.Characters import Character
from configuration.Configuration import Configuration


def main():
    configuration = Configuration()
    configuration.welcome()
    option = input()
    if option == "1":
        configuration.generate_default_configuration()
    elif option == "2":
        configuration.generate_custom_configuration()
    elif option == "3":
        configuration.exit()
    else:
        print("Please select a valid option")
        main()
 
    




if __name__ == "__main__":
    main()
