==============
Installing AGX
==============


Pre-requirements
----------------

AGX requires header files for libxml2 in order to install
and run correctly.

On debian based systems install the development headers like so::

    apt-get install python-dev libxml2-dev libxslt1-dev

.. note::
   Debian folks may grep buildout.cfg
   (and etc/base.cfg) for "apt-get" instructions ;-)


Download and install from pypi
------------------------------

Download and unpack ``agx.dev`` from ``https://pypi.python.org/pypi/agx.dev``.

Enter directory from command line and run buildout::

    python bootstrap.py --version 1.7
    ./bin/buildout


Install AGX from github
-----------------------

In case you don't have **git** on your system, install it::

    apt-get install git

Clone ``agx.dev`` from github::

    git clone git://github.com/bluedynamics/agx.dev.git

Enter directory from command line and run buildout::

    python bootstrap.py --version 1.7
    ./bin/buildout


Install development sources
---------------------------

Both - installation from pypi and from github provide installing AGX with
source packages for development of AGX itself::

    python bootstrap.py --version 1.7
    ./bin/buildout -c dev.cfg


Check Installation
------------------

When buildout has finished, the AGX binary is located at ``bin/agx`` in
the installation directory.

Run ``./bin/agx -i``. You should get output similar to this::

    AGX 1.0a2 (Reincarnation)
    Installed generators:
        agx.generator.generator (1.0a1)
        agx.generator.sql (1.0a1)
        agx.generator.dexterity (1.0a1)
        agx.generator.uml (1.0a1)
        agx.generator.pyegg (1.0a1)
        agx.generator.plone (1.0a1)
        agx.generator.buildout (1.0a1)
        agx.generator.zca (1.0a1)

Congratulations, AGX is now ready to be used.
