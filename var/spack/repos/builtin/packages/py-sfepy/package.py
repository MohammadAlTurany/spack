# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PySfepy(PythonPackage):
    """SfePy (http://sfepy.org) is a software for solving systems of coupled
    partial differential equations (PDEs) by the finite element method in 1D,
    2D and 3D. It can be viewed both as black-box PDE solver, and as a Python
    package which can be used for building custom applications.
    """

    homepage = "http://sfepy.org"
    url      = "https://github.com/sfepy/sfepy/archive/release_2017.3.tar.gz"

    version('2017.3', '65ab606a9fe80fccf17a7eb5ab8fd025')

    variant('petsc', default=False, description='Enable PETSc support')

    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-six', type='run')
    depends_on('py-scipy', type='run')
    depends_on('py-matplotlib', type='run')
    depends_on('py-sympy', type='run')
    depends_on('hdf5+hl', type='run')
    depends_on('py-pytables', type='run')
    depends_on('py-petsc4py', type='run', when='+petsc')
