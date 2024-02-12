from cowboy import Cowboy
class Sherif(Cowboy):
    def __init__(self, nom, boissonfavorite="Eau", popularite=0, adjectif="vaillant", brigands_coffres=0):
        super().__init__(nom, boissonfavorite, popularite, adjectif)
        self.__brigands_coffres = brigands_coffres

    def presenter(self):
        print(f"{self.quelEstTonNom()} : Je suis le Shérif {self.quelEstTonNom()}, j'ai coffré {self.__brigands_coffres} brigand(s).")

    def coffrer_brigand(self, brigand):
        print(f"{self.quelEstTonNom()} : Au nom de la loi, je vous arrête, {brigand.quelEstTonNom()}!")
        self.__brigands_coffres += 1

    def rechercher_brigand(self, brigand, recompense):
        nom_brigand = brigand.quelEstTonNom() 
        print(f"{self.quelEstTonNom()} : OYEZ OYEZ BRAVE GENS !! {recompense} $ à qui arrêtera {nom_brigand} mort ou vif !")
