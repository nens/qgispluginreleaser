import glob
import os
import shutil
import subprocess


def prerequisites_ok():
    if os.path.exists('metadata.txt'):
        if 'qgisMinimumVersion' in open('metadata.txt').read():
            return True


def create_zipfile(context):
    """This is the actual zest.releaser entry point

    Relevant items in the context dict:

    name
        Name of the project being released

    tagdir
        Directory where the tag checkout is placed (*if* a tag
        checkout has been made)

    version
        Version we're releasing

    workingdir
        Original working directory

    """
    if not prerequisites_ok():
        return
    # Create a zipfile.
    subprocess.call(['make', 'zip'])
    for zipfile in glob.glob('*.zip'):
        first_part = zipfile.split('.')[0]
        new_name = "%s-%s.zip" % (first_part, context['version'])
        target = os.path.join(context['workingdir'], new_name)
        shutil.copy(zipfile, target)
        print("Copied %s to %s" % (zipfile, target))
