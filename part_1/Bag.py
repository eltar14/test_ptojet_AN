#            /$$                                    /$$$$$$$
#           | $$                                   | $$__  $$
#   /$$$$$$$| $$  /$$$$$$   /$$$$$$$ /$$$$$$$      | $$  \ $$  /$$$$$$   /$$$$$$
#  /$$_____/| $$ |____  $$ /$$_____//$$_____/      | $$$$$$$  |____  $$ /$$__  $$
# | $$      | $$  /$$$$$$$|  $$$$$$|  $$$$$$       | $$__  $$  /$$$$$$$| $$  \ $$
# | $$      | $$ /$$__  $$ \____  $$\____  $$      | $$  \ $$ /$$__  $$| $$  | $$
# |  $$$$$$$| $$|  $$$$$$$ /$$$$$$$//$$$$$$$/      | $$$$$$$/|  $$$$$$$|  $$$$$$$
#  \_______/|__/ \_______/|_______/|_______/       |_______/  \_______/ \____  $$
#                                                                       /$$  \ $$
#                                                                      |  $$$$$$/
#                                                                       \______/

from Objet import Objet
class Bag:
    """
    author : A
    """
    def __init__(self):
        self.content = [] # contient des Objets
        self.weight = 0
        self.score = 0

    def add(self, obj:Objet):
        self.content.append(obj)
        self.weight += obj.masse
        self.score += obj.utilite

    def print(self):
        print(f'Contenu du sac de masse: {self.weight} et d\'utilite {self.score}')
        for elt in self.content:
            #self.content[i].print()#f'{obj.nom} ; {obj.masse} ; {obj.utilite}'
            elt.print()#f'{obj.nom} ; {obj.masse} ; {obj.utilite}'



    def get_mass(self):
        sum = 0
        for o in self.content:
            sum += o.masse
        return sum
