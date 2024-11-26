class Airplane:
    def __init__(self, name,plane_type, count_passengers, maximum_passengers):
        self.name = name
        self.plane_type = plane_type
        self.count_passengers = count_passengers
        self.maximum_passengers = maximum_passengers
    # ==
    def __eq__(self,other):
         return self.plane_type == other.plane_type
    # +
    def __add__(self,other):
        self.count_passengers += 1
        print("přičítám jednoho")
        return self
    # -
    def __sub__(self,other):
        self.count_passengers -= 1
        print("odečítám jednoho")
        return self
    # <
    def __lt__(self, other):
        return self.maximum_passengers < other.maximum_passengers
    # <=
    def __le__(self, other):
        return self.maximum_passengers <= other.maximum_passengers
    # >
    def __gt__(self, other):
        return self.maximum_passengers > other.maximum_passengers
    # >=
    def __ge__(self, other):
        return self.maximum_passengers >= other.maximum_passengers
        
    def __str__(self):
        return f"{self.name}:{self.plane_type}, cetujici:{self.count_passengers}, maximum: {self.maximum_passengers}"
        
        
plane1 = Airplane("letadlo 1","Skoda",5,30)
plane2 = Airplane("letadlo 2","Skoda",3,12)
plane3 = Airplane("letadlo 3","Volvo",8,35)
print(f"{plane1}\n{plane2}\n{plane3}")
print("--Začínáme!--")


# Rovná se
if plane1 == plane2:
    print(f"{plane1.name} a {plane2.name} mají stejný typ!")
else:
    print(f"{plane1.name} a {plane2.name} nemají stejný typ....")
    
if plane2 == plane3:
    print(f"{plane2.name} a {plane3.name} mají stejný typ!")
else:
    print(f"{plane2.name} a {plane3.name} nemají stejný typ....")
    
# přičítání / odečítání
plane1 += plane1 
plane2 -= plane2  

# větší / měnší
if plane1 < plane2:
    print(f"{plane1.name} má větší kapacitu než {plane2.name}") 
else:
    print(f"{plane1.name} má menší kapacitu než {plane2.name}") 


print("----konečný stav----")
print(f"{plane1}\n{plane2}\n{plane3}")



    
    
    
    
        