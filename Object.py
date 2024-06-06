class Object:
    """
        author : A
    """
    def __init__(self,name,  lon, lar, h):
        self.name = name
        self.length = lon
        self.width = lar
        self.height = h

    def print(self):
        print(f'name : {self.name} ; lon : {self.length} ; lar : {self.width} ; h : {self.height}')