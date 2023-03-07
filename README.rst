Fivetran service API Wrapper
=============



Installation
============

Install from PyPI with:

.. code::

    pip install fivetran-wrapper

Usage
=====

.. code:: python

    from fivetran-wrapper import FivetranWrapper


    logger = logging.getLogger(__name__)

    fw = FivetranWrapper(logger=logger)
