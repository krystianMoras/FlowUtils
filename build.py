from setuptools import Extension
from setuptools.command.build_ext import build_ext
import setuptools.errors
import numpy as np  # NumPy is needed to build C extensions
ext_modules = [
    Extension(
    'flowutils.logicle_c',
    sources=[
        'src/flowutils/logicle_c_ext/_logicle.c',
        'src/flowutils/logicle_c_ext/logicle.c'
    ],
    include_dirs=[np.get_include(), 'src/flowutils/logicle_c_ext'],
    extra_compile_args=['-std=c99']
),Extension(
    'flowutils.gating_c',
    sources=[
        'src/flowutils/gating_c_ext/_gate_helpers.c',
        'src/flowutils/gating_c_ext/gate_helpers.c'
    ],
    include_dirs=[np.get_include(), 'src/flowutils/gating_c_ext'],
    extra_compile_args=['-std=c99']
)
]


class BuildFailed(Exception):
    pass


class ExtBuilder(build_ext):

    def run(self):
        try:
            print("success")
            build_ext.run(self)
        except:
            raise BuildFailed('File not found. Could not compile C extension.')

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except:
            raise BuildFailed('Could not compile C extension.')


def build(setup_kwargs):
    """
    This function is mandatory in order to build the extensions.
    """
    setup_kwargs.update(
        {"ext_modules": ext_modules, "cmdclass": {"build_ext": ExtBuilder}}
    )
