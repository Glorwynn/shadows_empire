class Building:

    """docstring for ClassName"""

    def __init__(self, idBuild, name, price, rooms={}):
        self.idBuild = idBuild
        self.name = name
        self.rooms = rooms
        self.price = price
        self.owner = None
        self.host = None

    def buildRoom(self, room):
        if room in self.rooms:
            self.rooms[room] += 1
        else:
            self.room[room] = 1

    def destroyRoom(self, room):
        if self.rooms[room] > 1:
            self.rooms[room] -= 1
        else:
            del self.rooms[room]

    def inhabitantMax(self):
        nb = 0
        for room in self.rooms:
            if isinstance(room, Bedroom):
                nb += room.nbBed
        return(nb)

    def sale(self, buyer, seller):
        if buyer.gold >= self.price:
            buyer.gold -= self.price
            seller.gold += self.price
            buyer.properties += [self]
            self.owner = buyer
            self.host = buyer
        else:
            print("pas l'argent pour acheter ce batiment")


class Room:

    """docstring for Room"""

    def __init__(self, idRoom, name):
        self.name = name


class Bedroom(Room):

    """docstring for Bedroom"""

    def __init__(self, idRoom, name, nbBed):
        Room.__init__(self, idRoom, name)
        self.nbBed = nbBed
