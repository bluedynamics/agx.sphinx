.. _profile_plone:

==================
UML:Profile plone
==================

This document describes the UML profile used for Plone Products
with Generic Setup profiles. 

Overview
---------

.. image:: profile_plone.png
   :scale: 50%


.. note:: A more general description can be found here: :ref:`users_plone`



.. list-table:: List of Stereotypes
   :widths: 55 20 25
   :header-rows: 1

   * - UML:Stereotype
     - Metaclasses
     - Tagged Values
   * - name of stereotype with link to details
     - applicable to
     - .
   * - :ref:`st_gsprofile`
     - UML:Package
     - None
   * - :ref:`st_content_type`
     - UML:Class
     - create_content_class
   * - :ref:`st_referencable`
     - UML:Class
     - None
   * - :ref:`st_dynamic_view`
     - UML:Class
     - None
   * - :ref:`st_view`
     - UML:Class, UML:Dependency
     - name. permission, layer



.. _st_gsprofile:

UML:Stereotype <<gsprofile>>
-----------------------------

This stereotype can be attached to packages. In combination with the <<pyegg>>
stereotype can build eggs good for use as plugins for Plone.

Metaclasses
~~~~~~~~~~~~
- UML:Package

Tagged Values
~~~~~~~~~~~~~~

**None**




.. _st_content_type:

UML:Stereotype <<content_type>>
--------------------------------

Turn a class into a content type.

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values
~~~~~~~~~~~~~~

**create_contentclass**
    Integer



.. _st_referencable:

UML:Stereotype <<referencable>>
--------------------------------

This stereotype can be attached to classes if they are to be made referencable.

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values
~~~~~~~~~~~~~~

**None**



.. _st_dynamic_view:

UML:Stereotype <<dynamic view>>
--------------------------------

A dynamic view class. It actually is a view

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values
~~~~~~~~~~~~~~

**None**



.. _st_view:

UML:Stereotype <<view>>
------------------------

This stereotype can be attached to packages.

Metaclasses
~~~~~~~~~~~~
- UML:Class
- UML:Dependency

Tagged Values
~~~~~~~~~~~~~~

**name**
    String: name of the view.

**permission**
    String: permission for that view.

**layer**
    String: the layer the view is in.


