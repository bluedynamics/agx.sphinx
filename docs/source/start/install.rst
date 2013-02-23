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


Install AGX from source (currently the only method)
---------------------------------------------------

In case you don't have **git** on your system, install it::

    apt-get install git

Clone the development buildout from github::

    git clone git://github.com/bluedynamics/agx.dev.git

Change directory to location of already checked out repository and run
bootstrap.py and buildout::

    python bootstrap.py
    ./bin/buildout

When buildout has finished, the AGX binary is located at ``bin/agx`` in
the installation directory.

Run ``./bin/agx -i``. If you get output similar to this::

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

AGX is ready to be used.

Congratulations, you can now use AGX.
