from unittest import TestCase

from demo_package_lavajuno import demo

class TestDemo(TestCase):
    def setUp(self):
        pass

    def test_example(self):
        demo.demo_function()
