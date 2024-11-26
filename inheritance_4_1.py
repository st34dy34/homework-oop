# Topic. Inheritance. Part 4 Task 1
class Device:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        
    
class CoffeMachine(Device):
    def __init__(self, brand, model,watercapacity):
        Device.__init__(self,brand, model)
        self.watercapacity = watercapacity
    def make_coffe(self):
        print(f"{self.model} by {self.brand} is making you a coffee! (water: {self.watercapacity})")
    

class Blender(Device):
    def __init__(self, brand, model, vegetable):
        Device.__init__(self,brand, model)
        self.vegetable = vegetable
    def blend_something(self):
        print(f"{self.model} by {self.brand} is now blending {self.vegetable}!")


class MeatGrinder(Device):
    def __init__(self, brand,model,meat):
        Device.__init__(self,brand,model)
        self.meat = meat
    def grind_something(self):
        print(f"{self.model} by {self.brand} is now grinding {self.meat}!")
    
coffemachine = CoffeMachine("Tesla","4.2",100)
blender = Blender("Toyota","bl3nd3r", "carrot")
meatgrinder = MeatGrinder("Skoda","M34T 2.5","pork")

coffemachine.make_coffe()
blender.blend_something()
meatgrinder.grind_something()
