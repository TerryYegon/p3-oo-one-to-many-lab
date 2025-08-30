# lib/testing/test_owner_pet.py

import pytest
from lib.owner_pet import Pet, Owner

def test_owner_pet_relationship():
    owner1 = Owner("Alice")
    owner2 = Owner("Bob")

    pet1 = Pet("Fido", "dog", owner1)
    pet2 = Pet("Whiskers", "cat", owner1)
    pet3 = Pet("Rex", "dog", owner2)

    # Test owner's pets
    assert owner1.pets() == [pet1, pet2]
    assert owner2.pets() == [pet3]

    # Test adding pet later
    pet4 = Pet("Nemo", "exotic")
    owner2.add_pet(pet4)
    assert pet4.owner == owner2
    assert pet4 in owner2.pets()

    # Test get_sorted_pets
    sorted_pets = owner1.get_sorted_pets()
    assert sorted_pets == sorted([pet1, pet2], key=lambda p: p.name)
