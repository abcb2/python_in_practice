import unittest
import datetime
import pytz


class DateTimeTests(unittest.TestCase):
    def test_delta_calc_converts_timezone_info_to_utc(self):
        self.assertTrue(True)
        dt_utc = datetime.datetime.now(tz=datetime.timezone.utc)
        dt_tokyo = datetime.datetime.now(
            tz=datetime.timezone(datetime.timedelta(hours=9))
        )
        self.assertEqual(dt_tokyo.tzname(), "UTC+09:00")
        self.assertEqual(dt_utc.tzname(), "UTC+00:00")

        delta = dt_tokyo - dt_utc
        self.assertEqual(type(delta), datetime.timedelta)
        self.assertTrue(delta.total_seconds() < 1.0)

    def test_timezone_info_replace(self):
        dt_utc = datetime.datetime.now(tz=datetime.timezone.utc)
        self.assertEqual(dt_utc.tzname(), "UTC+00:00")
        dt_utc_replaced = dt_utc.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
        self.assertEqual(dt_utc_replaced.tzname(), "UTC+09:00")
        self.assertEqual(
            dt_utc_replaced.strftime("%Y-%m-%d %H:%M:%S"),
            dt_utc.strftime("%Y-%m-%d %H:%M:%S")
        )

    def test_delta(self):
        dt_now = datetime.datetime.now()
        dt_after = dt_now + datetime.timedelta(hours=9)
        self.assertEqual(dt_after - dt_now, datetime.timedelta(hours=9))

        dt_now_replaced = dt_now.replace(tzinfo=datetime.timezone.utc)
        dt_after_replaced = dt_after.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=9)))
        # print(dt_now_replaced, dt_after_replaced)
        self.assertEqual(dt_after_replaced - dt_now_replaced, datetime.timedelta(seconds=0))


if __name__ == "__main__":
    unittest.main()
