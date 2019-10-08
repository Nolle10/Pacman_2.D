class GameObject():
    def __init__(self,x ,y ,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getX(self):
        return self.x

    def getY(self):
        return self.y


    def setPosition(self, x, y):
        self.y = y
        self.x = x


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


    def findObject(self, objCollection: list, direction):


        resultSet = []
        for element in objCollection:
            if direction == "right" or direction == "left":
                if element.y == self.y:
                    resultSet.append(element)

                else:
                    if element.x == self.x:
                        resultSet.append(element)


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


