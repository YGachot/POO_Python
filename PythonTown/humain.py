from abc import ABC, abstractmethod

class Humain(ABC):  # En héritant de ABC (classe de base abstraite)

    def __init__(self, nom, boissonfavorite="Eau"):
        self.__nom = nom
        self.__boissonfavorite = boissonfavorite

    def presenter(self):
        print(f"{self.__nom} : Bonjour, je suis {self.__nom} et j'aime le {self.__boissonfavorite}.")

    def boire(self):
        print(f"{self.__nom} : Ah! un bon verre de {self.__boissonfavorite}! GLOUPS!")

    @abstractmethod
    def quelEstTaBoissonFavorite(self):  # Méthode abstraite
        pass

    @abstractmethod
    def quelEstTonNom(self):  # Méthode abstraite
        pass
