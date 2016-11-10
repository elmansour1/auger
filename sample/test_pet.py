#
# This file was entirely generated by auger, simply by watching how pet.py was used.
#

from pet import Pet
from unittest.mock import patch
import animal
import pet
import unittest

class PetTest(unittest.TestCase):
  @patch.object(Pet, 'getSpecies')
  def test___str__(self, mock_getSpecies):
    mock_getSpecies.return_value = 'Parrot:32'
    _pet = Pet(species='Parrot',name='Polly')
    self.assertEquals(_pet.__str__(), 'Polly is a Parrot:32')

  def test_createPet(self):
    self.assertIsInstance(pet.createPet(species='Parrot',name='Polly'), Pet)

  def test_getName(self):
    _pet = Pet(species='Parrot',name='Polly')
    self.assertEquals(_pet.getName(), 'Polly')

if __name__ == "__main__":
  unittest.main()

