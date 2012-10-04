==============
Installing AGX
==============


Pre-requirements
----------------

AGX requires python 2.6 and dev header files for libxml2 in order to install
and run correctly.

On debian based systems, install dev headers like so::

    apt-get install libxml2-dev libxslt1-dev

Attention Ubuntu Users
----------------------

If you run 12.04, run the following steps in order to install python2.6::

    add-apt-repository ppa:fkrull/deadsnakes
    apt-get update
    apt-get install python2.6-dev
    apt-get install git
    apt-get install libxml2-dev libxslt1-dev
    apt-get install python-distribute-deadsnakes


Install AGX from source (currently the only method)
---------------------------------------------------

Clone development buildout from github::

    git clone git://github.com/bluedynamics/agx.dev.git

Change directory to location of already checked out repository and run
bootstrap.py and buidlout::

    python2.6 bootstrap.py
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
        agx.generator.dexterity (f4ba3f45b63281ab75cde3d86a23af8cbdad2e02)
        agx.generator.buildout (7d10edbeaa5089f133853b93e58cc77945322a2b)

AGX is ready to be used.

Congratulations, you can now use AGX.
