ashell - Android shell with adbrc
==============================================

ashell provide bashrc functionality to android shell.
The rc file is in '~/.adbrc

Installation
------------
::

    pip install ashell

Useage
------
::

    ashell
    ashell -h

To install the default adbrc run
::

    ashell --print-default > ~/.adbrc

Default adbrc
-------------

The major feature of the default adbrc is to add history across sessions.
The default adbrc also contain some nice aliases and more.

Known Issues
------------
- The last command doesn't saved to the history file

Bugs
~~~~
Please report bugs, issues, feature requests, etc. on `GitHub <https://github.com/roi-meir/ashell/issues>`_.

Links
-----
* `Project home page (GitHub) <https://github.com/roi-meir/ashell>`_

License
-------
Licensed under the terms of the `MIT Licens <LICENSE.txt>`_.
