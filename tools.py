import pandas as pd
from Object import Object
def xlsx_to_object_list(path:str):
    """
    author : A
    :param path:
    :return:
    """
    data = pd.read_excel(path)
    data = data.values.tolist()
    objs = []
    for elt in data:
        o = Object(*elt[1:])
        objs.append(o)  # liste d'objets
    return objs