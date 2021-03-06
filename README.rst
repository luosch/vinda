vinda
=====

.. image:: https://img.shields.io/pypi/v/vinda.svg
	:target: https://pypi.python.org/pypi/vinda

.. image:: https://img.shields.io/pypi/dm/vinda.svg
        :target: https://pypi.python.org/pypi/vinda

:code:`vinda` can help user construct their index pages rapidly

Installation
------------

To install vinda, simply:

.. code-block:: bash

    $ pip install vinda


Usage
-----

.. code-block:: python

    >>> import vinda
    >>> vinda.look(ignore_list=['.git', '.DS_Store'])


Screenshots
-----------

.. image:: https://raw.githubusercontent.com/luosch/vinda/master/screenshots/index.png


Version 0.1.0 (2016.02.03)
--------------------------

*   Use Jinja2 to constuct index page
*   Only Supporting traverse in current path


Version 0.2.0 (2016.02.03)
--------------------------

*   fix bug -> ``template.html`` missing 


Version 0.3.0 (2016.02.04)
--------------------------

*   fix bug -> crash when writing ``index.html`` due to ``unicode``
*   add feature -> support recursive index page constructing
*   refactor -> output html file must be ``index.html`` 


Todo
----

*   clear function
*   avoid delete unconcerned ``index.html``
*   pagination


Lincense
--------

All source code is licensed under the `MIT License`_.

.. _MIT License: https://raw.githubusercontent.com/luosch/vinda/master/LICENSE
