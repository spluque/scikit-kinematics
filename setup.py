from setuptools import setup
from skinematics import __version__


def readme():
    with open('README.rst') as f:
        return f.read()


packages = ["skinematics", "skinematics.sensors", "skinematics.simulations",
            "skinematics.utils"]
setup(
    name="scikit-kinematics",
    version=__version__,
    python_requires=">=3.5",
    packages=packages,
    include_package_data=True,
    package_data={'tests': ["*.txt", "*.csv", "*.BIN"]},
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["docutils>=0.3", "matplotlib>=2.0", "numpy>=1.13.0",
                      "pandas>=0.18", "pygame", "PyOpenGL>3.0.0",
                      "scikit-learn>=0.20.0", "scipy>=0.18", "sympy>=1.0"],
    test_suite="skinematics.tests",
    extras_require={
        "dev": ["ipython", "jupyter", "jupyter-sphinx"],
        "docs": ["jupyter-sphinx"]
      },
    # metadata for upload to PyPI
    author="Thomas Haslwanter",
    author_email="thomas.haslwanter@fh-linz.at",
    description="Python utilites for movements in 3d space",
    long_description=readme(),
    license="http://opensource.org/licenses/BSD-2-Clause",
    download_url="https://github.com/thomas-haslwanter/scikit-kinematics",
    keywords="quaterions rotations",
    url="http://work.thaslwanter.at/skinematics/html",
    classifiers=["Development Status :: 4 - Beta",
                 "Programming Language :: Python :: 3",
                 "Intended Audience :: Developers",
                 "Intended Audience :: Science/Research",
                 "License :: OSI Approved :: BSD License",
                 "Topic :: Scientific/Engineering"]
)
