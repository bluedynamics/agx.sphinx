====================================================
Foundations - UML, Profiles, AGX-Generators and more
====================================================

UML - the Unified Modeling Language
===================================

UML (Unified Modelling Language) is a graphical language designed to 
describe software systems visually through diagrams. There are several different types of 
diagrams available, but at the moment AGX version 3 uses only class-diagrams.

ArchGenXML (versions 1 and 2), the predecessor of AGX, was able to use both 
class diagrams and state machine diagrams. Its sole purpose was 
to generate Products (= plugins) for the Plone Content Management System, 
where class diagrams would be translated to content types 
while state machines were used to generate workflow states and transitions
of content types for Plone. When it is finished, AGX v.3 will be 
a multi-purpose tool.

Class diagrams can be used to draw packages (python packages or modules), 
classes (python-classes) and as well its properties (attributes) and 
operations (methods) on these. In addition, associations in the diagram show 
how objects are aggregated within or referenced from one another.

The goal of model-driven development is to create the "blueprints" for your 
software in a well-defined, easily-communicated format: the UML model and 
diagram thereof. You can design your model using visual tools until you have a 
structure which adequately represents your needs. AGX will generate the 
necessary code. 

You probably have to customize that code somewhat, filling in method bodies, 
creating additional web-templates for your framework of choice etc., but AGX 
takes care of all the boilerplate for you.

With tagged values and stereotypes you can customize the generated code with a 
surprising degree of flexibility and control. When you need to hand-code 
something, AGX keeps your code if you follow some simple rules, 
i.e. use predefined slots for your modifications.

This manual is not aimed at teaching you UML and object-oriented, model-driven 
software development. There are several other fine manuals about that on the 
web. A very good starting point is the 
`OMG UML Resource Page <http://www.uml.org/>`_ including its web-links to 
tutorials. For a quick-start reading 
`Practical UML <http://edn.embarcadero.com/article/31863>`_ helps.

UML Profiles
============

AGX makes use of UML2 and its profiles. 

    A profile in the Unified Modeling Language (UML) provides a generic
    extension mechanism for customizing UML models for particular domains and 
    platforms. Extension mechanisms allow refining standard semantics in 
    strictly additive manner, so that they can't contradict standard semantics.
    
    Profiles are defined using stereotypes, tag definitions, and constraints 
    that are applied to specific model elements, such as Classes, Attributes, 
    Operations, and Activities. A Profile is a collection of such extensions 
    that collectively customize UML for a particular domain. 
    
    from Wikipedia at 2010-07-08 
    `Profile (UML) <http://en.wikipedia.org/wiki/Profile_%28UML%29>`_ 
                

AGX provides a specific profile for each generator package. The ``pyegg`` 
profile for example contains support for packages, modules, decorators etc. 
by providing stereotypes and tagged values.

AGX is extensible: Each generator addresses one specific domain and 
provides a profile for this domain. Generators and profiles may depend on a more 
basic domain, e.g. the ZCA-generator (Zope Component Architecture) extends the 
pyegg-generator.

How does it work?
=================

While creating a UML model the author applies desired domain specific profiles. 
Through profiles available stereotypes and tagged values for the domain are provided.
After creating a diagram with domain specific information set on the elements
AGX is invoked and code is generated.

While AGX is running, domain specific generators are working in sequence.
Each generator reads the same source tree and writes to the same target tree, 
i.e. from a UML model to a tree of files. A domain specific generator could be 
for Python eggs, Zope Component Architecture with its ZCML configuration, 
GenericSetup profiles, Django specific profiles or any other framework or
puropse, like buildout.

Each generator extends or modifies the target tree to fit it's needs. During
the whole transformation process the target tree is held in memory. After the
generators have done their work, the target tree dumps the data to the file system. 
For more information about the generation process see section 
:doc:`/developers/under_the_hood`.
