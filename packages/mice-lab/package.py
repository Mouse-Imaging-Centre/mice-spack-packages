# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class MiceLab(AutotoolsPackage, PythonPackage):
    """MICe-specific scripts"""

    homepage = "https://github.com/Mouse-Imaging-Centre/MICe-lab"
    url      = "https://github.com/Mouse-Imaging-Centre/MICe-lab/archive/refs/tags/0.18.tar.gz"

    version('0.19', sha256='5874aed4d4f2a2dd2d7ae3ab51b3743a')
    version('0.18', sha256='d95ac9ebc8f112135226ec36bda5f4d4')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('perl')
    depends_on('perl-getopt-tabular', type=('build', 'run'))
    depends_on('perl-mni-perllib', type=('build', 'run'))
    depends_on('minc-toolkit', type=('build', 'run'))
    depends_on('py-pyminc', type=('build', 'run'))
    depends_on('py-pydpiper', type=('build', 'run'))
    depends_on('opencv +python3 +python_bindings_generator', type=('build', 'run'))

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--verbose', '--force')

    @run_after('install')
    def python_install(self):
        PythonPackage.install(self, self.spec, self.prefix)

    # is this needed?
    def setup_py(self, *args, **kwargs):
        setup = self.setup_file()
        self.python('-s', setup, '--no-user-cfg', *args, **kwargs)
