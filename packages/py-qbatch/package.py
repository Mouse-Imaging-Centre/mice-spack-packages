# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyQbatch(PythonPackage):
    """"""

    homepage = "https://github.com/pipitone/qbatch"
    #git      = "https://github.com/pipitone/qbatch"
    url = "https://github.com/pipitone/qbatch/archive/refs/tags/v2.3.tar.gz"

    maintainers = ['bcdarwin']

    version('2.3', sha256="f55337ce1ab9807deac638a506d43e219a795cbc")

    depends_on('python@3.7:')
