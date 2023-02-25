import os
import shutil
from setuptools import setup
from Cython.Build import cythonize

# source and destination directories
src_dir = input('Enter path with py-files: ')
dest_dir = src_dir

# iterate over files in source directory
for filename in os.listdir(src_dir):
    if filename.endswith('.py'):  # check if file is a Python file
        src_file = os.path.join(src_dir, filename)  # create full source path
        dest_file = os.path.join(dest_dir, filename.replace('.py', '.pyx'))  # create full destination path
        shutil.copyfile(src_file, dest_file)  # copy the file with the new extension

# build .pyd files from .pyx files
extensions = cythonize(f'{dest_dir}\\*.pyx')
setup(ext_modules=extensions)
