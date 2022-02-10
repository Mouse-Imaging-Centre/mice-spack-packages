# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack import *


class PyMinc2Simple(CMakePackage, PythonPackage):
    """Simple interface to libminc"""

    homepage = "https://github.com/NIST-MNI/minc2-simple"
    git      = "https://github.com/NIST-MNI/minc2-simple.git"

    version('2021-05-11', commit="6382802dd6e3f712d394c7d708281d05b7e9a82b")

    depends_on('minc-toolkit')
    depends_on('py-cffi')
    depends_on('py-numpy')
    depends_on('py-six')

    def install(self, spec, prefix):
        CMakePackage.install(self, spec, prefix)
        with working_dir('python'):
            args = std_pip_args + ['--prefix=' + self.prefix, '.']
            pip(*args)
