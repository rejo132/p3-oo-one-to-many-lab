class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"pet_type must be one of {self.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner  # Optional owner parameter
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        """Return a list of pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        """Add a pet to this owner, validating it's a Pet instance."""
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instance of Pet")
        pet.owner = self
    
    def get_sorted_pets(self):
        """Return a sorted list of pets by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)