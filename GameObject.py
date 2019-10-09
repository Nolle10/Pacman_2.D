class GameObject:
    def __init__(self):
        pass

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def __intersectsX(self, other):
        if self.x >= other.x and self.x <= other.x + other.width:
            return True
        if self.x + self.width >= other.x and self.x + self.width <= other.x + other.width:
            return True
        return False

    def __intersectsY(self, other):
        if self.y >= other.y and self.y <= other.y + other.height:
            return True
        if self.y + self.height >= other.y and self.y + self.height <= other.y + other.height:
            return True
        return False

    def intersects(self, other):
        if self.__intersectsX(other) and self.__intersectsY(other):
            return True
        return False

    def locateCollisionObj(self, objCollection: list, direction):

        # Check all walls/cheeses to determine, which objects are 'in Pacmans way' potentially.
        resultSet = []
        for element in objCollection:
            if direction == "right" or direction == "left":
                if element.y == self.y:
                    resultSet.append(element)
            else:
                if element.x == self.x:
                    resultSet.append(element)

        # filter through results from list, that may be the object, which Pacman is in risk of colliding with.
        # find the closest element to Pacman, depending on the position and the direction he travels.
        finalResult = GameObject(10000, 10000, 40, 40)
        for element in resultSet:
            if direction == "right":
                if element.x >= self.x and abs(finalResult.x - self.x) > abs(element.x - self.x):
                    finalResult = element
            if direction == "left":
                if element.x <= self.x and abs(finalResult.x - self.x) > abs(element.x - self.x):
                    finalResult = element
            if direction == "down":
                if element.y >= self.y and abs(finalResult.y - self.y) > abs(element.y - self.y):
                    finalResult = element
            if direction == "up":
                if element.y <= self.y and abs(finalResult.y - self.y) > abs(element.y - self.y):
                    finalResult = element

        return finalResult