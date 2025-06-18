Changelog of qgispluginreleaser
===================================================


2.0.1 (2025-06-18)
------------------

- Fixed small problem in administration that prevented a pypi release.


2.0 (2025-06-18)
----------------

- Use file mode ``r`` instead of ``rU`` to support Python 3.11+.

- Updated the code on the whole to work with newer python versions (replacing
  ``pkg_resources`` with ``importlib`` for instance).

- Updated the project setup (removed buildout, added pyproject.toml, added github
  actions, added pre-commit).


1.1 (2020-05-25)
----------------

- Allow the ``metadata.txt`` to also be one subdirectory deeper.


1.0 (2017-06-20)
----------------

- Use the codecs package in conjunction with "utf8" to read and write files.


0.2 (2016-02-01)
----------------

- Qgis expects zip filenames to use a dot as name/version separator instead of
  a dash. We now create the zipfile with a dot instead.


0.1 (2016-01-19)
----------------

- Initial project structure created with nensskel.

- Changing versions in metadata.txt in the prerelease/postrelease step.

- Creating a zipfile (with version number in the filename) automatically in
  the release step. Note that you must answer "yes" to the "checkout a tag?"
  question.
