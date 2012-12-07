==================================
Dexterity Content Types for Plone
==================================

.. note:: Experienced developers can head right over to :ref:`profile_dexterity`

See the
`Dexterity Developer Manual <http://dexterity-developer-manual.readthedocs.org/>`_
for a reference on dexterity.


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

