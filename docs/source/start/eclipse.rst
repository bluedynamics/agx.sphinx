===================================================
Installing and configuring Eclipse for use with AGX
===================================================

This is the installation instruction to use the Eclipse IDE for development.
Currenty AGX requires Eclipse Indigo Modelling Edition.


Install Eclipse
---------------

Make sure to have an appropriate Java-interpreter on your machine.
Ubuntu users can simply::

    sudo apt-get install openjdk-7-jdk

Download and install the **Indigo** Eclipse Modeling Tools bundle suitable for
your operating system from the
`download page <http://www.eclipse.org/downloads/packages/release/indigo/sr2>`_.

.. note::
    If in doubt whether to install 32bit or 64bit version of eclipse, this
    issue has been discussed at `stack overflow 
    <http://stackoverflow.com/questions/9727430/java-and-eclipse-32-vs-64bit>`_.
    Spoiler: 32bit

Unpack the downloaded ZIP or tarball to a location of your choice. Eclipse
should run if Java was installed properly by executing the eclipse binary::

    /eclipse/install/path/eclipse

.. note::
    Note for GTK Users (Gnome i.e.) - There is a bug in some older versions of
    GTK that causes certain print backends to hang. Fix it by providing a
    2-liner script as eclipse launcher::

        #!/bin/sh
        export GDK_NATIVE_WINDOWS=1
        /eclipse/install/path/eclipse -vmargs -XX:+AggressiveHeap

On first startup, eclipse asks you for a workspace location. This is the
location where your eclipse projects live.

After defining the workspace the eclipse welcome screen comes up. Go ahead and
dig around a little bit or go directly to the workbench (icon on the 
right).


Install Papyrus
---------------

Eclipse Modeling Tools come along with facilities for drawing UML models.
Anyway we'll use Papyrus for modeling, it's one of the shipped tools.

Use Eclipses menu and find ``Help --> Install Modeling Components``,
search for Papyrus and install it. 

.. image:: ../_static/eclipse_indigo_modeling_components_papyrus.png


Install PyDev
-------------

PyDev is an Eclipse plugin for Python development.

To install pydev, use Eclipses menu and find ``Help --> Install New Software``,
click ``add`` button, enter ``pydev`` as name and the location
``http://pydev.org/updates/`` to search for the plugin.

.. image:: ../_static/eclipse_indigo_modeling_components_add_plugin.png

Select ``pydev`` plugin from available software, click ``install`` and follow
the install procedure.

.. image:: ../_static/eclipse_indigo_modeling_components_install_plugin.png


Install AGX Eclipse plugin
--------------------------

AGX Ships with an Eclipse plugin for invoking the generator out of the IDE.

To install the AGX Eclipse plugin, repeat the procedure as shown in
``Install PyDev``, using ``AGX`` as name and ``http://agx.me/updates`` as
plugin location when adding the AGX update site.

.. note::
    The AGX plugin required both Papyrus and Pydev in order to install and
    run correctly.


Unrelated but useful plugins for development with Eclipse
---------------------------------------------------------


Install ReST Editor
~~~~~~~~~~~~~~~~~~~

An Eclipse plug-in providing support to edit reStructuredText files.

* `Homepage <http://resteditor.sourceforge.net/>`_.

* Update Sites: http://eclipse-color-theme.github.com/update and
  http://resteditor.sourceforge.net/eclipse


Install YAML Editor
~~~~~~~~~~~~~~~~~~~

An Eclipse plug-in providing support to edit YAML files.

* `Homepage <http://foo.bar/>`_.

* Update Site: http://foo.bar


Install Javascript Editor
~~~~~~~~~~~~~~~~~~~~~~~~~

Eclipse provides a webtools project which ships editors for web technologies.

...


Install XML/HTML/PT Editor
~~~~~~~~~~~~~~~~~~~~~~~~~~

Install foo plugins from the webtools update site.

...
