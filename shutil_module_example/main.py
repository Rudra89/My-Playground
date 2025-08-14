# This code makes zip file of all files in a files folder.
# And it will name it output.zip

import shutil

shutil.make_archive("input", "zip", "shutil_module_example/files")