======================
UML:Profile dexterity
======================

This document describes the AGX Dexterity UML profile.

Overview
---------

.. image:: profile_dexterity.png
   :scale: 50%


UML:Stereotype <<python>>
---------------------------

Metaclasses
~~~~~~~~~~~~

- UML:Class

Tagged Values**
~~~~~~~~~~~~~~~~

**None**


UML:Stereotype <<xml>>
------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values**
~~~~~~~~~~~~~~~~

**None**: 


UML:Stereotype <<behaviour_basic>>
------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values**
~~~~~~~~~~~~~~~~

**None**: 


UML:Stereotype <<behaviour_categorization>>
---------------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values**
~~~~~~~~~~~~~~~~

**None**: 


UML:Stereotype <<behaviour_publication>>
------------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values**
~~~~~~~~~~~~~~~~

**None**: 


UML:Stereotype <<behaviour_ownership>>
----------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values**
~~~~~~~~~~~~~~~~

**None**: 


UML:Stereotype <<behaviour_dublincore>>
-----------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values**
~~~~~~~~~~~~~~~~

**None**: 


UML:Stereotype <<behaviour_namefromtitle>>
--------------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values**
~~~~~~~~~~~~~~~~

**None**: 


UML:Stereotype <<behaviour_relateditems>>
-------------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values**
~~~~~~~~~~~~~~~~

**None**: 


UML:Stereotype <<behaviour_standard>>
---------------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class

Tagged Values**
~~~~~~~~~~~~~~~~

**None**: 


UML:Stereotype <<behaviour>>
------------------------------

Metaclasses
~~~~~~~~~~~~
- UML:Class
- UML:Dependency

Tagged Values**
~~~~~~~~~~~~~~~~

**marker**: 
    String: marker name.


UML:Stereotype <<Choice>>
--------------------------

XXX explain me.

Metaclasses
~~~~~~~~~~~~
**None**

Tagged Values**
~~~~~~~~~~~~~~~~

**None**


UML:Stereotype <<RelationChoice>>
----------------------------------
XXX explain me.

Metaclasses
~~~~~~~~~~~~
**None**

Tagged Values**
~~~~~~~~~~~~~~~~

**None**


UML:Stereotype <<RelationList>>
--------------------------------
XXX explain me.

Metaclasses
~~~~~~~~~~~~
**None**

Tagged Values**
~~~~~~~~~~~~~~~~

**None**


UML:Stereotype <<ICollection>>
-------------------------------
Generalized interface class for Collections.
See the following four stereotypes for specializations.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**value_type**
    String: type of values in this collection.


UML:Stereotype <<Tuple>>
-------------------------
Specialization of ICollection, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<List>>
------------------------
Specialization of ICollection, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Set>>
-----------------------
Specialization of ICollection, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Frozenset>>
-----------------------------
Specialization of ICollection, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<IMinMaxLength>>
---------------------------------
Generalized interface class for minimum and maximum length specifications.
See the following eleven stereotypes for specializations.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**min_length**
    Integer: the minimum length.

**max_length**
    Integer: the maximum length.


UML:Stereotype <<SourceText>>
------------------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Bytes>>
-------------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<ASCII>>
-------------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<DottedName>>
------------------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<BytesLine>>
-----------------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<URI>>
-----------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<ASCIILine>>
-----------------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Id>>
----------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Text>>
------------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<TextLine>>
----------------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Password>>
----------------------------
Specialization of IMinMaxLen, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**



UML:Stereotype <<IDict>>
-------------------------
Generalized interface class for dictionaries.
See the following stereotype for specializations.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**key_type**
    String: the key type.

**value_type**
    String: the value type.


UML:Stereotype <<Dict>>
------------------------
Specialization of IDict, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**



UML:Stereotype <<IField>>
--------------------------
Generalized interface class for field types.
See the following stereotypes for specializations.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**title**
    String: the title.

**description**
    String: the descripton.

**required**
    Boolean: Is this field required?

**readonly**
   Boolean: may the value not be changed?

**default**
   String: the default content.


UML:Stereotype <<Bool>>
------------------------
Specialization of IField, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<InterfaceField>>
----------------------------------
Specialization of IField, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<NamedField>>
------------------------------
Specialization of IField, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Relation>>
----------------------------
Relation with some other content.

Specialization of IField, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<NamedImage>>
------------------------------
Image with a name.

Specialization of IField, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<NamedBlobFile>>
---------------------------------
File with a name.

Specialization of IField, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<NamedBlobImage>>
----------------------------------
Named Image, to be stored outside the ZODB.

Specialization of IField, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<IRichText>>
-----------------------------
Specialization of IField, see above.

Generalized interface class for RichText fields.
See the following stereotype for a specialization.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**default_mime_type**
    String: the default mime type.

**output_mime_type**
    String: the mime type for output.

**allowed_mime_types**
   String: the set of allowed mime types.


UML:Stereotype <<RichText>>
----------------------------
Specialization of IRichText, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<IMinMax>>
-----------------------------
Specialization of IField, see above.

Generalized interface class for fields with a mimimum and maximum.
See the following stereotype for a specialization.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**min**
    String: the minimum.

**max**
    String: the maximum.


UML:Stereotype <<Int>>
------------------------
Specialization of IMinMax, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Float>>
-------------------------
Specialization of IMinMax, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Date>>
------------------------
Specialization of IMinMax, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Datetime>>
----------------------------
Specialization of IMinMax, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Timedelta>>
-----------------------------
Specialization of IMinMax, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


UML:Stereotype <<Decimal>>
---------------------------
Specialization of IMinMax, see above.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**None**


.. _st_IObject:

UML:Stereotype <<IObject>>
-----------------------------
Specialization of IField, see above.

Generalized interface class for objects.
See the following stereotype for a specialization.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
**schema**
    String: the schema.


UML:Stereotype <<Object>>
--------------------------
Specialization of :ref:`st_IObject`.

Metaclasses
~~~~~~~~~~~~
- UML:Property

Tagged Values**
~~~~~~~~~~~~~~~~
see :ref:`st_IObject`.




Example Model (used for tests)
-------------------------------

.. image:: model_agx-generator-dexterity_example.svg
   :scale: 50%

The model contails a package with stereotypes **pyegg**, **gsprofile** and
**plone_self_contained** so we can expect the generation of a buildout for
Plone with an egg containing a plugin (Plone Product) with a Generic Setup
profile.


Here is the equivalent representation on the file system (after generation):
::

  agx.generator.dexterity-sample
   ├── LICENSE.rst
   ├── MANIFEST.rst
   ├── README.rst
   ├── bootstrap.py
   ├── buildout.cfg
   ├── setup.py
   └── src
       └── agx
            ├── __init__.py
            └── testpackage
                 ├── __init__.py
                 ├── browser.zcml
                 ├── configure.zcml
                 ├── content
                 │   ├── __init__.py
                 │   ├── address.py
                 │   ├── browser.zcml
                 │   ├── company.py
                 │   ├── configure.zcml
                 │   ├── department.py
                 │   ├── person.py
                 │   ├── personview.py
                 │   └── templates
                 │       ├── company.pt
                 │       ├── department.pt
                 │       ├── person.pt
                 │       └── personview.pt
                 ├── profiles
                 │   ├── default
                 │   │   ├── cssregistry.xml
                 │   │   ├── jsregistry.xml
                 │   │   ├── metadata.xml
                 │   │   ├── types
                 │   │   │   ├── agx.testpackage.content.company.xml
                 │   │   │   ├── agx.testpackage.content.department.xml
                 │   │   │   └── agx.testpackage.content.person.xml
                 │   │   └── types.xml
                 │   └── uninstall
                 ├── profiles.zcml
                 └── resources
                     ├── company_icon.png
                     ├── department_icon.png
                     ├── main.css
                     ├── main.js
                     └── person_icon.png

