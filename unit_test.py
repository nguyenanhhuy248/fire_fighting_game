import unittest
from Class.player import *
from Class.fire import *
from Class.equipment import *
from game_map import matrix, init_a, init_b
from function import current_position


class TestPlayer (unittest.TestCase):
    def setUp(self):
        self.player= Player((0,0))

class TestInit (TestPlayer):
    def test_position(self):
        self.assertEqual(current_position(self.player), 'A0')
    
    def test_initial_item(self):
        self.assertEqual(self.player.mask, None)
        self.assertEqual(self.player.extinguisher, None)

class TestValidDirection (TestPlayer):
    def test_valid_direction_check(self):
        self.assertFalse(self.player.check_valid_direction(1,'up')) 
        self.assertFalse(self.player.check_valid_direction(3,'up'))
        self.assertFalse(self.player.check_valid_direction(4,'down'))
        self.assertFalse(self.player.check_valid_direction(5,'left'))
        self.assertFalse(self.player.check_valid_direction(6,'left'))

class TestValidLook (TestPlayer):
    def test_valid_look(self):
        self.assertFalse(self.player.look('up'))
        self.assertFalse(self.player.look('left'))
        self.assertTrue(self.player.look('right'))
        self.assertTrue(self.player.look('down'))

class TestCollectItem (TestPlayer):
    def test_collect_item(self):
        self.assertEqual(self.player.collect(matrix), None)

class TestFire (unittest.TestCase):
    def setUp(self):
        self.fire = Fire((init_a, init_b))

class TestFirePower (TestFire):
    def test_fire_power(self):
        self.assertTrue(self.fire.power >= 6)

if __name__ == '__main__':
    unittest.main()
