from pybuilder.core import use_plugin, init, task

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

name = "torpedo"
default_task = "publish"


@task
def build_ami():
    pass

@init
def set_properties(project):
    project.depends_on("requests")
