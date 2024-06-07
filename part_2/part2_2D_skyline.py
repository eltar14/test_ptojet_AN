#   /$$$$$$              /$$ /$$                                             /$$                                               /$$                 /$$ /$$
#  /$$__  $$            | $$|__/                                            |__/                                              | $$                | $$|__/
# |__/  \ $$        /$$$$$$$ /$$ /$$$$$$/$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$ /$$  /$$$$$$  /$$$$$$$   /$$$$$$$        /$$$$$$$| $$   /$$ /$$   /$$| $$ /$$ /$$$$$$$   /$$$$$$
#   /$$$$$$/       /$$__  $$| $$| $$_  $$_  $$ /$$__  $$| $$__  $$ /$$_____/| $$ /$$__  $$| $$__  $$ /$$_____/       /$$_____/| $$  /$$/| $$  | $$| $$| $$| $$__  $$ /$$__  $$
#  /$$____/       | $$  | $$| $$| $$ \ $$ \ $$| $$$$$$$$| $$  \ $$|  $$$$$$ | $$| $$  \ $$| $$  \ $$|  $$$$$$       |  $$$$$$ | $$$$$$/ | $$  | $$| $$| $$| $$  \ $$| $$$$$$$$
# | $$            | $$  | $$| $$| $$ | $$ | $$| $$_____/| $$  | $$ \____  $$| $$| $$  | $$| $$  | $$ \____  $$       \____  $$| $$_  $$ | $$  | $$| $$| $$| $$  | $$| $$_____/
# | $$$$$$$$      |  $$$$$$$| $$| $$ | $$ | $$|  $$$$$$$| $$  | $$ /$$$$$$$/| $$|  $$$$$$/| $$  | $$ /$$$$$$$/       /$$$$$$$/| $$ \  $$|  $$$$$$$| $$| $$| $$  | $$|  $$$$$$$
# |________/       \_______/|__/|__/ |__/ |__/ \_______/|__/  |__/|_______/ |__/ \______/ |__/  |__/|_______/       |_______/ |__/  \__/ \____  $$|__/|__/|__/  |__/ \_______/
#                                                                                                                                        /$$  | $$
#                                                                                                                                       |  $$$$$$/
#                                                                                                                                        \______/

class Wagon:
    """
    author : N
    """
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

        self.placed_items = []
        self.skyline = [(0, 0)]  # liste des points de la skyline

    def __str__(self):
        return f"Wagon(longueur={self.longueur}, largeur={self.largeur}, placed_items={self.placed_items})"



class Item:
    """
    author : N
    """
    def __init__(self, name, longueur, largeur):
        self.name = name
        self.longueur = longueur
        self.largeur = largeur

    def __str__(self):
        return f"Item(name={self.name}, longueur={self.longueur}, largeur={self.largeur})"


def can_place(item, position, wagon):
    """
    author : N
    :param item:
    :param position:
    :param wagon:
    :return:
    """
    x, y = position
    # verifie si on peut placer l'objet à la position dans le wagon
    if x + item.longueur > wagon.longueur or y + item.largeur > wagon.largeur:
        return False

    for placed_item in wagon.placed_items:
        # verifie si il n'y à pas une collision entre l'item qu'on veut placer et un item déjà placé dans le wagon # si ne passe pas dedans return false
        if not (x + item.longueur <= placed_item[0] or x >= placed_item[0] + placed_item[2] or
                y + item.largeur <= placed_item[1] or y >= placed_item[1] + placed_item[3]):
            return False
    return True

def update_skyline(skyline, position, item):
    """
    author : N
    :param skyline:
    :param position:
    :param item:
    :return:
    """
    new_points = []
    x, y = position
    # ajout dans la skyline de l'item placé
    new_points.append((x + item.longueur, y))
    new_points.append((x, y + item.largeur))

    skyline.extend(new_points)
    skyline = sorted(set(skyline), key=lambda p: (p[0], p[1]))  # trie et elimine les doublons
    return skyline

def place_items(items, wagon_longueur, wagon_largeur):
    """
    author : N
    :param items:
    :param wagon_longueur:
    :param wagon_largeur:
    :return:
    """
    wagons = []
    current_wagon = Wagon(wagon_longueur, wagon_largeur)
    wagons.append(current_wagon)

    for item in items:
        placed = False
        best_position = None
        min_largeur = float('inf')

        # cherche une position dans les wagons
        for wagon in wagons:
            for position in wagon.skyline:
                if can_place(item, position, wagon):
                    x, y = position
                    if y < min_largeur:
                        best_position = position
                        min_largeur = y
                        current_wagon = wagon  # mettre a jour le wagon courant

            if best_position:
                break  # s'arrete quand on trouve une position

        # si on trouve une position on place l'objet
        if best_position:
            # ajout de la marchandise dans le wagon courant et et sur la skyline
            current_wagon.placed_items.append((best_position[0], best_position[1], item.longueur, item.largeur))
            current_wagon.skyline = update_skyline(current_wagon.skyline, best_position, item)
            placed = True

        # si on ne peut pas placer on créer un nouveau wagon
        if not placed:
            new_wagon = Wagon(wagon_longueur, wagon_largeur)
            new_wagon.placed_items.append((0, 0, item.longueur, item.largeur))
            new_wagon.skyline = update_skyline([(0, 0)], (0, 0), item)
            wagons.append(new_wagon)

    return wagons


donnees = [
    ["Tubes acier", 10, 1],
    ["Tubes acier", 9, 2],
    ["Tubes acier", 7.5, 1.2],
    ["Acide chlorhydrique", 1, 1],
    ["Godet pelleteuse", 2, 2],
    ["Rails", 11, 1],
    ["Tubes PVC", 3, 2],
    ["Echaffaudage", 3, 1.3],
    ["Verre", 3, 2.1],
    ["Ciment", 4, 1],
    ["Bois vrac", 5, 0.8],
    ["Troncs chênes", 6, 1.9],
    ["Troncs hêtres", 7, 1.6],
    ["Pompe à chaleur", 5, 1.1],
    ["Cuivre", 6, 2],
    ["Zinc", 5, 0.8],
    ["Papier", 4, 1.6],
    ["Carton", 7, 1],
    ["Verre blanc vrac", 9, 0.9],
    ["Verre brun vrac", 3, 1.6],
    ["Briques rouges", 5, 1.1],
    ["Pièces métalliques", 6, 1.6],
    ["Pièces métalliques", 7, 0.9],
    ["Pièces métalliques", 3, 1.6],
    ["Ardoises", 1, 1.8],
    ["Tuiles", 2, 1.2],
    ["Vitraux", 4, 0.7],
    ["Carrelage", 6, 1.2],
    ["Tôles", 7, 0.6],
    ["Tôles", 9, 1.7],
    ["Tôles", 6, 1.9],
    ["Tôles", 3, 2.2],
    ["Tôles", 3, 0.5],
    ["Mobilier urbain", 4, 0.7],
    ["Lin", 5, 2.2],
    ["Textiles à recycler", 6, 1.3],
    ["Aluminium", 6, 1.3],
    ["Batteries automobile", 7, 1.4],
    ["Quincaillerie", 6, 1.1],
    ["Treuil", 7, 0.9],
    ["Treuil", 8, 0.5],
    ["Acier", 8, 0.9],
    ["Laine de bois", 8, 0.9],
    ["Ouate de cellulose", 5, 1.7],
    ["Chanvre isolation", 2.2, 1.6],
    ["Moteur électrique", 4.2, 1.5],
    ["Semi conducteurs", 3.7, 0.9],
    ["Semi conducteurs", 5.6, 0.5],
    ["Semi conducteurs", 4.9, 0.9],
    ["Semi conducteurs", 8.7, 1.3],
    ["Semi conducteurs", 6.1, 2.2],
    ["Semi conducteurs", 3.3, 1.8],
    ["Semi conducteurs", 2.6, 1.6],
    ["Semi conducteurs", 2.9, 1.6],
    ["Aluminium", 2, 1.1],
    ["Aluminium", 3, 0.6],
    ["Aluminium", 6, 1],
    ["Aluminium", 5, 1.3],
    ["Aluminium", 4, 2.1],
    ["Aluminium", 6, 1.5],
    ["Aluminium", 4, 0.8],
    ["Aluminium", 2, 2],
    ["Aluminium", 4, 1],
    ["Aluminium", 6, 1.8],
    ["Lithium", 6, 1.9],
    ["Lithium", 3, 2],
    ["Lithium", 4, 1.5],
    ["Lithium", 4, 2.1],
    ["Lithium", 2, 1.2],
    ["Lithium", 6, 1.3],
    ["Lithium", 2, 0.8],
    ["Contreplaqué", 4, 1.4],
    ["Contreplaqué", 5, 0.6],
    ["Contreplaqué", 5, 0.6],
    ["Contreplaqué", 4, 0.7],
    ["Contreplaqué", 6, 0.5],
    ["Contreplaqué", 3, 1.5],
    ["Contreplaqué", 3, 1.4],
    ["Contreplaqué", 3, 2],
    ["Contreplaqué", 5, 1.5],
    ["Contreplaqué", 5, 2.2],
    ["Contreplaqué", 6, 1.2],
    ["Poutre", 5, 0.8],
    ["Poutre", 3, 0.5],
    ["Poutre", 5, 1.4],
    ["Poutre", 6, 0.7],
    ["Poutre", 6, 1.2],
    ["Poutre", 3, 1.7],
    ["Poutre", 5, 1.6],
    ["Pneus", 3, 1.3],
    ["Pneus", 4, 1.5],
    ["Pneus", 3, 1.5],
    ["Pneus", 3, 0.6],
    ["Pneus", 5, 1.8],
    ["Pneus", 3, 1.8],
    ["Pneus", 4, 1.7],
    ["Pneus", 4, 1.5],
    ["Pneus", 2, 2.1],
    ["Pneus", 2, 0.7],
    ["Pneus", 6, 1.2]
]


item_objects = []
for item in donnees:
    name, longueur, largeur = item[:3]
    item_object = Item(name, longueur, largeur)
    item_objects.append(item_object)
    # créer une liste d'objet item a partir des données


wagons = place_items(item_objects, 11.583, 2.294)
print(f"Nombre total de wagons nécessaires : {len(wagons)}")
for i, wagon in enumerate(wagons):
    print(f"Wagon {i+1} contient les articles suivants : {wagon.placed_items}")


