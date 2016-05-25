# -*- coding: utf-8 -*-
import unittest
import logging
from lib.counter import Counter


class CounterTest(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def tearDown(self):
        pass

    def test01(self):
        c = Counter()
        self.assertTrue(c.anonymous is True)

        c2 = Counter("taro", "jiro")
        self.assertTrue(c2.anonymous is False)
        self.assertTrue(c2.taro == 0)
        self.assertTrue(c2.jiro == 0)

    def test02(self):
        c = Counter("hoge")
        from collections import namedtuple
        Event = namedtuple("Event", ("name", "count"))
        event = Event(name="hoge", count=2)
        c(event)
        self.logger.info("count:%s", c.hoge)
        self.assertTrue(c.hoge == 2)

        event2 = Event(name="hoge", count=3)
        c(event2)
        self.assertTrue(c.hoge == 5)

    def test03(self):
        """
        countできないイベントを渡された場合は例外となる
        """
        c = Counter("taro")
        from collections import namedtuple
        Event = namedtuple("Event", ("name", "count"))
        event = Event(name="jiro", count=1)
        error_flag = False
        try:
            c(event)
        except:
            error_flag = True
        self.assertTrue(error_flag is True)


if __name__ == "__main__":
    unittest.main()
