Under the hood
==============

Introducing the tree transformation framework
---------------------------------------------

Basically AGX consists of transformation processing components and a crafty I/O
concept. Latter could be used apart from tree transformation tasks as well to
read and write data.

The transformation components treat all input/output data as **tree**, making it
possible to use the chain for several usecases, like:

  * code generation
  * data exchange
  * data conversion
  * [fill in your use-case here]

The major use-case and main goal of AGX is to generate Python code from some
source, e.g. UML.

The framework is based on concepts related to the Zope Component Architecture
(ZCA) and is thus pluggable and highly customizable.

We tried to make extension work for developers as easy and as little code
expensive as possible at the same time.

Thus it's easy to write your own generators and hook them into existing
transformation chains. Extending UML models by profiles with stereotypes
and tagged values and provision of additional generators enables new behavior in
the generated code.

Naming Conventions
------------------

The packages of the agx suite are named according to their function.
There exist several namespaces which contain core components and logical groups
of components. Please follow the naming conventions when providing your own
modules.

``agx.core``
  contains all transform related components and some base implementations aimed
  to be used or derived from when providing own components.

``node.ext.*``
  packages contain concrete I/O related implementations for XML, UML,
  file-system directories, python-code, ...

``agx.transform.*``
  packages provide specific source and target tree instances for the
  transformation chain -- like ``agx.transform.xml2uml`` consumes a
  ``node.ext.xml`` tree as source and provides a ``node.ext.uml`` tree as target.

``agx.generator.*``
  packages contain specific generator logic. Mostly these are a
  bunch of registered handlers for a transformation. Thess handlers are responsible
  to read from the source tree the information given and write nodes to the
  target tree. They are called by the transformation chain.



.. _under_the_hood-components_of_transformation_chain:

Components of the transformation chain
--------------------------------------

The AGX transformation chain provided by ``agx.core`` consists of several
components. They are decoupled by ZCA.

``Controller``
  The start point is usally the ``Controller``. It loads the configuration, then
  iterates over the chain (or pipeline) of registered transformations, walking
  from one source-tree over one or more intermediate trees to the target-tree.
  For each step with each pair of source and target it calls the processor with
  source, target and transformation. The target of the first transformation is the
  source of the second and so on. The last target called is eventually persisted.

``Processor``
  Responsible to  invoke all registered ``Generator`` instances of the
  transform the ``Processor`` is working on. Generators have an execution
  order defined by dependencies. The processor takes care of those. Before a
  generator is invoked the ``TargetHandler``  is looked up and initialised with
  the target. The Generator is called with source and handler wrapped target.
  (TODO: elaborate/clarify, esp. that last sentence)

``Generator``
  It walks recursivly through the whole source tree. For each node found it

  * calls the ``TargetHandler`` with the source node and
  * invokes a ``Dispatcher`` with source node and the handler wrapped target.

``Dispatcher``
  Looks up all ``Handler`` instances registered for the current transformation
  and generator. For each Handler it

  * checks whether the source node applies to the ``Scope`` (if one is
    defined) of the handler and
  * calls the handler with the source and target node if the scope is matched.

``Handler``
  Responsible to do atomic transformation related tasks. Finally, here data may
  be transfered from source to target. I.e creation and addition of target nodes,
  copying data to specific target nodes, collecting data on ``Token`` instances
  and other required tasks.

``Token``
  For information and data exchange inside the transformation chain there exist
  objects called ``Token``. Every handler can create and set or read
  already existing tokens, which have unique names in each transformation.


Overall Process of the Pipelined Multi Pass Tree Transformation
---------------------------------------------------------------

AGX core provides a generic pipelined multi pass tree transformation. It is
based on source tree traversal and dispatch to handlers. The core itself
provides the basic toolset and logic for such a transformation. Setup,
configuration and handlers must be provided by the application using AGX.

pipelined transformations
    First process a source tree A and create target tree B from it. In the
    next iteration tree B is the source tree and new target tree C is created.

multi pass processing
    In each tree processing step one or more generators are called. Each
    generator traverses the full source tree again.

dispatched generation
    target trees are generated by prioritized handlers. Scope detection is used
    to filter handlers responsible for the currently traversed source node.

The overall process is described by the following diagram:

.. msc::

    hscale = "1.5";

    controller,processor,generator,dispatcher;

    controller->controller [ label = "initialize with path/file of source and target" ];
    controller=>controller [ label = "fetch configuration" ];
    --- [label = "iterate over transform names", textcolor="maroon",linecolor="red"];
    controller=>controller [ label = "lookup transform" ];
    controller=>controller [ label = "create source using transform" ];
    controller=>controller [ label = "if no source factored use previous target as source" ];
    controller=>controller [ label = "create target using transform and source" ];
    controller=>controller [ label = "create processor for transform" ];
    controller=>processor [ label = "process target" ];
    processor=>processor [ label = "lookup generators for transform"];
    --- [label = "iterate over generators", textcolor="olive",linecolor="green"];
    processor=>processor [ label = "lookup targethandler for generator"];
    processor=>processor [ label = "set anchor of target handler to target"];
    processor=>generator [ label = "call generator with source and target handler"];
    generator=>generator [ label = "lookup dispatcher with same name as generator" ];
    --- [label = "walk through source tree top to bottom, depth last.", textcolor="orange",linecolor="orange"];
    generator=>generator [ label = "preprocess target, call it with current source node" ];
    generator=>dispatcher [ label = "call dispatcher with source node and target handler" ];
    dispatcher=>dispatcher [ label = "look up all ordered handlers"];
    --- [label = "iterate over handlers", textcolor="purple",linecolor="fuchsia"];
    dispatcher=>dispatcher [ label = "look up scope"];
    dispatcher=>dispatcher [ label = "if scope(source) is not matched, next()"];
    dispatcher rbox dispatcher [ label = "call handler(source, target)"];
    dispatcher=>dispatcher [ label = "next()"];
    --- [label = "end iteration over handlers", textcolor="purple",linecolor="fuchsia"];
    generator<-dispatcher [ label = "dispatch done"];
    --- [label = "end walking source tree", textcolor="orange",linecolor="orange"];
    processor<-generator [ label = "generation done" ];
    processor=>processor [ label = "next"];
    --- [label = "end iteration over generators", textcolor="olive",linecolor="green"];
    controller<=processor [ label = "return target" ];
    controller=>controller [ label = "next" ];
    --- [label = "end iteration over transform names",textcolor="maroon",linecolor="red"];
    controller=>controller [ label = "persist last target" ];
