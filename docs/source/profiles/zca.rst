.. _profile_zca:

================
UML:Profile zca
================

Overview
---------

This document describes the **ZCA** UML profile.

.. image:: profile_zca.svg
   :scale: 50%


.. note:: A more general description can be found here: :ref:`users_zca`.



.. list-table:: List of Stereotypes
   :widths: 55 20 25
   :header-rows: 1

   * - UML:Stereotype
     - Metaclasses
     - Tagged Values
   * - name of stereotype with link to details
     - applicable to
     - .
   * - :ref:`st_permission`
     - UML:Package
     - --
   * - :ref:`st_subscriber`
     - UML:Class
     - title, description, id
   * - :ref:`st_adapter`
     - UML:Class, UML:Interface
     - name
   * - :ref:`st_utility`
     - UML:Class, UML:Interface
     - name
   * - :ref:`st_adapts`
     - UML:Dependency
     - order
   * - :ref:`st_permits`
     - UML:Dependency
     - --
   * - :ref:`st_for`
     - UML:Dependency
     - --
   * - :ref:`st_subscribes`
     - UML:Dependency
     - --
   * - :ref:`st_provides`
     - UML:InterfaceRealisation
     - --
   * - :ref:`st_zcml`
     - UML:InterfaceRealization
     - --



.. _st_permission:

UML:Stereotype <<permission>>
------------------------------

Permission settings. 

Metaclasses
~~~~~~~~~~~~

- UML:Class

Tagged Values
~~~~~~~~~~~~~~

**title**
    Name of permission.

**description**
    Description of permission.

**id**
    Id of permission.




.. _st_subscriber:

UML:Stereotype <<subscriber>>
------------------------------

Metaclasses
~~~~~~~~~~~~

- UML:Class

Tagged Values
~~~~~~~~~~~~~~

**None**


UML:Stereotype <<event>>
-------------------------

Metaclasses
~~~~~~~~~~~~

- UML:Class
- UML:Interface

Tagged Values
~~~~~~~~~~~~~~

**None**



.. _st_adapter:

UML:Stereotype <<adapter>>
---------------------------

Metaclasses
~~~~~~~~~~~~

- UML:Class
- UML:Interface

Tagged Values
~~~~~~~~~~~~~~

**name**
    String: name of the adapter.




.. _st_utility:

UML:Stereotype <<utility>>
---------------------------

Utilities modelled as Classes with outgoing dependencies (with the <<provides>>
stereotype) to some interface.

Metaclasses
~~~~~~~~~~~~

- UML:Class
- UML:Interface

Tagged Values
~~~~~~~~~~~~~~

**name**
    String: a name for it.




.. _st_adapts:

UML:Stereotype <<adapts>>
--------------------------

Draw a dependency from an **Adapter** to an adapted class or interface.

Metaclasses
~~~~~~~~~~~~

- UML:Dependency

Tagged Values
~~~~~~~~~~~~~~

**order**
    String: the order of adaption.




.. _st_permits:

UML:Stereotype <<permits>>
---------------------------

Dependency between **Adapter** and a **Permission**.

Metaclasses
~~~~~~~~~~~~

- UML:Dependency

Tagged Values
~~~~~~~~~~~~~~

**None**





.. _st_for:

UML:Stereotype <<for>>
-----------------------

Metaclasses
~~~~~~~~~~~~

- UML:Dependency

Tagged Values
~~~~~~~~~~~~~~

**None**




.. _st_subscribes:

UML:Stereotype <<subscribes>>
------------------------------

Metaclasses
~~~~~~~~~~~~

- UML:Dependency

Tagged Values
~~~~~~~~~~~~~~

**None**




.. _st_provides:

UML:Stereotype <<provides>>
----------------------------

Metaclasses
~~~~~~~~~~~~

- UML:InterfaceRealization


Tagged Values
~~~~~~~~~~~~~~

**None**




.. _st_zcml:

UML:Stereotype <<zcml>>
------------------------

Metaclasses
~~~~~~~~~~~~

- UML:InterfaceRealization

Tagged Values
~~~~~~~~~~~~~~

**None**


