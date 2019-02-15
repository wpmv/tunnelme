===========
Development
===========

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

Get Started!
------------

Here's how to set up `tunnel_utils` for local development.

1. Clone the `tunnel_utils` repository from GitLab::

    $ git clone git@git.ent.tds.net:usrolh/tunnel-utils.git

2. Install your local copy into a virtualenv. Many virtualenv management
   solutions exist, so use whatever you prefer. Assuming you have
   virtualenvwrapper installed, this is how you set up your fork for local
   development::

    $ mkvirtualenv dev-tunnel-utils
    $ cd tunnel-utils/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox::

    $ pytest
    $ prospector
    $ tox     # to test other python versions

6. Commit your changes and push your branch to Gitlab::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a merge request through the Gitlab website.


Dependencies
------------

This project uses pip-tools to help pin dependancies to specific versions. Install pip-tools into your virtualenv like so:::

    pip install --upgrade pip
    pip install --upgrade pip-tools

Requirements for the package to function are read into ``setup.py`` from the
file ``requirements/main.in`` (unversioned), and pinned in
``requirements/main.txt``.

Requirements for development, continuous integration, and testing are listed in
``requirements/dev.in`` (unversioned), and pinned in ``requirements/dev.txt``.
There is some rudimentary support for pytest in ``setup.py``'s tests_require,
but running pytest that way is not recommended.

When you update one of the ``requirements/*.in`` files, run the following for
``main.in``::

    pip-compile requirements/main.in

or, for ``dev.in``::

    pip-compile requirements/dev.in

To sync requirements, deleting unused packages and installing pinned versions::

    pip-sync requirements/*.txt

After a sync, depending on your development style, you may need to install the
local package again in development mode::

    pip install -e .

or::

    python setup.py develop

Merge Request Guidelines
------------------------

Before you submit a merge request, check that it meets these guidelines:

1. The merge request should include tests.
2. If the merge request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add to the api
   and prose documentation.
3. The pull request should work for Python 3.5+

Version Changes
---------------

This project's version string is managed by `bumpversion`_, a tool to manage
semantic versioning, version bump commits and tags, and similar concernts.
Running the tool will update all the places where the version is specified
(setup.py, documentation, __init__.py, etc). It's controlled by the
configuration file `.bumpversion.cfg` and a CLI tool.

This project is configured with 5 possible version levels:

* major - backwards incompatible changes
* minor - backwards compatible new features
* patch - bugfix changes
* prerel - "pre-release" level during development, a (alpha), b (beta), rc
  (release candidate) or ""
* prerelversion - "version" of the given prerel (allowing for rc1, rc2, etc)

To update the minor version::

    bumpversion --verbose minor

If the current version was ``1.1.2``, this would update the current version to
``1.2.0a0``. Note that updating one level zeros out the levels below it. This
would also make a git commit and a git tag for the version bump.

You can specify the new version with the ``--new-version`` flag::

   bumpversion --verbose --new-version 1.2.3 minor

You can verify what is going to happen with the ``--dry-run`` flag::

   bumpversion --verbose --dry-run minor

.. _`bumpversion`: https://github.com/peritus/bumpversion

Tips
----

To run a subset of tests::

    $ pytest -k <some test keyword>

Consult the pytest documentation for details on including and excluding tests.
