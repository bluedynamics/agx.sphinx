AGX Overview
============

This document shows an overview of package dependencies and the recent
AGX configuration.

It's a good starting point when writing generators and handlers to figure out
the right place for your stuff.

AGX Package Dependencies
------------------------

**Legend**:

.. graphviz::

    digraph depslegend {
        size = "5,1";
        
        "nonagx" [style="filled", fillcolor="grey90", label="Non AGX", shape="record"];
        "core" [style="filled", fillcolor="pink2", label="Core", shape="record"];
        "io" [style="filled", fillcolor="palegreen3", label="IO", shape="record"];
        "transform" [style="filled", fillcolor="lightskyblue3", label="Transform", shape="record"];
        "generator" [style="filled", fillcolor="tan2", label="Generator", shape="record"];
        "flavour" [style="filled", fillcolor="yellow2", label="Flavour", shape="record"];
    }

**Diagram**:

.. graphviz::

    digraph dependencies {
        size = "9,9"
        
        "lxml" [style="filled", fillcolor="grey90", label="lxml", shape="Mrecord"];
        "uuid" [style="filled", fillcolor="grey90", label="uuid", shape="Mrecord"];
        "odict" [style="filled", fillcolor="grey90", label="odict", shape="Mrecord"];
        "node" [style="filled", fillcolor="grey90", label="node", shape="Mrecord"];
        "Chameleon" [style="filled", fillcolor="grey90", label="Chameleon", shape="Mrecord"];
        "Jinja2" [style="filled", fillcolor="grey90", label="Jinja2", shape="Mrecord"];
        
        "zope.location" [style="filled", fillcolor="grey90", label="zope.location", shape="Mrecord"];
        "zope.configuration" [style="filled", fillcolor="grey90", label="zope.configuration", shape="Mrecord"];
        "zope.lifecycleevent" [style="filled", fillcolor="grey90", label="zope.lifecycleevent", shape="Mrecord"];
        "zope.documenttemplate" [style="filled", fillcolor="grey90", label="zope.documenttemplate", shape="Mrecord"];
        
        "agx.core" [style="filled", fillcolor="pink2", label="agx.core", shape="Mrecord"];
        
        "node.ext.directory" [style="filled", fillcolor="palegreen3", label="node.ext.directory", shape="Mrecord"];
        "node.ext.python" [style="filled", fillcolor="palegreen3", label="node.ext.directory", shape="Mrecord"];
        "node.ext.template" [style="filled", fillcolor="palegreen3", label="node.ext.template", shape="Mrecord"];
        "node.ext.uml" [style="filled", fillcolor="palegreen3", label="node.ext.uml", shape="Mrecord"];
        "node.ext.xml" [style="filled", fillcolor="palegreen3", label="node.ext.xml", shape="Mrecord"];
        "node.ext.xmi" [style="filled", fillcolor="palegreen3", label="node.ext.xmi", shape="Mrecord"];
        "node.ext.zcml" [style="filled", fillcolor="palegreen3", label="node.ext.zcml", shape="Mrecord"];
        
        "agx.transform.uml2fs" [style="filled", fillcolor="lightskyblue3", label="agx.transform.uml2fs", shape="Mrecord"];
        "agx.transform.xmi2uml" [style="filled", fillcolor="lightskyblue3", label="agx.transform.xmi2uml", shape="Mrecord"];
        
        "agx.generator.uml" [style="filled", fillcolor="tan2", label="agx.generator.uml", shape="Mrecord"];
        "agx.generator.pyegg" [style="filled", fillcolor="tan2", label="agx.generator.pyegg", shape="Mrecord"];
        "agx.generator.zca" [style="filled", fillcolor="tan2", label="agx.generator.zca", shape="Mrecord"];
        "agx.generator.buildout" [style="filled", fillcolor="tan2", label="agx.generator.buildout", shape="Mrecord"];
        "agx.generator.plone" [style="filled", fillcolor="tan2", label="agx.generator.plone", shape="Mrecord"];
        "agx.generator.dexterity" [style="filled", fillcolor="tan2", label="agx.generator.dexterity", shape="Mrecord"];
        
        "agx.dev" [style="filled", fillcolor="yellow2", label="agx.dev", shape="Mrecord"];
        
        "node" -> "uuid" [arrowhead="none"];
        "node" -> "odict" [arrowhead="none"];
        "node" -> "zope.location" [arrowhead="none"];
        "node" -> "zope.lifecycleevent" [arrowhead="none"];
        
        "agx.dev" -> "agx.generator.uml" [arrowhead="none"];
        "agx.dev" -> "agx.generator.dexterity" [arrowhead="none"];
        
        "agx.core" -> "node" [arrowhead="none"];
        "agx.core" -> "zope.configuration" [arrowhead="none"];
        
        "node.ext.directory" -> "node" [arrowhead="none"];
        
        "node.ext.python" -> "node.ext.directory" [arrowhead="none"];
        
        "node.ext.template" -> "node.ext.directory" [arrowhead="none"];
        "node.ext.template" -> "zope.documenttemplate" [arrowhead="none"];
        "node.ext.template" -> "Chameleon" [arrowhead="none"];
        "node.ext.template" -> "Jinja2" [arrowhead="none"];
        
        "node.ext.uml" -> "node" [arrowhead="none"];
        
        "node.ext.xmi" -> "node.ext.xml" [arrowhead="none"];
        
        "node.ext.xml" -> "node" [arrowhead="none"];
        "node.ext.xml" -> "lxml" [arrowhead="none"];
        
        "node.ext.zcml" -> "node.ext.xml" [arrowhead="none"];
        
        "agx.transform.xmi2uml" -> "agx.core" [arrowhead="none"];
        "agx.transform.xmi2uml" -> "node.ext.xmi" [arrowhead="none"];
        "agx.transform.xmi2uml" -> "node.ext.uml" [arrowhead="none"];
        
        "agx.transform.uml2fs" -> "agx.core" [arrowhead="none"];
        "agx.transform.uml2fs" -> "node.ext.directory" [arrowhead="none"];
        
        "agx.generator.uml" -> "agx.transform.xmi2uml" [arrowhead="none"];
        
        "agx.generator.pyegg" -> "node.ext.template" [arrowhead="none"];
        "agx.generator.pyegg" -> "node.ext.python" [arrowhead="none"];
        "agx.generator.pyegg" -> "node.ext.uml" [arrowhead="none"];
        "agx.generator.pyegg" -> "agx.transform.uml2fs" [arrowhead="none"];
        
        "agx.generator.zca" -> "agx.generator.pyegg" [arrowhead="none"];
        "agx.generator.zca" -> "node.ext.zcml" [arrowhead="none"];
        
        "agx.generator.buildout" -> "agx.generator.pyegg" [arrowhead="none"];
        
        "agx.generator.plone" -> "agx.generator.zca" [arrowhead="none"];
        "agx.generator.plone" -> "agx.generator.buildout" [arrowhead="none"];
        
        "agx.generator.dexterity" -> "agx.generator.plone" [arrowhead="none"];
    }

AGX Configuration
-----------------

**Legend**:

.. graphviz::

    digraph configlegend {
        size = "5,1";
        
        "transform" [style="filled", fillcolor="lightskyblue3", label="Transform", shape="record"];
        "generator" [style="filled", fillcolor="pink2", label="Generator", shape="record"];
        "targethandler" [style="filled", fillcolor="tan2", label="Target handler", shape="record"];
        "handler" [style="filled", fillcolor="palegreen3", label="Handler", shape="record"];
        "scope" [style="filled", fillcolor="yellow2", label="Scope", shape="record"];
    }

**Diagram**:

.. agxconfiggraph::
