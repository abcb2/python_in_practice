# -*- coding: utf-8 -*-
import unittest
import logging
from lib.multiplexer import Multiplexer
from lib.counter import Counter
from lib.event import Event


class MultiplexerTest(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def tearDown(self):
        pass

    def test01(self):
        c = Counter('hoge')
        m = Multiplexer()
        event = Event("hoge", 2)
        m.connect('hoge', c)
        m.send(event)
        self.assertTrue(c.hoge == 2)

        m.state = Multiplexer.DORMANT
        m.send(event)
        self.assertTrue(c.hoge == 2)

        m.state = Multiplexer.ACTIVE
        m.send(event)
        self.assertTrue(c.hoge == 4)

if __name__ == "__main__":
    unittest.main()
