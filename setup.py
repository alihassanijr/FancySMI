"""
Hacked together by Ali Hassani

This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from setuptools import setup


setup(
        name="fancy-smi",
        scripts=['fancy-smi'],
        version="0.1",
        description="A colorful and clean SMI built on top of nvidia-smi.",
        long_description=open('README.md', 'r').read(),
        long_description_content_type='text/markdown',
        author="Ali Hassani",
        url="https://github.com/alihassanijr/FancySMI",
        license="Apache 2.0",
        classifiers=['Environment :: Console'],
        python_requires=">=3.6",
        install_requires=["rich"]
        )
