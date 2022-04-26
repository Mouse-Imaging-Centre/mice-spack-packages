# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPydpiper(PythonPackage):
    """Neuroimaging pipeline library/framework and pipelines"""

    homepage = "https://github.com/Mouse-Imaging-Centre/pydpiper"
    git      = "https://github.com/Mouse-Imaging-Centre/pydpiper.git"
    url = "https://github.com/Mouse-Imaging-Centre/pydpiper/archive/refs/tags/v2.0.15.tar.gz"

    maintainers = ['bcdarwin']

    version('2.0.15', commit="8d3f355ef8fda7cd73723734c0d4d2cc0f9f0e32")

    depends_on('python@3.7:')
    depends_on('py-pytest', type='build')
    depends_on('py-networkx', type=('build', 'run'))
    depends_on('py-ordered-set', type=('build', 'run'))
    depends_on('py-configargparse', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-pandas', type=('build', 'run'))
    depends_on('py-pyro4', type=('build', 'run'))
    depends_on('py-pyminc', type=('build', 'run'))
    depends_on('py-minc2-simple', type=('build', 'run'))
    depends_on('py-qbatch', type=('build', 'run'))

    depends_on('minc-toolkit +shared')
    depends_on('minc-stuffs')
