# Your mission here is to create a function that gets a tuple and returns a tuple with 3 elements - the first, third and second to the last for the given array.
#
# Input: A tuple, at least 3 elements long.
#
# Output: A tuple.
#
# Example:
#
# easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
# easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
# easy_unpack((6, 3, 7)) == (6, 7, 3)
import unittest


def easy_unpack(a):
    if len(a) > 2:
        print((a[0], a[2], a[-2]))
        return (a[0], a[2], a[-2])
    else:
        print('Uncorrected size input tuple.')
        return None


class Test_My_Functions(unittest.TestCase):
    def test_ease_unpack(self):
        self.assertEqual(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)),(1,3,7))
        self.assertEqual(easy_unpack((1, 1, 1, 1)), (1, 10, 1))
        self.assertEqual(easy_unpack((6, 3, 7)), (6, 7, 3))

if __name__ == '__main__':
    unittest.main()

