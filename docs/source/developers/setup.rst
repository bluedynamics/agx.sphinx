Setting up AGX and Tests
========================

Here we describe the procedure to get AGX and the tests up and running from scratch. 

You may use `virtualenv <http://www.virtualenv.org>`_ to keep the Python setup separated
from your system Python. Virtualenv is supplied with many package managers::

    apt-get install python-virtualenv


1) Get the development bundle of AGX:
::

   $ git clone git://github.com/bluedynamics/agx.dev.git
   $ cd agx.dev


2) Create a virtualenv for your AGX setup:
::

   agx.dev$ virtualenv .


3) Bootstrap and run the buildout:
::

   agx.dev$ ./bin/python bootstrap.py -c dev.cfg
   agx.dev$ ./bin/buildout -c dev.cfg


3a) Run the tests:
::

   agx.dev$ ./tests.sh


3b) You can also run tests for a specific package or generator:
::

   agx.dev$ bin/test agx.generator.pyegg
