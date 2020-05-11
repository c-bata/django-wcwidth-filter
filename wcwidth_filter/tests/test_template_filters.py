from django.template import Template, Context
from django.test import TestCase


class TestWcswidthFilter(TestCase):
    def test_single_width_characters(self):
        template = Template("{% load wcwidth %}{{ x | wcswidth }}")
        context = Context({
            "x": "Hello",
        })
        actual = template.render(context)
        self.assertEqual(actual, "5")

    def test_double_width_characters(self):
        template = Template("{% load wcwidth %}{{ x | wcswidth }}")
        context = Context({
            "x": "こんにちは",
        })
        actual = template.render(context)
        self.assertEqual(actual, "10")


class TestTruncateWcswidthFilter(TestCase):
    def test_single_width_characters_not_truncated(self):
        template = Template("{% load wcwidth %}{{ x | truncate_wcswidth:5 }}")
        context = Context({
            "x": "Hello",
        })
        actual = template.render(context)
        self.assertEqual(actual, "Hello")

    def test_double_width_characters_not_truncated(self):
        template = Template("{% load wcwidth %}{{ x | truncate_wcswidth:10 }}")
        context = Context({
            "x": "こんにちは",
        })
        actual = template.render(context)
        self.assertEqual(actual, "こんにちは")

    def test_single_width_characters_truncated(self):
        template = Template("{% load wcwidth %}{{ x | truncate_wcswidth:4 }}")
        context = Context({
            "x": "Hello",
        })
        actual = template.render(context)
        self.assertEqual(actual, "Hel…")

    def test_double_width_characters_truncated(self):
        template = Template("{% load wcwidth %}{{ x | truncate_wcswidth:5 }}")
        context = Context({
            "x": "こんにちは",
        })
        actual = template.render(context)
        self.assertEqual(actual, "こん…")

    def test_double_width_characters_truncated2(self):
        template = Template("{% load wcwidth %}{{ x | truncate_wcswidth:6 }}")
        context = Context({
            "x": "こんにちは",
        })
        actual = template.render(context)
        self.assertEqual(actual, "こん…")

    def test_double_width_characters_truncated3(self):
        template = Template("{% load wcwidth %}{{ x | truncate_wcswidth:9 }}")
        context = Context({
            "x": "こんにちは",
        })
        actual = template.render(context)
        self.assertEqual(actual, "こんにち…")
