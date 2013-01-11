.. AGX documentation master file


.. image:: _static/agx.png


=======================================
Code-Generation and Tree-Transformation
=======================================

.. note::

    AGX and this documentation are **alpha**. In alpha phase things are not 
    complete. We appreciate any contribution: in code, documentation or just by 
    trying it and reporting problems. Contact `developers <dev@agx.me>`_ to get 
    involved.

AGX transforms trees of information. It was intended to generate Python code 
from UML2 diagrams.

Its generic core is a framework to convert or transform any data 
source tree into any data target tree. Its generic model of pipelined
multi-pass transformations allows to solve complex source based tasks of 
data-transformation.

AGX roots date back to the code-generator ArchGenXML (from 2003). It is also its
successor. AGX is a complete rewrite with lessons learned and in no way
compatible with the old code-generator. AGX itself is written in Python.


.. toctree::
   :maxdepth: 2
   
   Getting Started <start/index>
   User Documentation <users/index>
   Profile Reference <profiles/index.rst>
   Developer Documentation <developers/index>


.. toctree::
   :hidden:

   imprint


Legal see :doc:`imprint`.
