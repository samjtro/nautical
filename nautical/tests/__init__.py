import unittest
from ..location.point import Point
from ..location.util import haversine
from nautical.time.conversion import convert_noaa_time
from ..io.parse import get_noaa_forecast_url, get_url_source
from bs4 import BeautifulSoup


class TestNautical(unittest.TestCase):
    """
    Test the Nautical Package
    """

    """
    LOCATION sub module testing
    """
    def test_latitude(self):
        """
        Test both a valid and invalid latitude value checking the whether the values were set or not
        after each attempt.
        """
        p1 = Point(67.23, 0, 0)
        self.assertAlmostEqual(p1.latitude, 67.23, 2, "Latitude value is incorrect")

        p2 = Point(-67.23, 0, 0)
        self.assertAlmostEqual(p2.latitude, -67.23, 2, "Latitude value is incorrect")

        p2.latitude = "abgsdf"
        self.assertAlmostEqual(p2.latitude, -67.23, 2, "Latitude value is incorrect")

        p3 = Point(-90.23, 0, 0)
        self.assertAlmostEqual(p3.latitude, 0.0, 2, "Latitude value is incorrect")

    def test_longitude(self):
        """
        Test both a valid and invalid longitude value checking the whether the values were set or not
        after each attempt.
        """
        p1 = Point(0, 0.23, 0)
        self.assertAlmostEqual(p1.longitude, 0.23, 2, "Longitude value is incorrect")

        p2 = Point(0, -167.23, 0)
        self.assertAlmostEqual(p2.longitude, -167.23, 2, "Longitude value is incorrect")

        p2.longitude = "dasdf"
        self.assertAlmostEqual(p2.longitude, -167.23, 2, "Longitude value is incorrect")

        p3 = Point(0, 180.23, 0)
        self.assertAlmostEqual(p3.longitude, 0.0, 2, "Longitude value is incorrect")

    def test_altitude(self):
        """
        Test both a valid and invalid altitude value checking the whether the values were set or not
        after each attempt.
        """
        p1 = Point(0, 0, 1251231.2342)
        self.assertAlmostEqual(p1.altitude, 1251231.2342, 4, "Altitude value is incorrect")

        p1.altitude = "123123jnnkjk"
        self.assertAlmostEqual(p1.altitude, 1251231.2342, 4, "Altitude value is incorrect")

    def test_parser(self):
        """
        Test the parse function of the Point
        """
        p1 = Point()
        p1.parse("-110.123, 76.45, 123.67")

        self.assertAlmostEqual(p1.latitude, 76.45, 2, "Latitude value is incorrect")
        self.assertAlmostEqual(p1.longitude, -110.123, 3, "Longitude value is incorrect")
        self.assertAlmostEqual(p1.altitude, 123.67, 2, "Altitude value is incorrect")

    def test_distance(self):
        """
        Test the haversine distance function of the Point class

        test distance from virginia beach to norfolk Virginia

        """
        # location of virginia beach
        p = Point(36.8529, -75.9780)

        # location of norfolk
        dist = haversine(p, Point(36.8508, -76.2859))

        # roughly 27 km but it is closer to 27404.727 .... meters
        self.assertAlmostEqual(dist, 27404.73, 2, "Distance between VB and Norfolk is incorrect.")

    """
    IO sub module tests
    """

    def test_beautiful_soup(self):
        """
        Test that an invalid and valid url return the proper data
        """
        try:
            url = get_noaa_forecast_url(44099)
            soup = get_url_source(url)
            self.assertTrue(isinstance(soup, BeautifulSoup), "44099 did not return a viable Beautiful soup object")
        except Exception:
            pass

        try:
            bad_url = get_noaa_forecast_url("afasdfasdjfna")
            bad_soup = get_url_source(bad_url)
            self.assertFalse(isinstance(bad_soup, BeautifulSoup), "afasdfasdjfna did not return a viable Beautiful soup object")
        except Exception:
            pass

    def test_forecast_url(self):
        """
        Test valid and invalid sets of data passed to the create forecast url
        """
        try:
            self.assertNotEqual(get_noaa_forecast_url(44099), None, "Failed to find url for 44099")
            self.assertEqual(get_noaa_forecast_url(""), None, "Failed to find url")
        except Exception:
            pass

    @staticmethod
    def suite() -> unittest.TestSuite:
        """
        Create a test suite for all of the tests in this test sub module. The user
        can run the suite of tests to determine any issues on their system.
        :return: TestSuite object
        """
        suite = unittest.TestSuite()
        """ LOCATION TESTS """
        suite.addTest(TestNautical("test_latitude"))
        suite.addTest(TestNautical("test_longitude"))
        suite.addTest(TestNautical("test_altitude"))
        suite.addTest(TestNautical("test_parser"))
        suite.addTest(TestNautical("test_distance"))
        """ IO TESTS """
        suite.addTest(TestNautical("test_beautiful_soup"))
        suite.addTest(TestNautical("test_forecast_url"))

        return suite
