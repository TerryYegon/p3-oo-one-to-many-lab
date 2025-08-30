# lib/owner_pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        if owner:
            self.set_owner(owner)
        Pet.all.append(self)

    def set_owner(self, owner):
        from .owner_pet import Owner
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner class")
        self.owner = owner
        if self not in owner.pets_list:
            owner.add_pet(self)


class Owner:
    all = []

    def __init__(self, name):
        self.name = name
        self.pets_list = []
        Owner.all.append(self)

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        pet.owner = self
        if pet not in self.pets_list:
            self.pets_list.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)
