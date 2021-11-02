# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyMinc2Simple(CMakePackage, PythonPackage):
    """Simple interface to libminc"""

    homepage = "https://github.com/NIST-MNI/minc2-simple"
    git      = "https://github.com/NIST-MNI/minc2-simple.git"

    version('2021-05-11', commit="6382802dd6e3f712d394c7d708281d05b7e9a82b")

    phases = ['cmake', 'build', 'python_build', 'install', 'python_install']

    depends_on('minc-toolkit')
    depends_on('py-cffi')
    depends_on('py-numpy')
    depends_on('py-six')

    def python_build(self, spec, prefix):
        self._build_directory = 'python'
        PythonPackage.build_ext(self, spec, prefix)

    def python_install(self, spec, prefix):
        PythonPackage.install(self, spec, prefix)

    def setup_py(self, *args, **kwargs):
        setup = self.setup_file()

        self.python('-s', join_path("python", setup), '--no-user-cfg', *args, **kwargs)
