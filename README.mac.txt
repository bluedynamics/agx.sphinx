To set this up on a mac, I installed mscgen through homebrew:

  brew install mscgen

Before that, I had to move around libiconvs dylib:

  rm /usr/local/lib/libiconv.2.dylib
  ln -s /usr/lib/libiconv.2.dylib /usr/local/lib/libiconv.2.dylib


How to get going
================


I tried to set this up on a vanilla Mac (10.7). 

$ easy_install pip
$ pip install virtualenv
$ git clone git://github.com/bluedynamics/agx.sphinx.git
$ . env/bin/activate
(env)$ python bootstrap.py -c dev.mac.cfg
(env)$ bin/buildout -c dev.mac.cfg

If you get a traceback during buildout about 'locale', try setting the locale
to a reasonable value and rerun buildout:

   ...
       raise ValueError, 'unknown locale: %s' % localename
   ValueError: unknown locale: UTF-8


(env)$ export LC_ALL=de_DE.UTF-8
(env)$ export LANG=de_DE.UTF-8
(env)$ bin/buildout -c dev.mac.cfg
