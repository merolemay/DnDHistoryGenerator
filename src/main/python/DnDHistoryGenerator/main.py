def main():
    from characters.Characters import Character
    from configuration.Configuration import Configuration
    configuration = Configuration()
    configuration.welcome()
    option = input()   
    print("Generating a new history with default configuration")
    configuration.generate_default_configuration()
    ListOfCharacters = configuration.generate_ramdon_party()
    print("The party is composed by:")
    for character in ListOfCharacters:
        print(f'{character.name} the {character.race}')
    




if __name__ == "__main__":
    main()
