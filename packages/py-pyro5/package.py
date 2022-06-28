# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyPyro5(PythonPackage):
    """Python remote objects library"""

    homepage = "https://pyro5.readthedocs.io"
    pypi     = "Pyro5/Pyro5-5.13.1.tar.gz"

    version('5.13.1', sha256='2be9da379ae0ec4cf69ffb3c5c589b698eea00e614a9af7945b87fa9bb09baf2')

    depends_on('py-serpent', type=('build', 'run'))
