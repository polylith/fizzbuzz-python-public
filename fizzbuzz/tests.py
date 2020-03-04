import unittest
import xmlrunner

from fizzbuzz.task import fizzbuzz


class Test(unittest.TestCase):

    def test_business_as_usual(self):
        actual = fizzbuzz(1)
        assert actual is 1, "fizzbuzz function called with {}, so it should return {} but was {}".format(1, 1, actual)

        actual = fizzbuzz(2)
        assert actual is 2, "fizzbuzz function called with {}, so it should return {} but was {}".format(2, 2, actual)

        actual = fizzbuzz(4)
        assert actual is 4, "fizzbuzz function called with {}, so it should return {} but was {}".format(4, 4, actual)

        actual = fizzbuzz(7)
        assert actual is 7, "fizzbuzz function called with {}, so it should return {} but was {}".format(7, 7, actual)

        actual = fizzbuzz(998)
        assert actual is 998, "fizzbuzz function called with {}, so it should return {} but was {}".format(998, 998, actual)

    def test_fizz(self):
        actual = fizzbuzz(3)
        assert actual == "fizz", "fizzbuzz function called with {}, so it should return {} but was {}".format(3, "fizz", actual)

        actual = fizzbuzz(6)
        assert actual == "fizz", "fizzbuzz function called with {}, so it should return {} but was {}".format(6, "fizz", actual)

        actual = fizzbuzz(111)
        assert actual == "fizz", "fizzbuzz function called with {}, so it should return {} but was {}".format(111, "fizz", actual)

    def test_buzz(self):
        actual = fizzbuzz(5)
        assert actual == "buzz", "fizzbuzz function called with {}, so it should return {} but was {}".format(5, "buzz", actual)

        actual = fizzbuzz(10)
        assert actual == "buzz", "fizzbuzz function called with {}, so it should return {} but was {}".format(10, "buzz", actual)

        actual = fizzbuzz(20)
        assert actual == "buzz", "fizzbuzz function called with {}, so it should return {} but was {}".format(20, "buzz", actual)

        actual = fizzbuzz(500)
        assert actual == "buzz", "fizzbuzz function called with {}, so it should return {} but was {}".format(500, "buzz", actual)

    def test_fizz_buzz(self):
        actual = fizzbuzz(15)
        assert actual == "fizzbuzz", "fizzbuzz function called with {}, so it should return {}".format(15, "fizzbuzz", actual)

        actual = fizzbuzz(30)
        assert actual == "fizzbuzz", "fizzbuzz function called with {}, so it should return {}".format(30, "fizzbuzz", actual)

        actual = fizzbuzz(45)
        assert actual == "fizzbuzz", "fizzbuzz function called with {}, so it should return {}".format(45, "fizzbuzz", actual)

        actual = fizzbuzz(600)
        assert actual == "fizzbuzz", "fizzbuzz function called with {}, so it should return {}".format(600, "fizzbuzz", actual)



if __name__ == '__main__':
    with open('results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
