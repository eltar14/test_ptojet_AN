#   /$$$$$$              /$$ /$$                                             /$$                                               /$$                 /$$ /$$
#  /$$__  $$            | $$|__/                                            |__/                                              | $$                | $$|__/
# |__/  \ $$        /$$$$$$$ /$$ /$$$$$$/$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$ /$$  /$$$$$$  /$$$$$$$   /$$$$$$$        /$$$$$$$| $$   /$$ /$$   /$$| $$ /$$ /$$$$$$$   /$$$$$$
#    /$$$$$/       /$$__  $$| $$| $$_  $$_  $$ /$$__  $$| $$__  $$ /$$_____/| $$ /$$__  $$| $$__  $$ /$$_____/       /$$_____/| $$  /$$/| $$  | $$| $$| $$| $$__  $$ /$$__  $$
#   |___  $$      | $$  | $$| $$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$|  $$$$$$ | $$| $$  \ $$| $$  \ $$|  $$$$$$       |  $$$$$$ | $$$$$$/ | $$  | $$| $$| $$| $$  \ $$| $$$$$$$$
#  /$$  \ $$      | $$  | $$| $$| $$ | $$ | $$| $$_____/| $$  | $$ \____  $$| $$| $$  | $$| $$  | $$ \____  $$       \____  $$| $$_  $$ | $$  | $$| $$| $$| $$  | $$| $$_____/
# |  $$$$$$/      |  $$$$$$$| $$| $$ | $$ | $$|  $$$$$$$| $$  | $$ /$$$$$$$/| $$|  $$$$$$/| $$  | $$ /$$$$$$$/       /$$$$$$$/| $$ \  $$|  $$$$$$$| $$| $$| $$  | $$|  $$$$$$$
#  \______/        \_______/|__/|__/ |__/ |__/ \_______/|__/  |__/|_______/ |__/ \______/ |__/  |__/|_______/       |_______/ |__/  \__/ \____  $$|__/|__/|__/  |__/ \_______/
#                                                                                                                                        /$$  | $$
#                                                                                                                                       |  $$$$$$/
#                                                                                                                                        \______/


"""
Fonctions en cours de verification, potentiellement des chevauchements entre les objets
"""
class Item:
    """
    author : N
    """
    def __init__(self, name, longueur, largeur, hauteur):
        self.name = name
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur

    def __str__(self):
        # représentation en chaîne de caracteres de l'objet pour l'affichage
        return f"Item(name={self.name}, longueur={self.longueur}, largeur={self.largeur}, hauteur={self.hauteur})"

class Wagon:
    """
    author : N
    """
    def __init__(self, longueur, largeur, hauteur):
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
        self.skyline = [(0, 0, 0)]  # liste des points de la skyline initialisée à l'origine
        self.placed_items = [] # liste des objets placés contient leur position et leur dimensions dans un tuple

    def __str__(self):
        # représentation en chaine de caracteres du wagon
        items_str = ", ".join([str(item) for item in self.placed_items])
        return f"Wagon(longueur={self.longueur}, largeur={self.largeur}, hauteur={self.hauteur}, placed_items=[{items_str}])"

    def can_place(self, item, position):
        """
        author : N
        :param item:
        :param position:
        :return:
        """
        x, y, z = position
        # Verifie si l'item dépasse les dimensions du wagon
        if x + item.longueur > self.longueur or y + item.largeur > self.largeur or z + item.hauteur > self.hauteur:
            return False

        # vérifie les chevauchements avec les items déjà placés
        for px, py, pz, pl, pw, ph in self.placed_items:
            if not (x + item.longueur <= px or x >= px + pl or
                    y + item.largeur <= py or y >= py + pw or
                    z + item.hauteur <= pz or z >= pz + ph):
                return False
        return True

    def place_item(self, item, position):
        """
        author : N
        :param item:
        :param position:
        :return:
        """
        #ajout de l'objet et maj de la skyline
        self.placed_items.append((position[0], position[1], position[2], item.longueur, item.largeur, item.hauteur))
        self.update_skyline(position, item)

    def update_skyline(self, position, item):
        """
        author : N
        :param position:
        :param item:
        :return:
        """
        # ajout de l'objet qui vient d'être rangé dans le wagon a la skyline
        new_points = [
            (position[0] + item.longueur, position[1], position[2]),
            (position[0], position[1] + item.largeur, position[2]),
            (position[0], position[1], position[2] + item.hauteur)
        ]

        # ajoute les nouveaux points à la skyline existante
        self.skyline.extend(new_points)
        # trie et élimine les doublons dans la skyline
        self.skyline = sorted(set(self.skyline), key=lambda p: (p[2], p[1], p[0]))

def skyline_algorithm(items, wagon_longueur, wagon_largeur, wagon_hauteur):
    """
    author : N
    :param items:
    :param wagon_longueur:
    :param wagon_largeur:
    :param wagon_hauteur:
    :return:
    """
    wagons = []
    current_wagon = Wagon(wagon_longueur, wagon_largeur, wagon_hauteur)
    wagons.append(current_wagon)

    for item in items:
        placed = False
        for wagon in wagons:
            for position in wagon.skyline:
                if wagon.can_place(item, position):
                    wagon.place_item(item, position)
                    placed = True
                    break
            if placed:
                break
        if not placed: # créer un nouveau wagon quand plus de place dans le wagon actuel
            new_wagon = Wagon(wagon_longueur, wagon_largeur, wagon_hauteur)
            new_wagon.place_item(item, (0, 0, 0))
            wagons.append(new_wagon)

    return wagons

donnees = [
    ["Tubes acier", 10, 1, 0.5],
    ["Tubes acier", 9, 2, 0.7],
    ["Tubes acier", 7.5, 1.2, 0.4],
    ["Acide chlorhydrique", 1, 1, 1],
    ["Godet pelleteuse", 2, 2, 1],
    ["Rails", 11, 1, 0.2],
    ["Tubes PVC", 3, 2, 0.6],
    ["Echaffaudage", 3, 1.3, 1.8],
    ["Verre", 3, 2.1, 0.6],
    ["Ciment", 4, 1, 0.5],
    ["Bois vrac", 5, 0.8, 1],
    ["Troncs chênes", 6, 1.9, 1],
    ["Troncs hêtres", 7, 1.6, 1.5],
    ["Pompe à chaleur", 5, 1.1, 2.3],
    ["Cuivre", 6, 2, 1.4],
    ["Zinc", 5, 0.8, 0.8],
    ["Papier", 4, 1.6, 0.6],
    ["Carton", 7, 1, 1.3],
    ["Verre blanc vrac", 9, 0.9, 2.2],
    ["Verre brun vrac", 3, 1.6, 0.9],
    ["Briques rouges", 5, 1.1, 2.4],
    ["Pièces métalliques", 6, 1.6, 1.4],
    ["Pièces métalliques", 7, 0.9, 1.2],
    ["Pièces métalliques", 3, 1.6, 1.9],
    ["Ardoises", 1, 1.8, 1],
    ["Tuiles", 2, 1.2, 2.3],
    ["Vitraux", 4, 0.7, 1.2],
    ["Carrelage", 6, 1.2, 2.5],
    ["Tôles", 7, 0.6, 1.5],
    ["Tôles", 9, 1.7, 1],
    ["Tôles", 6, 1.9, 1.6],
    ["Tôles", 3, 2.2, 2.2],
    ["Tôles", 3, 0.5, 2.2],
    ["Mobilier urbain", 4, 0.7, 1.9],
    ["Lin", 5, 2.2, 0.7],
    ["Textiles à recycler", 6, 1.3, 2.5],
    ["Aluminium", 6, 1.3, 1.2],
    ["Batteries automobile", 7, 1.4, 2.5],
    ["Quincaillerie", 6, 1.1, 1],
    ["Treuil", 7, 0.9, 1.3],
    ["Treuil", 8, 0.5, 0.5],
    ["Acier", 8, 0.9, 1.7],
    ["Laine de bois", 8, 0.9, 1.8],
    ["Ouate de cellulose", 5, 1.7, 1.2],
    ["Chanvre isolation", 2.2, 1.6, 1.1],
    ["Moteur électrique", 4.2, 1.5, 0.8],
    ["Semi conducteurs", 3.7, 0.9, 1.4],
    ["Semi conducteurs", 5.6, 0.5, 1.4],
    ["Semi conducteurs", 4.9, 0.9, 2.5],
    ["Semi conducteurs", 8.7, 1.3, 1.3],
    ["Semi conducteurs", 6.1, 2.2, 2.3],
    ["Semi conducteurs", 3.3, 1.8, 2.3],
    ["Semi conducteurs", 2.6, 1.6, 2.3],
    ["Semi conducteurs", 2.9, 1.6, 2],
    ["Aluminium", 2, 1.1, 0.6],
    ["Aluminium", 3, 0.6, 1.2],
    ["Aluminium", 6, 1, 0.8],
    ["Aluminium", 5, 1.3, 0.6],
    ["Aluminium", 4, 2.1, 2.1],
    ["Aluminium", 6, 1.5, 1.9],
    ["Aluminium", 4, 0.8, 2.1],
    ["Aluminium", 2, 2, 2.3],
    ["Aluminium", 4, 1, 1.1],
    ["Aluminium", 6, 1.8, 1.1],
    ["Lithium", 6, 1.9, 0.9],
    ["Lithium", 3, 2, 2.2],
    ["Lithium", 4, 1.5, 0.9],
    ["Lithium", 4, 2.1, 2.5],
    ["Lithium", 2, 1.2, 1.5],
    ["Lithium", 6, 1.3, 2],
    ["Lithium", 2, 0.8, 1.1],
    ["Contreplaqué", 4, 1.4, 2],
    ["Contreplaqué", 5, 0.6, 0.5],
    ["Contreplaqué", 5, 0.6, 1.8],
    ["Contreplaqué", 4, 0.7, 1.4],
    ["Contreplaqué", 6, 0.5, 0.7],
    ["Contreplaqué", 3, 1.5, 1.8],
    ["Contreplaqué", 3, 1.4, 2],
    ["Contreplaqué", 3, 2, 2.3],
    ["Contreplaqué", 5, 1.5, 0.7],
    ["Contreplaqué", 5, 2.2, 0.5],
    ["Contreplaqué", 6, 1.2, 1.2],
    ["Poutre", 5, 0.8, 0.7],
    ["Poutre", 3, 0.5, 1.9],
    ["Poutre", 5, 1.4, 0.7],
    ["Poutre", 6, 0.7, 0.7],
    ["Poutre", 6, 1.2, 2]
]

item_objects = [Item(*item) for item in donnees]

wagons = skyline_algorithm(item_objects, 11.583, 2.294, 2.569)
print(f"Nombre total de wagons nécessaires : {len(wagons)}")
for i, wagon in enumerate(wagons):
    print(f"Wagon {i + 1} contient les articles suivants :")
    for item in wagon.placed_items:
        print(f" - {item}")
