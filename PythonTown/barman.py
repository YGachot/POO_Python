from humain import Humain

class Barman(Humain):
    def __init__(self, nom, nom_bar=None, boissonfavorite = "Vin"):
        super().__init__(nom, boissonfavorite)
        self.__nom_bar = nom_bar if nom_bar else f"Chez {nom}"

    def quelEstTaBoissonFavorite(self):
        return self._Humain__boissonfavorite

    def quelEstTonNom(self):
        return self._Humain__nom    

    def presenter(self):
        print(f"{self._Humain__nom} : Je travaille au bar {self.__nom_bar}. Coco.")

    def parler(self, phrase):
        print(f"{self._Humain__nom} : {phrase}. Coco.")

    def servir(self, personne):
        print(f"{self._Humain__nom} sert un verre de {personne._Humain__boissonfavorite} à {personne.quelEstTonNom()}.")