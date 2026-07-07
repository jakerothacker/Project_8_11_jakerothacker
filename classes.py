
class HasFur:
    pass

class CanFly:
    pass

class CanSwim:
    pass

class HasScales:
    pass 

class Answer:
    def __init__(self,name,*traits):
        self.name = name
        self.traits = traits

class Animal(Answer):
    def __init__(self,name,*traits):
        super().__init__(name, *traits)
        


fish = Animal("Fish", [CanSwim(), HasScales()])

print(isinstance(fish,Answer))





