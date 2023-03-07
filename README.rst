Fivetran service API Wrapper
============================



Installation
============

Install from PyPI with:

.. code::

    pip install fivetraner

Usage
=====

.. code:: python

    from fivetraner import FivetranWrapper


    logger = logging.getLogger(__name__)

    fw = FivetranWrapper(logger=logger)
