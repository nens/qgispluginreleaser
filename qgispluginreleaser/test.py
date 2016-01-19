from unittest import TestCase
import pkg_resources


class InstallationTestCase(TestCase):

    def test_entry_point_available(self):
        entry_points = list(pkg_resources.iter_entry_points(
            group='zest.releaser.releaser.after_checkout'))
        self.assertTrue('qgispluginreleaser.extension' in str(entry_points))
