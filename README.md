A Spack repo for some MICe-developed and -maintained software packages, some of which are of general interest to MINC users and others mostly for internal use.

# Usage

- git clone https://github.com/spack/spack.git
- git clone <this repo>
- TODO configure main spack repo to point to this repo (repo-wide or per-env basis)
- TODO detect compilers, external packages (--scope=site)
- export SPACK_ENV="my-new-env-yy-mm-dd"
- source var/spack/setup-env.sh
- spack env create ${SPACK_ENV}
- edit var/spack/environments/${SPACK_ENV}/spack.yaml as appropriate
- spack env activate ${SPACK_ENV}
- spack concretize (optional)
- spack install
- (after running spack concretize or spack install you'll have to delete var/spack/environments/${SPACK_ENV}/spack.lock after changing spack.yaml (including via `spack add`, `spack remove`, etc), and after editing a package that's successfully installed you'll have to remove the lockfile and also uninstall the package--Spack seemingly doesn't track changes to the package.py in the hash)
- spack module lmod refresh  # generate module files
- spack env loads -m lmod -r  # generate "loads" file (a shell file to be sourced)
- convert the `loads` file to a modulefile
- edit minc-toolkit module to include LD_LIBRARY_PATH (otherwise blacklisted at the moment), needed for Pyminc to work
- install R packages and make a module (assumes you have devtools and packrat installed e.g. as a user, from previous Spack env, Packrat env, etc.):
- echo 'depends_on('r-packages/<version>') >> /path/to/StdEnv.lua
