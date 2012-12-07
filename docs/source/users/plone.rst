.. _users_plone:

===============
Plone Products
===============

Model Products with Generic Setup Profiles for Plone.

.. note:: Experienced developers can look at the :ref:`profile_plone`


Example Model (used for tests)
-------------------------------

..  image:: model_agx-generator-plone_diagram.svg
    :scale: 50%


An these files are generated on the file system:
::

  ├── LICENSE.rst
  ├── MANIFEST.rst
  ├── README.rst
  ├── setup.py
  └── src
       └── agx
            ├── __init__.py
            └── testpackage
                 ├── __init__.py
                 ├── anothercontenttype.py
                 ├── browser.py
                 ├── browser.zcml
                 ├── browserpackage
                 │   ├── __init__.py
                 │   ├── browser.zcml
                 │   ├── configure.zcml
                 │   ├── globalview.py
                 │   └── templates
                 │       └── globalview.pt
                 ├── configure.zcml
                 ├── mycontenttype.py
                 ├── normalclassshouldnotappearinbrowserzcml.py
                 ├── profiles
                 │   ├── default
                 │   │   ├── cssregistry.xml
                 │   │   ├── jsregistry.xml
                 │   │   └── metadata.xml
                 │   └── uninstall
                 ├── profiles.zcml
                 ├── resources
                 │   ├── main.css
                 │   └── main.js
                 ├── templates
                 │   ├── dynaview.pt
                 │   ├── edit_view.pt
                 │   ├── myview_template.pt
                 │   ├── myview_view.pt
                 │   └── viewtwo.pt
                 └── viewtwo.py
