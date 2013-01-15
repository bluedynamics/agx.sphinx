===================
User Documentation
===================

This documentation is aimed at users of AGX -- people drawing UML diagrams to
generate code from it.

The chapter has an overview on modeling technology in general and also with
respect to the various generation targets that AGX features.


**Python eggs**
    are the Python equivalent to distribution packages such as
    Java Jars or Zip archives. Eggs can be installed and also declare
    dependencies to other packages and other metadata.

**Zope Component Architecture**
    The Zope Component Architecture (ZCA) is a term for modularized software.
    It came into being when
    `Zope <http://zope.org>`_,
    one of the first web application servers that had grown
    to a large monolithic beast was rewritten and split into components.

**Plone: Products with Generic Setup profiles**
    Probably the most successful content management systems running on top of
    Zope is Plone. When developing for **Plone**, you build **Products** that have
    **Generic Setup** profiles and a characteristic filesystem structure and way
    of hooking into the machinery to them.

**Dexterity**
    is the new kid on the block (not so new), ready to replace the
    older Archetype based content types. AGX can generate **Dexterity content types**
    and thus offers modern CRUD for a renown mature CMS.

**Buildout**
    is the Python equivalent of Make or Ant: repeatable installations.

**SQLAlchemy**
    While Zope (and Plone) use the ZODB -- an object database -- some applications
    are better suited for relational databases. AGX can generate code to make use
    of **SQL** databases through SQLAlchemy, an object relational mapper (**ORM**).

**Generator**
    As special feature, the **Generator** can be used to generate its own code.
    Stay tuned!


.. toctree::
   :maxdepth: 2

   Foundations - about UML, Profiles, AGX-Generators and more <foundations>
   Import and use basic data types in the model <basic_types>
   Generating Python Eggs <pyegg>
   Buildout <buildout>
   Zope Component Architecture <zca>
   Plone (Generic Setup profiles) <plone>
   Dexterity <dexterity>
   SQL ORM <sql>
   Generator Generator <../developers/generator>


