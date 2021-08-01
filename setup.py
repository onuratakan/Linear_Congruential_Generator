from setuptools import setup

setup(name='Linear_Congruential_Generator',
version='0.1.4',
description="""The random number generator.
""",
long_description="""
# Linear Congruential Generator | ![Made_with_python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg) ![Licence](https://img.shields.io/github/license/onuratakan/Linear_Congruential_Generator.svg)

# Installing
```console
pip install Linear-Congruential-Generator
```

# Import
```python
from lcg import LCG
```
""",
long_description_content_type='text/markdown',
url='https://github.com/onuratakan/LCG',
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
packages=["lcg"],
package_dir={'':'src'},
python_requires='>=3',
zip_safe=False)