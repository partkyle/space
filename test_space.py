import unittest
import space


class SpaceTestCase(unittest.TestCase):
    def test_space_goes_on_for_infinity(self):
        space_ = space.space()

        self.assertIsNotNone(space_)

        # Prove that space goes on for at least 9000
        for i in xrange(9000):
            space_ = space_.space
            self.assertIsNotNone(space_)
