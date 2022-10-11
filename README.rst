Hello Sphinx
============

Getting started in technical writing with Sphinx and VS Code (under Windows).


Lecture 1/3: Authoring 4coders with Sphinx+VS-code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Duration: 90min

Assignment A1: Write a protocol of a meeting as html file
---------------------------------------------------------

Procedure

* Create an empty folder on your harddisk. E.g. ``hello-sphinx``
* Start a Terminal in that folder.
* Initialize a git repository there.
* In repository root folder create empty file ``.gitignore``
* Create a subfolder ``docs``
* Change cwd (current working directoryx) to ``docs``
* Create an empty file ``index.rst``
* Open the root folder of the repository in visual studio code ("code").
* Use code to write "I did something for Akshit." in that file.
* Add ``build/`` to file ``.gitignore``
* In Terminal make sure that cwd is the root folder of the repo. Execute command line ``sphinx-build docs build/html`` **(1)**

Solutions to problems

* In Terminal execute command line ``pipenv install sphinx``
* In Terminal execute command line ``pipenv shell``
* Create an empty file ``conf.py`` in folder ``docs``

Resume procedure

* Re-do **(1)**
* Open the file build/index.html in your browser.
* Tell us what you see.
* Open an other tab in your browser
* Browse to https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
* Pimp your protocol by ...

   * a chapter resp. heading
   * at least two paragraphs
   * some words written in bolt
   * some words written in italic letters
   * another chapter with a subchapter

Make your life easier and use sphinx-autobuild:

* In Terminal, make sure that cwd is root of repository. Execute command line ``pipenv install sphinx-autobuild``
* Make sure that you are still in a pipenv shell.
* In Terminal, make sure that cwd is root of repository. Execute command line ``sphinx-autobuild docs build/html``
* Look carefully in the console's output. There is some url http://127.0.0.1:8000 . Click on that url which will open that url your browser.

Tell us what you see.

Assignment A2: Create protocol in PDF format
--------------------------------------------

Procedure

* In Terminal, cwd is root of repo, execute command ``rst2pdf docs/index.rst`` **(2)**

Solutions to problems

* In Terminal execute command line ``pipenv install rst2pdf``

Resume procedure

* Re-run  **(2)**
* In a file explorer double-click file ``build/index.pdf``

Tell us what you see.

Assignment A3: Create a high-quality PDF document
-------------------------------------------------

Procedure

* In Terminal make sure that cwd is the root folder of the repo. Execute command line ``sphinx-build -b latex docs build/latex``
* Execute command line ``make --directory build/latex`` **(3)**

Solutions to problems

* In Terminal (cwd does not matter) execute command line ``scoop install miktex``
* In Terminal execute command line ``miktex-console``
* In GUI "MikTeX Console" do:
  
  * Select Updates on the left
  * Press button ``Change...`` on the right of ``Retrieve from:``

    * Select ``Local package repository (file system)``
    * Press button ``Next``
    * Press button ``Browse...`` and browse to on corporate premises where the miktex repository is mirrored. **(4)**
    * Press button ``Finish``
    * Close GUI "MikTeX Console"

*  In Terminal (cwd does not matter) execute command line ``scoop install make``

Resume procedure

* Rerun **(3)**
* Open file ``build/latex/python.pdf``

Tell us what you see.

.. note:: xxthunder is happy to help you to find that folder in **(4)**. 

Assignment A4: Make using sphinx inside VScode comfortable
----------------------------------------------------------

Procedure (setup)

* In Terminal, cwd does not matter, execute command line:

  * ``code --install-extension lextudio.restructuredtext-pack``
  * ``code --install-extension yzane.markdown-pdf``
  * ``code --install-extension dendron.dendron-paste-image``
  
In code configure extension dendron-paste-image by doing:

* Go to **Menubar/File/Preferences/Settings**
* Search for ``paste``
* In edit line of **Paste Image: Prefix** insert

.. code-block::

    .. figure::


.. attention:: There must be one whitespace behind the two colons!

* In drop-down-list of **Paste Image: Encode Path** choose ``none``
* In edit-line of **Paste Image: Path** append ``/_figures`` so it has content

.. code-block::

    ${currentFileDir}/_figures

* Close settings-tab
 
.. note:: We favor previewing html with combination sphinx-autobuild+browser above previewing html inside VS code.

Procedure (try-it-out)

* Open your index.rst in code
* Create a screenshot and copy it to the clipboard using Shift-Windows-S
* Place the cursor at the end of index.rst at the very beginning of a new line.
* Hit Ctrl-Alt-V

Tell us what you see.

Assignment A5: Define title and copyright
-----------------------------------------

Define the title

Procedure

* In code open conf.py
* Add a line: ``project = "Hello Sphinx"``
* Save
* (Auto-)build html
* View index.html in browser
* Tell us what you see

Define the copyright

Procedure

* Add to conf.py line: ``copyright = "2022, Rumanian twins"``
* Save
* (Auto-)build html
* View ``index.html`` resp. open http://127.0.0.1:8000 in browser

Tell us what you see.

Further reading
---------------

* https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
* https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf
* https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
* https://sublime-and-sphinx-guide.readthedocs.io/en/latest/index.html
* https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/Index.html
