Setting up AGX Tests
====================

Here we describes the procedure to get the AGX tests up and running from scratch. 
In this example we build a full Python 2.6 installation to keep the setup clean 
and self-contained. You might want to skip the installation of Python if you 
consider to use an other interpreter of your choice.

1) First we install plain Python 2.6:

$ svn co https://svn.plone.org/svn/collective/buildout/bda-naked-python
$ cd bda-naked-python
bda-naked-python$ python bootstrap.py
bda-naked-python$ ./bin/buildout -v
bda-naked-python$ cd ..

2) Then we get the development bundle of AGX:

$ git clone git://github.com/bluedynamics/agx.dev.git
$ cd agx.dev
agx.dev$ ../bda-naked-python/parts/python/bin/python2.6 bootstrap.py -c [dev.cfg|anon.cfg]
agx.dev$ ./bin/buildout -c [dev.cfg|anon.cfg]
agx.dev$ cd ..

3) What we can do now is run the tests:

agx.dev$ ./bin/test
