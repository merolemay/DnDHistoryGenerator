from nltk import CFG
from nltk.parse.generate import generate
from configuration.Configuration import Configuration


class Grammar:

    #Un CFG que da una descipcion de los miembros del party usando sus nombres, clase y liniamiento
    #Ejemplo: "El party esta compuesto por un guerrero de liniamiento caotico bueno llamado Juan, un clerigo de liniamiento legal bueno llamado Pedro y un ladron de liniamiento caotico neutral llamado Diego"
    # @param party: Lista de objetos Character
    # @return: String

    """
    
    def describe_party(self):
        for character in self.ListofCharacters:
            print(f'{character.name} the {character.race} which is {character.alignment}')
    """
    def party_description(self, party):
        grammar = CFG.fromstring("""
            S -> NP VP
            NP -> Det N
            VP -> V NP | V NP PP
            PP -> P NP
            Det -> 'el' | 'un'
            N -> 'guerrero' | 'clerigo' | 'ladron' | 'mago'
            V -> 'es'
            P -> 'de'
            """)
        
        for sentence in generate(grammar, n=1):
            print(' '.join(sentence))
                
    