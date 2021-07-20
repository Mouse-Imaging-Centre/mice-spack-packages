# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPydpiper(PythonPackage):
    """Neuroimaging pipeline library/framework and pipelines"""

    homepage = "https://github.com/Mouse-Imaging-Centre/pydpiper"
    url = "https://github.com/Mouse-Imaging-Centre/pydpiper/archive/refs/tags/v2.0.15.tar.gz"

    maintainers = ['bcdarwin']

    version('master', branch='master')
    version('2.0.15', sha256='9c687ecc0dfaba5954300a858c952362')

    depends_on('python@3.7:')
    depends_on('py-pytest', type='build')
    depends_on('py-networkx')
    depends_on('py-ordered-set')
    depends_on('py-configargparse')
    depends_on('py-numpy')
    depends_on('py-pandas')
    depends_on('py-pyro4')
    depends_on('py-pyminc')

    depends_on('minc-toolkit +shared')
    depends_on('minc-stuffs')
