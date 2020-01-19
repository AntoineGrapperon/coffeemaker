import unittest

import coffeemaker.pendulum as _pendulum

class TestPendulum(unittest.TestCase):

    def test_init(self):
        horloge = _pendulum.Pendulum()
        self.assertEqual(horloge.dummy_test(), 1)


if __name__ == '__main__':
    unittest.main()
