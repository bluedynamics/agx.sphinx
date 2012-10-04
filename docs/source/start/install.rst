==============
Installing AGX
==============


Pre-requirements
----------------

AGX requires python 2.6 and dev header files for libxml2 in order to install
and run correctly.

On debian based systems, install dev headers like so::

    apt-get install libxml2-dev libxslt1-dev


Install AGX from source (currently the only method)
---------------------------------------------------

Clone development buildout from github::

    git clone git://github.com/bluedynamics/agx.dev.git

Change directory to location of already checked out repository and run
bootstrap.py and buidlout::

    python bootstrap.py
    ./bin/buildout

When buildout has finished, the AGX binary is located at ``bin/agx`` in
the installation directory.

Run ``./bin/agx -i``. If you get output similar to this::

    AGX 3.0-dev Development

AGX is ready to be used.

Congratulations, you can now use AGX.
