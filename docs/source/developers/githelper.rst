
Working with multiple repositories
===================================

When hacking on AGX, you have to deal with a large number of repositories in the
local agx.dev checkout directory.

The repositories are in a subfolder called **devsrc/**. To update them all the
normal  way would be quite a lot of typing and changing directories.


Githelper / igitt
------------------
To ease this process, Robert has created a tool named **githelper** or **igitt**.
You can check it out from  `rnixx' githelper repository on Github <https://github.com/rnixx/githelper>`_
and install it into your system.

Once you have done that, you can change directory to *devsrc/* and update all
repositories at once (*git pull*).
::

    igitt pull 


Find more documentation in igitt.py.
