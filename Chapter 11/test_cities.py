import unittest
from city_functions import display_city


class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        display = display_city('tokyo', 'japan')
        self.assertEqual(display, 'Tokyo, Japan')

    def test_city_country_population(self):
        display = display_city('tokyo', 'japan', 5000)
        self.assertEqual(display, 'Tokyo, Japan - population 5000')


if __name__ == "__main__":
    unittest.main()
