.. _profile_sql:

=================
UML:Profile sql
=================


Overview
---------

This document describes the UML profile for SQL.

.. image:: profile_sql.svg
   :scale: 50%


UML:Stereotype <<sql_content>>
-------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values
~~~~~~~~~~~~~~

**None**


UML:Stereotype <<sql_table>>
-----------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values
~~~~~~~~~~~~~~

**None**


UML:Stereotype <<sql_concrete_table_inheritance>>
--------------------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values
~~~~~~~~~~~~~~

**None**


UML:Stereotype <<joined_table_inheritance>>
--------------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values
~~~~~~~~~~~~~~

**None**


UML:Stereotype <<column>>
--------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values
~~~~~~~~~~~~~~

**index**
    Boolean

**not_null**
    Boolean

**unique**
    Boolean

**default**
    String

**server_default**
    String


UML:Stereotype <<primary>>
---------------------------

Special type of <<column>>

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values
~~~~~~~~~~~~~~

**None**


UML:Stereotype <<sql_type>>
----------------------------

Metaclasses
~~~~~~~~~~~~
- UML:PrimitiveType

Tagged Values
~~~~~~~~~~~~~~

**classname**
    String

**import_from**
    String

**default**
    String


UML:Stereotype <<z3c_saconfig>>
--------------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Package

Tagged Values
~~~~~~~~~~~~~~

**engine_name**
    String

**engine_url**
    String

**session_name**
    String


UML:Stereotype <<attribute_maped>>
-----------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Association

Tagged Values
~~~~~~~~~~~~~~

**key**
    String


UML:Stereotype <<lazy>>
------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Association

Tagged Values
~~~~~~~~~~~~~~

**laziness**
    String


UML:Stereotype <<ordered>>
---------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Association

Tagged Values
~~~~~~~~~~~~~~

**order_by**
    String


