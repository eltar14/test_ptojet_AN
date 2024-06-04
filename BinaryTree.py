from Objet import  Objet
class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def add_child(self, side:bool, data):
        if side:
            self.left = BinaryTree(data)
            self.left.parent = self
        else:
            self.right = BinaryTree(data)
            self.right.parent = self

    def get_level(self):
        level = 0
        node = self
        while node.parent is not None:
            node = node.parent
            level += 1
        return level

    def get_parent(self):
        return self.parent


    def is_left_child(self):
        if self.parent is not None:
            return self.parent.left is self
        else:
            return False

    def get_parents_with_side(self):
        parents = []
        node = self
        while node.parent is not None:
            if node.is_left_child():
                parents.append((node.parent.data, 'gauche'))
            else:
                parents.append((node.parent.data, 'droit'))
            node = node.parent
        return parents

    def get_parents_by_level(self):
        parents = [0] * (self.get_level() + 1)
        node = self
        while node.parent is not None:
            if node.is_left_child():
                parents[node.get_level()] = 1
            else:
                parents[node.get_level()] = 0
            node = node.parent
        return parents

    def print_tree(self, level=0):
        if self is None:
            return
        if self.right is not None:  # Ajouter cette ligne
            self.right.print_tree(level+1)
        print(' ' * 4 * level + '->', self.data)
        if self.left is not None:  # Ajouter cette ligne
            self.left.print_tree(level+1)

    def find_max(self):
        max_value = self.data
        max_node = self
        if self.left is not None:
            result = self.left.find_max()
            if result[0] > max_value:
                max_value = result[0]
                max_node = result[1]
        if self.right is not None:
            result = self.right.find_max()
            if result[0] > max_value:
                max_value = result[0]
                max_node = result[1]
        return (max_value, max_node)

    def create_tree(self, objects_list:list, backpack_size:float, util=0, weight = 0):
        if self.get_level() >= len(objects_list) :
            return
        depth = self.get_level()
        if(weight+objects_list[depth].masse <= (backpack_size + 0.0005)):
            self.add_child(True, util+objects_list[depth].utilite) # le DATA
            self.left.create_tree(objects_list, backpack_size, util+objects_list[depth].utilite, weight+objects_list[depth].masse)
        self.add_child(False, util+0)
        self.right.create_tree(objects_list, backpack_size, util, weight)

def print_tree(root, val="data", left="left", right="right"): # source : https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python#:~:text=I%20am%20leaving,your%20node%20definition.
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)



if __name__ == '__main__':
    # Créer le nœud racine
    root = BinaryTree(0)
    import pandas as pd

    data = pd.read_csv("sac2.csv", sep=';', decimal=',')
    data = data.values.tolist()
    objs = []
    for elt in data:
        o = Objet(*elt)
        #o.print()
        objs.append(o)  # liste d'objets



    #print_tree(root)
    #objs[0].print()
    root.create_tree(objs, 0.6)
    vals = root.find_max()[1].get_parents_by_level()[1:]
    print(vals)
    out  = [obj for flag, obj in zip(vals, objs) if flag == 1]

    stats_sac = [0, 0]
    for elt in out:
        stats_sac[0]+= elt.masse
        stats_sac[1]+= elt.utilite

    print(f'Masse : {stats_sac[0]} et utilité : {stats_sac[1]}')
    for elt in out:
        elt.print()
    """
    # Ajouter des nœuds enfants à la racine
    root.add_child(True, 2)
    root.add_child(False, 3)

    # Ajouter des nœuds enfants au nœud gauche de la racine
    root.left.add_child(True, 4)
    root.left.add_child(False, 5)

    # Ajouter des nœuds enfants au nœud droit de la racine
    root.right.add_child(True, 6)
    root.right.add_child(False, 7)

    root.print_tree()
    root.parcours_prefixe()
    #print(root.get_level())
    print("coucou")
    """