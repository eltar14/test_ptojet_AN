#            /$$                                     /$$$$$$  /$$       /$$                       /$$
#           | $$                                    /$$__  $$| $$      | $$                      | $$
#   /$$$$$$$| $$  /$$$$$$   /$$$$$$$ /$$$$$$$      | $$  \ $$| $$$$$$$ | $$$$$$$  /$$  /$$$$$$  /$$$$$$
#  /$$_____/| $$ |____  $$ /$$_____//$$_____/      | $$  | $$| $$__  $$| $$__  $$|__/ /$$__  $$|_  $$_/
# | $$      | $$  /$$$$$$$|  $$$$$$|  $$$$$$       | $$  | $$| $$  \ $$| $$  \ $$ /$$| $$$$$$$$  | $$
# | $$      | $$ /$$__  $$ \____  $$\____  $$      | $$  | $$| $$  | $$| $$  | $$| $$| $$_____/  | $$ /$$
# |  $$$$$$$| $$|  $$$$$$$ /$$$$$$$//$$$$$$$/      |  $$$$$$/| $$$$$$$/| $$$$$$$/| $$|  $$$$$$$  |  $$$$/
#  \_______/|__/ \_______/|_______/|_______/        \______/ |_______/ |_______/ | $$ \_______/   \___/
#                                                                           /$$  | $$
#                                                                          |  $$$$$$/
#                                                                           \______/

# pour partie 1 seulement

import math
class Objet:
    """
    author : A
    """
    def __init__(self, nom, masse, utilite):
        self.nom = nom
        self.masse = masse
        self.utilite = utilite

    def ratio(self):
        return self.utilite/math.sqrt(self.masse)
    def print(self):
        print(f'{self.nom} ; {self.masse} ; {self.utilite}')
