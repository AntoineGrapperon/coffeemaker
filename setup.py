import os as _os
import shutil as _shutil
import sys as _sys

from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

LICENSE = "WTFYW"
AUTHOR = "Antoine"
EMAIL = "antoine.grapperon@gmail.com"
URL = "https://www.youtube.com/watch?v=oHg5SJYRHA0"
VERSION = '0.0.1'

class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        _bdist_wheel.finalize_options(self)
        self.root_is_pure = False


if _os.path.exists("build"):
    _shutil.rmtree("build")
if _os.path.exists("dist"):
    _shutil.rmtree("dist")

requirements = [
    "datetime",
    "dateutils",
    "pytz"
]

setup(
    name="coffeemaker",
    description="Coffee maker",
    version=VERSION,
    maintainer=AUTHOR,
    maintainer_email=EMAIL,
    license=LICENSE,
    url=URL,
    packages=[
        "coffeemaker"
    ],
    package_dir={'': 'src'},
    install_requires=requirements,
    cmdclass={"bdist_wheel": bdist_wheel},
    zip_safe=False,
    include_package_data=True,
)