import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_child_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(6), 50)

    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(25), 150)

    def test_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(69), 100)

    def test_invalid_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "invalid")


if __name__ == '__main__':
    unittest.main()