from django.template import Template, Context
from django.test import TestCase


class TestWcswidthFilter(TestCase):
    def test_wcswidth_with_single_width_characters(self):
        template = Template("{% load wcwidth %}{{ x | wcswidth }}")
        context = Context({
            "x": "Hello",
        })
        actual = template.render(context)
        self.assertEqual(actual, "5")

    def test_wcswidth_with_double_width_characters(self):
        template = Template("{% load wcwidth %}{{ x | wcswidth }}")
        context = Context({
            "x": "こんにちは",
        })
        actual = template.render(context)
        self.assertEqual(actual, "10")
