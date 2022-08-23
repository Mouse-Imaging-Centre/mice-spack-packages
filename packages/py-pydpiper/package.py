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

    version('2.0.19', sha256="29596140cee7e1f3e9ad5cbab40c3d90bbd4764fc515ec33426092eddae01615")
    version('2.0.18', sha256="5fec8c79978ae25e8deb4d92163b0b2b7fdc72e9")
    version('2.0.17', sha256="9a7ffaa2581cb920c96ae6d32ab7ae91a8982468")
    version('2.0.16', sha256="5283a38f3d8ae1881f49e8fb834dccb92f81acd5")
    version('2.0.15', commit="8d3f355ef8fda7cd73723734c0d4d2cc0f9f0e32")

    depends_on('python@3.7:')
    depends_on('py-pytest', type='build')
    depends_on('py-networkx', type=('build', 'run'))
    depends_on('py-ordered-set', type=('build', 'run'))
    depends_on('py-configargparse', type=('build', 'run'))
    depends_on('py-jinja2', type=('build', 'run'), when='@2.0.16:')
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-pandas', type=('build', 'run'))
    depends_on('py-pyro4', type=('build', 'run'), when='@:2.0.17')
    depends_on('py-pyro5', type=('build', 'run'), when='@2.0.18:')
    depends_on('py-simplejson', type=('build', 'run'), when='@2.0.18:')
    depends_on('py-pyminc', type=('build', 'run'))
    depends_on('py-minc2-simple', type=('build', 'run'))
    depends_on('py-qbatch', type=('build', 'run'))

    depends_on('cctools', type='run', when='@2.0.18:')
    depends_on('minc-toolkit +shared', type='run')
    depends_on('minc-stuffs', type='run')
