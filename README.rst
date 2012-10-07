Documentation building buildout for AGX.
========================================
Install this buildout to work on and build the documentation. 
It will pull (sic!) in all relevant AGX packages.

Nightly build: https://jenkins.c-3-s.org/job/agx.sphinx_bluedynamics/AGX_Docs

Old stable version: https://agx.me

This Package is part of **AGX**. See `<http://agx.me>`_ for Details. 


Debian based Installation
-------------------------

   $ sudo apt-get install mscgen
   $ pip install virtualenv
   $ git clone git://github.com/bluedynamics/agx.sphinx.git
   $ . env/bin/activate
   (env)$ python bootstrap.py -c debian.cfg
   (env)$ bin/buildout -c debian.cfg
   (env)$ bin/sphinx


Mac based Installation
----------------------


   $ brew install mscgen
   $ easy_install pip
   $ pip install virtualenv
   $ git clone git://github.com/bluedynamics/agx.sphinx.git
   $ . env/bin/activate
   (env)$ python bootstrap.py -c mac.cfg
   (env)$ bin/buildout -c mac.cfg
   (env)$ bin/sphinx

If there are problems with compilation of some libs during the above:
   $ rm /usr/local/lib/libiconv.2.dylib
   $ ln -s /usr/lib/libiconv.2.dylib /usr/local/lib/libiconv.2.dylib


If you get a traceback during buildout about 'locale', try setting the locale
to a reasonable value and re-run buildout::

   ...
       raise ValueError, 'unknown locale: %s' % localename
   ValueError: unknown locale: UTF-8


   (env)$ export LC_ALL=de_DE.UTF-8
   (env)$ export LANG=de_DE.UTF-8
   (env)$ bin/buildout -c dev.mac.cfg


Creating Screenshots
--------------------

The screenshots were made on Ubuntu 12 and edited with Gimp to beautify them
with drop shadows. From the Menu pick
``Filters --> Light and Shadow --> Drop Shadow...''
first a dark one:

  Offset X = 8, Offset Y = 8, Blur radius = 15, Black,
  Opacity = 80, Allow Resizing=True

then a light one for the upper left corner:

  Offset X = -2, Offset Y = -2, Blur radius = 20, Black,
  Opacity = 30, Allow Resizing=True


Changes
=======

1.0dev
------

  - Initial
