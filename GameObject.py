class GameObject():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setPosition(self, x, y):
        self.x = x
        self.y = y

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