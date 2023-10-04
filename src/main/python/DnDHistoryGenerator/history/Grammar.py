from nltk import CFG
from nltk.parse.generate import generate
from configuration.Configuration import Configuration


class Grammar:
    #Un CFG que da una descipcion de los miembros del party usando sus nombres, clase y liniamiento
    #Ejemplo: "El party esta compuesto por un guerrero de liniamiento caotico bueno llamado Juan, un clerigo de liniamiento legal bueno llamado Pedro y un ladron de liniamiento caotico neutral llamado Diego"
    # @param party: Lista de objetos Character
    # @return: String
    grammar = CFG.fromstring("""
        S -> NP VP
        NP -> Det N | Det N PP | 'I'
        VP -> V NP | VP PP
        PP -> P NP
        Det -> 'the' | 'a' | 'an' | 'my'
        N -> 'group' | 'character' | 'cleric' | 'thief' | 'warrior' | 'wizard' | 'paladin' | 'ranger' | 'druid' | 'bard' | 'monk' | 'sorcerer' | 'barbarian' | 'rogue' | 'fighter' | 'monk' | 'druid' | 'ranger' | 'wizard' | 'paladin' | 'cleric' | 'bard' | 'sorcerer' | 'barbarian' | 'rogue' | 'fighter'
        V -> 'is' | 'are'
        P -> 'of' | 'in'
    """
    )

    def party_description(self, party):
        for sentence in generate(self.grammar, n=1):
            print(' '.join(sentence))
            print(self.generate_description(party))
    
    def generate_description(self, party):
        description = ""
        for character in party:
            description += "\n" + "a " + character.race + " of " + character.alignment + " alignment named " + character.name + ", "
        return description[:-2] + "."
