# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class MiceLab(AutotoolsPackage, PythonPackage):
    """MICe-specific scripts"""

    homepage = "https://github.com/Mouse-Imaging-Centre/MICe-lab"
    url      = "https://github.com/Mouse-Imaging-Centre/MICe-lab/archive/refs/tags/0.18.tar.gz"

    version('0.18', sha256='d95ac9ebc8f112135226ec36bda5f4d4')

    phases = ['autoreconf', 'configure', 'build', 'python_build', 'install', 'python_install']

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('perl')
    depends_on('minc-toolkit')
    depends_on('py-pyminc')
    depends_on('py-pydpiper')
    depends_on('opencv +python3 +python_bindings_generator')

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
