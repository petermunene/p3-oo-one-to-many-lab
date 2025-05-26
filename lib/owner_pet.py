class Pet:
    all=[]
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner=None):
        if pet_type in Pet.PET_TYPES:
            self.pet_type=pet_type
            self.name=name
            self.owner=owner
            Pet.all.append(self)
        else:
            raise Exception
 
    pass

class Owner:
    def __init__(self, name):
        self.name=name
    def pets(self):
        pets=[pet for pet in Pet.all if pet.owner==self]
        return pets
    def add_pet(self, pet):
        if  isinstance (pet,Pet):
            pet.owner=self
        else:
            raise Exception
    def get_sorted_pets(self):
        pets = [pet for pet in Pet.all if pet.owner == self]
        return sorted(pets, key=lambda pet: pet.name)
    pass