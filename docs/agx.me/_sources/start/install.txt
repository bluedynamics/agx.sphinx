==============
Installing AGX
==============

Pre-Requirements
----------------

You need Python 2.6 and the dev-headers of libxml2 in order to run AGX.

Install AGX from Source (currently the only method)
---------------------------------------------------

Checkout development project by typing
::

    git clone git://github.com/bluedynamics/agx.dev.git

Enter agx.dev and run bootstrap
::

    python bootstrap.py -c [dev.cfg|anon.cfg]

Run Buildout
::

    ./bin/buildout -c [dev.cfg|anon.cfg]

When buildout has finished, the AGX binary is located at
``bin/agx`` in install_dir.

Run ``./bin/agx -i`` and you get output similar to this
::

    AGX 3.0-dev Development

Congratulations, you can now use AGX.