import math
class Objet:
    def __init__(self, nom, masse, utilite):
        self.nom = nom
        self.masse = masse
        self.utilite = utilite

    def ratio(self):
        return self.utilite/math.sqrt(self.masse)
    def print(self):
        print(f'{self.nom} ; {self.masse} ; {self.utilite}')
