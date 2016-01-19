qgispluginreleaser
==========================================

Add-on for zest.releaser for releasing qgis plugins.

Zest.releaser can be extended, see its `entrypoints documentation
<http://zestreleaser.readthedocs.org/en/latest/entrypoints.html>`_.

We want to hook into the "release" step so that we can create a zipfile with a
version number and report the zipfile's location for easy copy/pasting into
``scp`` later on.

Optional: do the "scp" directly from the plugin.
