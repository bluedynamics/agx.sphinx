==============================
Using AGX on the Command Line
==============================

AGX' Eclipse plugin comes with some handy menu entries, e.g. for

 * the import of profiles
 * the generation of code from models

However, apart from the fact that Papyrus runs only in Eclipse [1]_ there is no
need to use Eclipse for code generation. In fact, all Eclipse does is call AGX.

And you can do that yourself!

.. [1] There is a standalone version of Papyrus on `www.papyrusuml.org <http://www.papyrusuml.org>`_,
       but that again is an Eclipse plugin project offering the Papyrus editor.



Call AGX without arguments
===========================

Try it! Change to the directory where you installed AGX, e.g. your workspace.
Then call **bin/agx**. 
If you call AGX without arguments, you are presented with the following information: ::

  user@host:~/$ cd workspace/agx.dev 
  user@host:~/workspace/agx.dev$ bin/agx
  CRITICAL No control flags given.
  Usage: agx UMLFILE options

  Options:
    -h, --help            show this help message and exit
    -o /target/path, --output-directory=/target/path
                          Write generated code to TARGET
    -p /path/to/profile1.uml;/path/to/profile2.uml, --profiles=/path/to/profile1.uml;/path/to/profile2.uml
                          Comma seperated Paths to profile file(s)
    -e profilename1;profilename2, --export-profiles=profilename1;profilename2
                          Comma seperated profile names to export for model
    -l, --listprofiles    List of available profiles
    -i, --info            AGX Version and flavour info.
    -d, --debug           Additional output of debug information.
    -m, --postmortem      Enable postmortem debugger.
    -t, --listtemplates   list available model templates
    -c template_name, --create=template_name
                          Create a model from a model template by name. (see
                          '-t' option)
    -s, --short           option for short machine readable messages
  user@host:~/workspace_indigo/agx.dev$ 


AGX Commandline Options
========================


Show help message (-h)
-----------------------

Calling AGX with the **-h** option (or **--help**) will simply show the information above.



List the available profiles (-l)
---------------------------------

If you want to see the list of the profiles registered with AGX,
just call AGX with the **-l** (or **--listtemplates**) option.

You will be presented with output similar to this.
(Note that "..." here shows that some part ot the path has been omitted) ::

  user@host:~/workspace_indigo/agx.dev$ bin/agx -l
  generator /.../agx.generator.generator/src/agx/generator/generator/profiles/generator.profile.uml
  sql /.../agx.generator.sql/src/agx/generator/sql/profiles/sql.profile.uml
  dexterity /.../agx.generator.dexterity/src/agx/generator/dexterity/profiles/dexterity.profile.uml
  pyegg /.../agx.generator.pyegg/src/agx/generator/pyegg/profiles/pyegg.profile.uml
  plone /.../agx.generator.plone/src/agx/generator/plone/profiles/plone.profile.uml
  buildout /.../agx.generator.buildout/src/agx/generator/buildout/profiles/buildout.profile.uml
  zca /.../agx.generator.zca/src/agx/generator/zca/profiles/zca.profile.uml


Please refer to the :ref:`user_documentation` or :ref:`profile_documentation`
to find out what the profiles can do for you.


Export profiles to the file system (-e)
----------------------------------------

If you need one or more profile files for use with a model, you can use the **-e**
or **--export-profiles** option to get the most recent version of the profile
known to AGX.


List installed versions of AGX (-i)
--------------------------------------

This option is helpful to determine which version of AGX and generators
you have installed. Just call AGX with the **-i** option to get some output
like this: ::

  AGX 3.0-dev Develop
  Installed generators:
      agx.generator.generator (7a2e81ad6bc5c3f8e5341fe4b69956962b0af363)
      agx.generator.sql (b7ce8cba845b7a8df87e4dee57fa75c900e7dc3b)
      agx.generator.dexterity (96b8b98dfde5caf74fc72273a14ac3f6b186888d)
      agx.generator.uml (206a2c00866d04ce6a47e7bcaeb0322d70e4a56a)
      agx.generator.pyegg (00b774d9884e0cbcf8cc219c3174b61cc187e5bc)
      agx.generator.plone (4edb072d6feab866e8e6f9faa432fff67e45048b)
      agx.generator.buildout (f48d57e851c20640a65ac01127da3690b340eab8)
      agx.generator.zca (75c20d271984d4edcbdd3283f2f8f1fca6365bf6)


The long hashes following the generators relate to their git version hash on
github. Append this hash to e.g. 
`this URL for agx.generator.generator <https://github.com/bluedynamics/agx.generator.generator/commit/>`_
to see the version on github.


List the available templates (-t)
----------------------------------

You can get a listing of the available templates by calling AGX with the **-t**
or **--listtemplates** option. This will yield output similar to the following:
::

  user@host:/opt/agx/agx.dev$ bin/agx -t
  sql_example: SQL Product
          A simple SQL content model with two sql_content classes.

  dexterity_product: Dexterity Product
          A vanilla Plone Dexterity model that contains the necessary
          settings for content stuff for Plone.

  python_egg: Python Egg
          A minimal Python egg model.

  plone_product: Plone Product
          A vanilla Plone model that contains the necessary settings
          for a Plone product: generic setup profile etc.
          but without content classes.

  generator_example: Generator Example
          An example model for a generator generator.
          (Advanced users only!) 

  dexterity_example: Dexterity Example
          A ready-to-run Plone Dexterity example that demonstrates
          how to model content stuff for Plone.
          Contains a set of example classes.


The listed templates can be used like in the following section.


Create a model from a template (-c)
------------------------------------

A call to AGX with the **-c** option followed by one of the template names known
to AGX will create a model from this template (i.e. .di, .notation and .uml files),
an .agx settings file and a folder called 'uml_profiles' containing the relevant
profiles, as well as a log file documenting the process.

::

  user@host:/opt/agx/agx.dev/foo$ ../bin/agx -c sql_example
  INFO  Export to target: './uml_profiles'
  INFO  Export 'sql'
  INFO  Export 'pyegg'
  user@host:/opt/agx/agx.dev/foo$ ls
  agx.core.log  model.di  model.notation  model.uml  model.uml.agx  uml_profiles
  user@host:/opt/agx/agx.dev/foo$ tree
  .
  ├── agx.core.log
  ├── model.di
  ├── model.notation
  ├── model.uml
  ├── model.uml.agx
  └── uml_profiles
      ├── pyegg.profile.uml
      └── sql.profile.uml

  1 directory, 7 files


Thus, AGX can be used almost like `paster <http://pythonpaste.org/>`_ to generate
usefull structures and files on the file system, with the added bonus of a model
so you can develop your application further.


