from unittest import TestCase, mock

from qgispluginreleaser.entry_point import create_zipfile


def return_metadata():
    return "metadata.txt"


class EntryPointTestCase(TestCase):
    def setUp(self):
        self.patcher = mock.patch(
            "qgispluginreleaser.entry_point.metadata_file", return_metadata
        )
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_makefile_call(self):
        with mock.patch("subprocess.call") as mocked:
            create_zipfile({})
            self.assertTrue(mocked.called)

    def test_ziprename(self):
        def mock_glob(something):
            return ["something.zip"]

        with mock.patch("subprocess.call"):
            with mock.patch("glob.glob", mock_glob):
                with mock.patch("shutil.copy") as mocked:
                    create_zipfile({"version": "1.0", "workingdir": "/tmp"})
                    mocked.assert_called_with("something.zip", "/tmp/something.1.0.zip")
