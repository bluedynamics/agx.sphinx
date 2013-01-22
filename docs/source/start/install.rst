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

    AGX 3.0-dev Develop
    Installed generators:
        agx.generator.uml (6b4b7c33b7d6e48f91479f902b80b37e834104c1)
        agx.generator.pyegg (c51cecb86e21da6a60e126d36b21e59ee250c2d7)
        agx.generator.zca (4c8e835921da036f92a52d80b1378c344f528a88)
        agx.generator.sql (08a33d0c1b49505e26b9885e575dc67fe1d8e864)
        agx.generator.plone (b9d04d1c86c8977151adc635f35d883486b12268)
        agx.generator.dexterity (771dde17a7bf4640b672aac46b41e09d042302a8)
        agx.generator.buildout (7d10edbeaa5089f133853b93e58cc77945322a2b)
        agx.generator.generator (5ad11b18339b5cf85989257c1622dcdbf9579521)

AGX is ready to be used.

Congratulations, you can now use AGX.
