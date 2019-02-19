=====
Usage
=====

Overview
--------
This package is typically meant to be used in conjunction with Cygwin to allow a quick and easy
SSH tunnel to open from your Windows PC to your WorkPC. While it might have usefulness elsewhere, the following
instructions are geared toward that single approach.

Prerequisites
-------------
- Cygwin with the following packages installed:
    - python3
    - pip
    - ssh
- SSH config_ on Cygwin for forwarding appropriate ports and tunneling via ``ssh <YOUR WORKPC>.workpc.tds.net``
- YAML file containing a digitized version of your Entrust grid card
    - Schema for the YAML file is defined in the grid_card.py_ base class. You can also use this example:

.. _grid_card.py: https://git.ent.tds.net/usrolh/tunnel-utils/blob/master/tunnel_utils/grid_card.py#L11

.. _config: https://wiki.tds.net/display/CloudTV/Configure+Cygwin+for+Work+PC

.. code-block:: yaml

    ---
    serial: "12345"
    grid:
      a: ["x", "x", "x", "x", "x"]
      b: ["x", "x", "x", "x", "x"]
      c: ["x", "x", "x", "x", "x"]
      d: ["x", "x", "x", "x", "x"]
      e: ["x", "x", "x", "x", "x"]
      f: ["x", "x", "x", "x", "x"]
      g: ["x", "x", "x", "x", "x"]
      h: ["x", "x", "x", "x", "x"]
      i: ["x", "x", "x", "x", "x"]
      j: ["x", "x", "x", "x", "x"]


Install from Git
----------------

In Cygwin, start by cloning the project to a local folder (like ``~/local/src``)

.. code-block:: bash

    $ git clone git@git.ent.tds.net:usrolh/tunnel-utils.git ~/local/src/tunnel-utils

Now simply install the project using Cygwin's instance of ``python3``

.. code-block:: bash

    $ python3 -m pip install ~/local/src/tunnel-utils

**Note**
    You may need to set up trusted hosts for the following domains if you haven't already:

    - pypi.python.org
    - pypi.org
    - files.pythonhosted.org

    You can do this in a ``pip.conf`` or on the command line using ``--trusted-host`` options.

This will create an executable in your path called ``start_tunnel``, which you can verify by calling

.. code-block:: bash

    $ start_tunnel --help



Test that it works
------------------

Before we try to set up any shortcuts or automate this, we need to make sure it works. In most cases,
that's as easy as running the command manually with the appropriate options. But **be careful**, if
you find yourself unsuccessfully running this command multiple times, you run the risk of locking out your
LDAP account, or your grid card. Best practice is to run it once (after you have ensured everything looks correct). If
that works, then great. If not, you may want to seek help before trying additional times.

With that said, you can simply test it by running the following command (substituting your details where appropriate):

.. code-block:: bash

    $ start_tunnel -h <YOUR WORKPC>.workpc.tds.net -p <YOUR WORKPC PASSWORD> -c /path/to/your/grid_card.yml

The output should look something like this:

.. code-block:: bash

    Initiating tunnel...
    Using tunnel command: 'ssh <YOUR WORKPC>.workpc.tds.net'
    Authenticating with devnull...
    Received challenge: Enter a response to the grid challenge [C1] [J2] [G1] [G5]
    Sending challenge response: 'a4gj'
    Authenticating with <YOUR WORKPC>.workpc.tds.net...
    Successfully connected!
    Opening interactive session...

    Last login: Fri Feb 13 16:57:23 2019 from devnull201.tds.net
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Only users authorized by TDS may access this system. Any use of this
    system in violation of the TDS Code of Conduct or applicable law is
    unauthorized and may constitute a violation of the federal Computer
    Fraud and Abuse Act.  TDS may monitor all use of this system without
    further notice.

    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    [userid@<YOUR WORKPC> ~]$

You are now greeted with an interactive prompt on your workpc. If you have set up your Cygwin
SSH config to forward the appropriate ports (as described above), then you should be able to use your proxy now.

**Note**

If you set your WorkPC prompt to end in something other than ``$``, you may have issues with the confirmation step.
This can be changed by modifying the ``success_prompt`` variable in the tunnel class. A future version of this code may allow
this to be changed from the command line.

Setting up a Cygwin shortcut
----------------------------

Now that you've got a working tunnel command, you may want to speed things up by creating a shortcut.
This shortcut can live on your desktop, taskbar, or even in your ``startup`` folder if you want it to run on login of your
PC.

Simply create a new shortcut in Windows, and set the location to:

.. code-block:: PowerShell

    C:\cygwin64\bin\mintty.exe -i /Cygwin-Terminal.ico /bin/bash -l -c "echo -ne '\e]0;WorkPC Tunnel\a'; start_tunnel -h <YOUR WORKPC>.workpc.tds.net -c /path/to/your/grid_card.yml -p <YOUR WORKPC PASSWORD>"

You can always spruce this up with a custom icon, or change the name of the window header as you like.