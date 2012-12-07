=======================
Generating Python Eggs
=======================

.. note::

  Experienced developers can jump to :ref:`profile_pyegg`.



An Example Model (for tests)
----------------------------

This model is used for the tests of this package.

.. image:: model-agx.generator.pyegg-testpackage.png
   :scale: 50%

When feeding it to AGX to generate code, the following files and folders are
created on the filesystem in a folder **agx.testpackage**:
::

   agx.testpackage
    ├── LICENSE.rst
    ├── MANIFEST.rst
    ├── README.rst
    ├── setup.py
    └── src
         └── agx
              ├── __init__.py
              └── testpackage
                   ├── __init__.py
                   ├── classinegg.py
                   ├── somepackage
                   │    ├── __init__.py
                   │    └── packageclass.py
                   └── testmodule.py
