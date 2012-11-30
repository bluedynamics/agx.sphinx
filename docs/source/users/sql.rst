===========
SQL Alchemy
===========


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


Example Model (used for tests)
-------------------------------

.. image:: model_agx-generator-sql_example.svg
   :scale: 50%


Filesystem representation:
::
 agx.generator.sql-sample
  ├── LICENSE.rst
  ├── MANIFEST.rst
  ├── README.rst
  ├── setup.py
  └── src
       └── agx
            ├── __init__.py
            └── testpackage
                 ├── __init__.py
                 └── sql
                      ├── __init__.py
                      ├── company.py
                      └── personal.py

The interesting bits are in personal.py:

.. code-block:: python

  # -*- coding: utf-8 -*-

  from sqlalchemy.orm import relationship
  from sqlalchemy import (
      Column,
      Integer,
      String,
      ForeignKey,
  )
  from sqlalchemy.ext.declarative import declarative_base

  Base = declarative_base()


  class Person(Base):

      __tablename__ = 'person'
      firstname = Column(String)
      lastname = Column(String)
      id = Column(Integer, index=True, primary_key=True)
      addresses = relationship(
          'Address', backref='person',
          primaryjoin='Address.person_id==Person.id')


  class Address(Base):

      __tablename__ = 'address'
      street = Column(String)
      city = Column(String)
      country = Column(String)
      zip = Column(String)
      id = Column(Integer, index=True, primary_key=True)
      person_id = Column(Integer, ForeignKey('person.id'), nullable=False)
