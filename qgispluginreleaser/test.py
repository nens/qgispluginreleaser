from qgispluginreleaser.extension import run
from unittest import TestCase

import mock
import pkg_resources


class InstallationTestCase(TestCase):

    def test_entry_point_available(self):
        entry_points = list(pkg_resources.iter_entry_points(
            group='zest.releaser.releaser.after_checkout'))
        self.assertTrue('qgispluginreleaser.extension' in str(entry_points))


class EntryPointTestCase(TestCase):

    def test_makefile_call(self):
        with mock.patch('subprocess.call') as mocked:
            run({})
            self.assertTrue(mocked.called)
