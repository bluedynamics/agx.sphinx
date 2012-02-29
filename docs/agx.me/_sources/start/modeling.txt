===============================
About the Model Driven Approach
===============================

AGX uses models to generate software from them. This approach is widely spread
in other programming languages like Java or C++. Python is suited well too for 
the model driven approach.

    Model-driven engineering (MDE) is a software development methodology which 
    focuses on creating models, or abstractions, more close to some particular 
    domain concepts rather than computing (or algorithmic) concepts. It is meant 
    to increase productivity by maximizing compatibility between systems, 
    simplifying the process of design, and promoting communication between 
    individuals and teams working on the system.
    
    from Wikipedia at 2010-07-20 
    `Model-driven engineering <http://en.wikipedia.org/wiki/Model_Driven_Software_Development>`_ 

While AGX aims to be generic in its architecture it currently supports only 
UML - the Unified Modeling Language - for its source models. It is a 
graphical language designed to describe software through diagrams. There are 
several different types of diagrams available, but at the moment AGX uses only 
class-diagrams.

AGX can be extended by using profiles and matching generators. Each profile defines 
a set of features and contains a UML profile loadable in any modern UML 
modeling tool. It also contains AGX generators bound to the scope of the profile 
responsible for generating Python code, structures or configuration.
