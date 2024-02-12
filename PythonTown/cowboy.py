from humain import Humain

class Cowboy(Humain):
    def __init__(self, nom, boissonfavorite="Whisky", popularite=0, adjectif="Beau Gosse"):
        super().__init__(nom, boissonfavorite)
        self.__popularite = popularite
        self.__adjectif = adjectif
    
    def quelEstTonNom(self):
        return self._Humain__nom
    
    def quelEstTaBoissonFavorite(self):
        return self._Humain__boissonfavorite

    def tirer_sur_brigand(self, brigand):
        print("Le", self.__adjectif, self.quelEstTonNom(), "tire sur", brigand.quelEstTonNom())
        print(self.quelEstTonNom(),": Dans les dents rantanplan !")
        print(self.quelEstTonNom(),": Prend ça !")

    def liberer_dame(self, dame):
        print(self.quelEstTonNom(), ": Soyez libérée,", dame.quelEstTonNom(), "!")
        dame.se_faire_liberer_par_cowboy(self)
        self.__popularite += 1
    
    def presentation(self):
        print(f"{self._Humain__nom} : On dit de moi que je suis {self.__adjectif} et ma popularité est de {self.__popularite}.")