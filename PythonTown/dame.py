from humain import Humain

class Dame(Humain):
    def __init__(self, nom, boissonfavorite="Lait", couleur_robe="Rouge", etat="libre"):
        super().__init__(nom, boissonfavorite)
        self.__couleur_robe = couleur_robe
        self.__etat = etat

    def quelEstTonNom(self):
        return f"Miss {self._Humain__nom}"
    
    def quelEstTaBoissonFavorite(self):
        return self._Humain__boissonfavorite
    
    def presentation(self):
        print(self.quelEstTonNom(), ": Ma robe est de couleur", self.__couleur_robe,".")

    def se_faire_enlever(self):
        print(self.quelEstTonNom(), ": AAAh! Au secours, je me suis faite enlever!")

    def se_faire_liberer_par_cowboy(self, cowboy):
        print(self.quelEstTonNom(), ": Merci,", cowboy.quelEstTonNom(), "pour m'avoir libérée!")

    def changer_robe(self, nouvelle_couleur):
        print(self.quelEstTonNom(), ": Regardez ma nouvelle robe", nouvelle_couleur, "!")
        self.__couleur_robe = nouvelle_couleur

    def get_couleur_robe(self):
        return self.__couleur_robe

    def get_etat(self):
        return self.__etat

    def changer_etat(self, nouvel_etat):
        self.__etat = nouvel_etat
