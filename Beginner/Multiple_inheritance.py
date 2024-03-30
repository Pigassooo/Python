class Father():
    def skills(self):
        print("enjoy gardening")

class Mother():
    def skills(self):
        print('like cooking')


class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print('enjoy sports')


c = Child()
c.skills()
