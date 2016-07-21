# -*- coding: utf-8 -*-

import unittest
from unittest import mock
from asyncio import test_utils
from asyncio import base_events
import asyncio


class BaseEventLoopTests(test_utils.TestCase):
    # def setUp(self):
    #     self.loop = base_events.BaseEventLoop()
    #     self.loop._selector = mock.Mock()
    #     self.loop._selector.select.return_value = ()
    #     self.set_event_loop(self.loop)

    def setUp(self):
        self.loop = asyncio.get_event_loop()

    def test_close(self):
        self.assertFalse(self.loop.is_closed())
        self.loop.close()
        self.assertTrue(self.loop.is_closed())

        # possible close() more than once
        self.loop.close()
        self.loop.close()

        future = asyncio.Future(loop=self.loop)
        self.assertRaises(RuntimeError, self.loop.run_forever)
        self.assertRaises(RuntimeError, self.loop.run_until_complete, future)

    def test__add_callback_handle(self):
        pass


if __name__ == "__main__":
    unittest.main()
