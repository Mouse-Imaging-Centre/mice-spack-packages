# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

import os


class MincStuffs(AutotoolsPackage, PythonPackage):
    """Various scripts for working with MINC files"""

    homepage = "https://gtihub.com/Mouse-Imaging-Centre/minc-stuffs"
    url      = "https://github.com/Mouse-Imaging-Centre/minc-stuffs/archive/refs/tags/v0.1.25.tar.gz"

    maintainers = ['bcdarwin']

    version('0.1.25', sha256='9860fa84518543233cbe00aea34e66c066fe29498a82bb80417cd5d16072e8ee')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('perl')
    depends_on('minc-toolkit')
    depends_on('py-pyminc')

    phases = ['autoreconf', 'configure', 'build', 'python_build', 'install', 'python_install']

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--verbose', '--force')

    def python_build(self, spec, prefix):
        self._build_directory = 'python'
        PythonPackage.build_ext(self, spec, prefix)

    def python_install(self, spec, prefix):
        PythonPackage.install(self, spec, prefix)

    def setup_py(self, *args, **kwargs):
        setup = self.setup_file()

        self.python('-s', setup, '--no-user-cfg', *args, **kwargs)
