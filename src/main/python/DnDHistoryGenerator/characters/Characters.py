import pandas as pd

class Character:
      name = ""
      race = ""
      alignment = ""

      def generate_character(self):
            charratersdf = pd.read_csv("data/characters.csv")
            self.name = charratersdf.sample().iloc[0]["name"]
            self.race = charratersdf.sample().iloc[0]["race"]
            self.alignment = charratersdf.sample().iloc[0]["alignment"]


