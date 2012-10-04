This Package is part of **AGX**. See `<http://agx.me>`_ for Details.


Debian based Installation
=========================

$ sudo apt-get install mscgen
$ pip install virtualenv
$ git clone git://github.com/bluedynamics/agx.sphinx.git
$ . env/bin/activate
(env)$ python bootstrap.py -c debian.cfg
(env)$ bin/buildout -c debian.cfg
(env)$ bin/sphinx


Mac based Installation
======================

$ rm /usr/local/lib/libiconv.2.dylib
$ ln -s /usr/lib/libiconv.2.dylib /usr/local/lib/libiconv.2.dylib
$ brew install mscgen
$ easy_install pip
$ pip install virtualenv
$ git clone git://github.com/bluedynamics/agx.sphinx.git
$ . env/bin/activate
(env)$ python bootstrap.py -c mac.cfg
(env)$ bin/buildout -c mac.cfg
(env)$ bin/sphinx

If you get a traceback during buildout about 'locale', try setting the locale
to a reasonable value and re-run buildout::

   ...
       raise ValueError, 'unknown locale: %s' % localename
   ValueError: unknown locale: UTF-8

(env)$ export LC_ALL=de_DE.UTF-8
(env)$ export LANG=de_DE.UTF-8
(env)$ bin/buildout -c dev.mac.cfg


Changes
=======

1.0dev
------

  - Initial