
class HasFur:
    pass

class CanFly:
    pass

class CanSwim:
    pass

class HasScales:
    pass 

class Answer:
    def __init__(self,name):
        self.name = name
        self.traits = {}
    def add_trait(self, trait_name, trait_class):
        self.traits[trait_name] = trait_class
    def remove_trait(self, trait_name):
        self.traits.pop(trait_name, None)

    def check_trait(self, trait_class):
        if trait_class in self.traits:
            return True
        else:
            return False
    

class Animal(Answer):
    def __init__(self,name):
        super().__init__(name)
        


fish = Animal("Fish")
fish.add_trait("can_swim", CanSwim)
fish.add_trait("has_scales",HasScales)

print(isinstance(fish,Answer))
print(fish.check_trait("can_swim"))
