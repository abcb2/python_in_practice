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

    def test_pytz_03(self):
        dt_now = datetime.datetime.now()
        self.assertEqual(dt_now.tzinfo, None)

        with self.assertRaises(ValueError):
            # can't use astimezone method to naive dt object
            dt_tokyo = dt_now.astimezone(pytz.timezone('Asia/Tokyo'))

        dt_utc = datetime.datetime(2016, 1, 1, 10, 0, 0, tzinfo=pytz.utc)
        self.assertEqual(str(dt_utc), "2016-01-01 10:00:00+00:00")

        dt_tokyo = dt_utc.astimezone(pytz.timezone('Asia/Tokyo'))
        self.assertEqual(str(dt_tokyo), "2016-01-01 19:00:00+09:00")


if __name__ == "__main__":
    unittest.main()
