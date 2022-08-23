A Spack repo for some MICe-developed and -maintained software packages, some of which are of general interest to MINC users and others mostly for internal use.

# Usage

Initial setup:

1. git clone https://github.com/spack/spack.git
1. git clone https://github.com/Mouse-Imaging-Centre/mice-spack-packages.git
1. source spack/share/spack/setup-env.sh
1. configure main spack repo to point to this repo (repo-wide via `spack repo add ...` or per-env basis)
1. detect compilers: `spack compiler find --scope=site`
1. (highly recommended) detect external packages (--scope=site)
1. configure etc/spack/modules.yaml -- in particular, if using tcl modules instead of lmod (not recommended), set 'autoload: direct' or generated modulefiles won't respect Python dependencies

Building the set of packages:

1. export MY_SPACK_ENV="my-new-env-yy-mm-dd"
1. spack env create ${MY_SPACK_ENV}
1. edit `var/spack/environments/${MY_SPACK_ENV}/spack.yaml` as appropriate
1. spack env activate ${MY_SPACK_ENV}
1. spack concretize (optional)
1. spack install
1. (after running spack concretize or spack install you'll have to delete var/spack/environments/${MY_SPACK_ENV}/spack.lock after changing spack.yaml (including via `spack add`, `spack remove`, etc), and after editing a package that's successfully installed you'll have to remove the lockfile and also uninstall the package--Spack seemingly doesn't track changes to the package.py in the hash)
1. spack module lmod refresh  # generate module files (or `tcl` instead of `lmod`)
1. spack env loads -m lmod  # generate "loads" file (a shell file to be sourced)
1. convert the `loads` file to a modulefile
1. install R packages and make a module (assumes you have devtools and packrat installed e.g. as a user, from previous Spack env, Packrat env, etc.):
1. `echo 'depends_on('r-packages/<version>') >> /path/to/StdEnv.lua`
1. configure qbatch, RMINC, and Pydpiper by setting PYDPIPER_CONFIG_FILE, RMINC_BATCH_CONF, and relevant QBATCH vars (e.g. in modulefiles)
