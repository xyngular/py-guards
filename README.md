![PythonSupport](https://img.shields.io/static/v1?label=python&message=%203.8|%203.9|%203.10&color=blue?style=flat-square&logo=python)
![PyPI version](https://badge.fury.io/py/guards.svg)



# Overview

Various objects that allow for sentinel-like singleton guards for various purposes, including:

- Ones pre-defined in this library:
  - Default
  - Null
- Also, Easily create your own custom singletons/sentinels types.

**[📄 Detailed Documentation](https://xyngular.github.io/py-guards/latest/)** | **[🐍 PyPi](https://pypi.org/project/guards/)**

# Install

```bash
# via pip
pip install guards

# via poetry
poetry add guards
```

# Quick Start

```python
from guards import Default
import os

def my_func(my_param = Default):
    if my_param is Default:
        # Resolve default value for parameter, otherwise None.
        my_param = os.environ.get('MY_PARAM', None)
    ...
```

# Licensing

This library is licensed under the MIT-0 License. See the LICENSE file.
