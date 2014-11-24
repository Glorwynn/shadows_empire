class Building:

    """
        Class for Buildings
        ===================
        Attributes:
        -----------
            - idBuild: Integer
            - name: String
            - rooms: Dictionary {room: number}
            - price: Integer
            - owner: Character
            - host: Character
    """

    def __init__(self, idBuild, name, price, rooms={}):
        self.idBuild = idBuild
        self.name = name
        self.rooms = rooms
        self.price = price
        self.owner = None
        self.host = None

    def buildRoom(self, room):
        """
            Build a room in Building
            ------------------------
            Add a room in attribute rooms

            OUTPUT: None
        """
        if room in self.rooms:
            self.rooms[room] += 1
        else:
            self.room[room] = 1

    def destroyRoom(self, room):
        """
            Destroy a room
            --------------
            Remove a room from attribute rooms

            OUTPUT: None
        """
        if self.rooms[room] > 1:
            self.rooms[room] -= 1
        else:
            del self.rooms[room]

    def inhabitantMax(self):
        """
            Compute the maximum number of members in the Building
            -----------------------------------------------------
            The number is compute from the number of rooms
            in the building.

            OUTPUT: Integer
        """
        nb = 0
        for room in self.rooms:
            if isinstance(room, Bedroom):
                nb += room.nbBed
        return(nb)

    def sell(self, buyer, seller):
        """
            Sell a building
            ---------------
            Add the gold from buyer to seller, change the owner to buyer
            and add the building in the estates of character

            OUTPUT: None
        """
        if buyer.gold >= self.price:
            buyer.gold -= self.price
            seller.gold += self.price
            buyer.estates += [self]
            self.owner = buyer
            self.host = buyer
        else:
            print("pas l'argent pour acheter ce batiment")


class Room:

    """
        Class for generic room
        ======================
        Attributes:
            - Name: String
    """

    def __init__(self, idRoom, name):
        self.name = name


class Bedroom(Room):

    """
        Class for bedroom
        ======================
        Attributes:
            - Name: String
            - nbBed: Integer
    """

    def __init__(self, idRoom, name, nbBed):
        Room.__init__(self, idRoom, name)
        self.nbBed = nbBed
