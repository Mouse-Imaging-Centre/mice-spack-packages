# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyPyro4(PythonPackage):
    """Python remote objects library"""

    homepage = "https://pyro4.readthedocs.io"
    pypi     = "Pyro4/Pyro4-4.80.tar.gz"

    version('4.80', sha256='46847ca703de3f483fbd0b2d22622f36eff03e6ef7ec7704d4ecaa3964cb2220')
