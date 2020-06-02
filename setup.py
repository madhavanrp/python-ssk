from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

extensions = [
    Extension("string_kernel", ["string_kernel.pyx"], include_dirs=[numpy.get_include()])
]

setup(
    # ext_modules=cythonize("ssk_kernel_c.pyx"),
    ext_modules=cythonize(extensions)
)