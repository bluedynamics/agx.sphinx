.. _users_buildout:

=========
Buildout
=========

.. note::

  Experienced developers can jump to :ref:`profile_buildout`.


Create a working setup for **buildout**.

Buildout is a software build system, the Python equivalent of Make, Maven and
the like, enabling repeatable setups: bootstrap self-contained installations
with dependencies and configuration.
See `<http://www.buildout.org/>`_.


At this stage, **agx.generator.buildout** only supports generation of buildouts
for Plone version 4.1.2.


If you want AGX to generate files for a Plone 4.1.2 buildout,
just add the **<<plone_self_contained>>** stereotype to your UML:Package.

