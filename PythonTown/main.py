from dame import Dame
from cowboy import Cowboy
from brigand import Brigand
from barman import Barman
from sherif import Sherif

dame = Dame("Louis")
cowboy = Cowboy("Matéo")
brigand = Brigand("Bernard")
barman = Barman("Florian")
sherif = Sherif("Clément")

recompense = brigand.get_recompense()

print("")
print("Présentation des personnages :")
print("")

dame.presenter()
brigand.presenter()
cowboy.presenter()
barman.presenter()
sherif.presenter()


print("")
print("Debut de l'histoire :")
print("")
print("Il était un fois à Python Town")
print("")

barman.servir(dame)
dame.presentation()
dame.changer_robe("Noire")
dame.se_faire_enlever()
brigand.kidnapper_dame(dame)
sherif.rechercher_brigand(brigand,recompense)
brigand.presentation()
brigand.get_recompense()
cowboy.tirer_sur_brigand(brigand)
cowboy.presentation()
cowboy.liberer_dame(dame)
sherif.coffrer_brigand(brigand)


print("")
print("Fin de l'histoire !")
print("")
