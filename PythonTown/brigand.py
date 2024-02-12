import random
from humain import Humain

class Brigand(Humain):
    def __init__(self, nom, boissonfavorite="Tord-boyaux", look="méchant", nb_dames_enlevees=random.randint(1,5), recompense=random.randint(250,700), en_prison=False):
        super().__init__(nom, boissonfavorite)
        self.__look = look
        self.__nb_dames_enlevees = nb_dames_enlevees
        self.__recompense = recompense
        self.__en_prison = en_prison

    def quelEstTonNom(self):
        return f"{self._Humain__nom} le {self.__look}"
    
    def quelEstTaBoissonFavorite(self):
        return self._Humain__boissonfavorite

    def kidnapper_dame(self, dame):
        print(super().quelEstTonNom(), ": Ah ah!", dame.quelEstTonNom(), ", tu es mienne désormais!")
        self.__nb_dames_enlevees += 1

    def se_faire_emprisonner_par_sherif(self, sherif):
        print(self.quelEstTonNom(), ": Damned, je suis fait! ", sherif.quelEstTonNom(), ", tu m’as eu!")
        self.__en_prison = True

    def get_recompense(self):
        return self.__recompense
    
    def presentation(self):
        print(f"{self._Humain__nom} : J'ai l'air {self.__look} et j'ai déjà kidnappé {self.__nb_dames_enlevees} dame(s) !")
        print(f"{self._Humain__nom} : Ma tête est mise à prix {self.__recompense} $.")
