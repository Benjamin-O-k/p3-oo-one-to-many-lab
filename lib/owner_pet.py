class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name,pet_type,owner = None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a pet type")
        self.pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if isinstance(owner,Owner):
            self._owner = owner
        else:
            raise Exception("Invalid Owner")

    # @property
    # def is_pet_type(self):
    #     return self.pet_type in Pet.PET_TYPES

    # @is_pet_type.setter
    # def is_pet_type(self):
    #     if self.pet_type in Pet.PET_TYPES:
    #         return self.pet_type
    #     else:
    #         raise Exception(f"{self.pet_type} is not a pet type")

class Owner:
    def __init__(self,name) -> None:
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Invalid pet")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

