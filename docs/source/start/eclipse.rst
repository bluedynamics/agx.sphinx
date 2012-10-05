===================================================
Installing and configuring Eclipse for use with AGX
===================================================

This is the installation instruction to use the Eclipse IDE for development.
Currenty AGX requires Eclipse Indigo Modelling Edition.


Installing Eclipse
------------------

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

Note for GTK Users (Gnome i.e.) - There is a bug in some versions of GTK that
causes certain print backends to hang. Fix it by providing a 2-liner
script as eclipse launcher::

    #!/bin/sh
    export GDK_NATIVE_WINDOWS=1
    /eclipse/install/path/eclipse -vmargs -XX:+AggressiveHeap

On first startup, eclipse asks you for a workspace location. This is the
location where your eclipse projects live.

After defining the workspace the eclipse welcome screen comes up. Go ahead and
dig around a little bit or go directly to the workbench (icon on the 
right).


Installing Papyrus
------------------

Eclipse Modeling Tools come along with facilities for drawing UML models.
Anyway we'll use Papyrus for modeling, it's one of the shipped tools.

Use Eclipses Menu and find 'Help --> Install Modeling Components',
search for Papyrus and install it. 

.. image:: ../_static/eclipse_indigo_modeling_components_papyrus.png


Installing Eclipse AGX
----------------------

AGX Ships with an Eclipse plugin for invoking the generator out of the IDE.
The update site for this plugin is at `<http://agx.me/updates/>`_. Install it
using the update manager.


Using PyDev
-----------

PyDev is an Eclipse plugin for Python development and the choice if you
decide to use Eclipse as your Python IDE.

Using it has the advantage of combining modeling, code generation and custom
work on the generated stuff all in the same IDE - hurrah!.

The update site for Pydev is at `<http://pydev.org/updates/>`_.


Using Aptana Studio
-------------------

Aptana Studio is an IDE for building Web-applications and comes along
with HTML, CSS and JavaScript tools and is is a pretty useful extension.

The update site for Aptana is located at
`<http://download.aptana.org/tools/studio/plugin/install/studio>`_.
