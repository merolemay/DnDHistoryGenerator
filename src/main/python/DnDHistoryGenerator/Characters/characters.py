import pandas as pd

class Character:
      name = ""
      race = ""

      def generate_character(self):
            charratersdf = pd.read_csv("src/main/resources/characters.csv")
            self.name = charratersdf.sample().iloc[0]["name"]
            self.race = charratersdf.sample().iloc[0]["race"]
        

