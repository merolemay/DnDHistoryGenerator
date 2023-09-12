def main():
    from src.main.python.DnDHistoryGenerator.Configuration import configuration
    from src.main.python.DnDHistoryGenerator.History import automatas,transductors,grammar
    from src.main.python.DnDHistoryGenerator.Interaction import choices
    from src.main.python.DnDHistoryGenerator.utils import validations

    while True:
        try:
            print("Welcome to the D&D History Generator")
            print("Please select an option:")
            print("1. Generate a new history")
            print("2. Generate a new history with a custom configuration")
            print("3. Exit")
            option = int(input("Option: "))
            if option == 1:
                configuration.generate_default_configuration()
                configuration.load_configuration()
                automatas.generate_automatas()
                transductors.generate_transductors()
                grammar.generate_grammar()
                choices.generate_choices()
                print("History generated successfully")
            elif option == 2:
                configuration.generate_custom_configuration()
                configuration.load_configuration()
                automatas.generate_automatas()
                transductors.generate_transductors()
                grammar.generate_grammar()
                choices.generate_choices()
                print("History generated successfully")
            elif option == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")
        except Exception as e:
            print("An error has occurred: " + str(e))
            print("Please try again")
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
