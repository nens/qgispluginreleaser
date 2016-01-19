from qgispluginreleaser.entry_point import run
from unittest import TestCase

import mock
import pkg_resources


class InstallationTestCase(TestCase):

    def test_entry_point_available(self):
        entry_points = list(pkg_resources.iter_entry_points(
            group='zest.releaser.releaser.after_checkout'))
        self.assertTrue('qgispluginreleaser.entry_point' in str(entry_points))


class EntryPointTestCase(TestCase):

    def test_makefile_call(self):
        with mock.patch('subprocess.call') as mocked:
            run({})
            self.assertTrue(mocked.called)

    def test_ziprename(self):

        def mock_glob(something):
            return ['something.zip']

        with mock.patch('subprocess.call'):
            with mock.patch('glob.glob', mock_glob):
                with mock.patch('shutil.copy') as mocked:
                    run({'version': '1.0',
                         'workingdir': '/tmp'})
                    mocked.assert_called_with(
                        'something.zip',
                        '/tmp/something-1.0.zip')
