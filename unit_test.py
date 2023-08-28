import unittest
from Class.player import *
from Class.fire import *
from Class.equipment import *
from game_map import matrix, init_a, init_b
from function import current_position


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player((0, 0))


class TestInit(TestPlayer):
    def test_position(self):
        """
        Test if the position of the player is as expected
        """
        self.assertEqual(current_position(self.player), "A0")

    def test_initial_item(self):
        """
        Test if initial items that a player has are None
        """
        self.assertEqual(self.player.mask, None)
        self.assertEqual(self.player.extinguisher, None)


class TestValidDirection(TestPlayer):
    def test_valid_direction_check(self):
        """
        Test if the check_valid_direction function works as expected
        """
        self.assertFalse(self.player.check_valid_direction(1, "up"))
        self.assertFalse(self.player.check_valid_direction(3, "up"))
        self.assertFalse(self.player.check_valid_direction(4, "down"))
        self.assertFalse(self.player.check_valid_direction(5, "left"))
        self.assertFalse(self.player.check_valid_direction(6, "left"))


class TestValidLook(TestPlayer):
    def test_valid_look(self):
        """
        Test if the look function works as expected
        """
        self.assertFalse(self.player.look("up"))
        self.assertFalse(self.player.look("left"))
        self.assertTrue(self.player.look("right"))
        self.assertTrue(self.player.look("down"))


class TestCollectItem(TestPlayer):
    def test_collect_item(self):
        """
        Test if the look function works as expected
        i.e. if the player cannot collect anything at the current position
        """
        self.assertEqual(self.player.collect(matrix), None)


class TestFire(unittest.TestCase):
    def setUp(self):
        self.fire = Fire((init_a, init_b))


class TestFirePower(TestFire):
    def test_fire_power(self):
        """
        Test if a fire is initialized correctly
        i.e. fire power is greater than or equal to 6
        """
        self.assertTrue(self.fire.power >= 6)


if __name__ == "__main__":
    unittest.main()
