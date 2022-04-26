# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPyminc(PythonPackage):
    """Python bindings to libminc"""

    pypi     = "pyminc/pyminc-0.54.tar.gz"
    homepage = "https://github.com/Mouse-Imaging-Centre/pyminc"

    maintainers = ['bcdarwin']

    version('0.55', 'c794e8bdd25852397fee7196140ae512')
    version('0.54', '44f79dc4f09781a6c8b80b1d6a58363c')

    depends_on('python@3.7:')
    depends_on('py-pytest', type='build')
    depends_on('py-parameterized', type='build')
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('minc-toolkit +shared', type='run')

