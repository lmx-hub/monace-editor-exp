import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions

for dist in get_installed_distributions():
    subprocess.call("pip install --upgrade " + dist.project_name, shell=True)