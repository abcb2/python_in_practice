import unittest
import datetime
import pytz


class PyTzTests(unittest.TestCase):
    def test_pytz_01(self):
        utc = pytz.utc
        dt = datetime.datetime.now(tz=utc)
        self.assertEqual(dt.tzinfo, utc)

    def test_pytz_02(self):
        dt_now = datetime.datetime.now()
        self.assertEqual(dt_now.tzinfo, None)

        tz_tokyo = pytz.timezone("Asia/Tokyo")
        dt_tokyo = dt_now.replace(tzinfo=tz_tokyo)
        self.assertEqual(
            repr(dt_tokyo.tzinfo),
            "<DstTzInfo 'Asia/Tokyo' JST+9:00:00 STD>"
        )
        self.assertEqual(dt_tokyo.tzname(), 'JST')

        dt_utc = dt_now.replace(tzinfo=pytz.utc)
        self.assertEqual(repr(dt_utc.tzinfo), "<UTC>")
        self.assertEqual(dt_utc.tzname(), 'UTC')

        delta = dt_utc - dt_tokyo
        self.assertEqual(delta, datetime.timedelta(hours=9))


if __name__ == "__main__":
    unittest.main()
