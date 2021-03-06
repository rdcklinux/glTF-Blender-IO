# This file copy documentation into local svn repo
# in order to update online doc on blender server
# Example:
# copy_doc -r /home/<user>/blender_docs/

import argparse
import shutil
from os.path import isfile, isdir, dirname, realpath
from os import listdir

ap = argparse.ArgumentParser()
ap.add_argument("-r", "--repo", required=True, help="repo path")
args = vars(ap.parse_args())

doc = dirname(realpath(__file__)) + "/../docs/blender_docs/io_gltf2.rst"
images = dirname(realpath(__file__)) + "/../images/"

if not isdir(args["repo"]):
    sys.exit()

shutil.copy(doc, args["repo"] + "/manual/addons/io_gltf2.rst")

images_list = listdir(images)
for img in images_list:
    if not isfile(images + img):
        continue
    shutil.copy(images + img, args["repo"] + "/manual/images/" + img)
