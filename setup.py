#!/usr/bin/env python
from distutils.core import setup, Extension
import numpy as np

c_emd = Extension(
    'c_emd',
    sources=['c_emd/pyemd.c',
             'c_emd/emd.c' ],
    include_dirs=['c_emd', np.get_include()],
    define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_4_API_VERSION')])

setup(
    name='emd',
    version='3.0',
    description=(
      "Accurate, efficient Earth Mover's Distance in Python."
    ),
    author='Gary Doran',
    author_email='gary.doran@case.edu',
    url='https://github.com/garydoranjr/pyemd.git',
    license="BSD compatable (see the LICENSE file)",
    packages=['emd'],
    ext_modules=[c_emd]
)
