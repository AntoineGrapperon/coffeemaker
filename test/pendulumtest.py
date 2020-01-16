import unittest

import coffeemaker.pendulum as _pendulum

class TestPendulum(unittest.TestCase):

    def test_init(self):
        self.assertEqual(_pendulum.Pendulum(), 1)


if __name__ == '__main__':
    unittest.main()
