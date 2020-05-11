=====================
django-wcwidth-filter
=====================

A collection of Django template filters for multi-width characters.

Installation
------------

.. code-block:: console

   $ python3 -m pip install djangohttpbench

Usage
-----

wcswidth filter
~~~~~~~~~~~~~~~

.. code-block:: python

   >>> template = Template("{% load wcwidth %}{{ x | wcswidth }}")
   >>> context = Context({
   >>>     "x": "Hello",
   >>> })
   >>> template.render(context)
   5
   >>> context = Context({
   >>>     "x": "こんにちは",
   >>> })
   >>> template.render(context)
   10
