# pado-tcga

[![PyPI Version](https://img.shields.io/pypi/v/pado-tcga)](https://pypi.org/project/pado-tcga/)
[![Read the Docs](https://img.shields.io/readthedocs/pado-tcga)](https://pado-tcga.readthedocs.io)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/ap--/pado-tcga/pado-tcga?label=tests)](https://github.com/ap--/pado-tcga/actions)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pado-tcga)](https://github.com/ap--/pado-tcga)
[![GitHub issues](https://img.shields.io/github/issues/ap--/pado-tcga)](https://github.com/ap--/pado-tcga/issues)

Pado dataset for TCGA on AWS opendata

## Documentation

To load the latest release of the pado dataset:

```python
# pip install pado s3fs requests aiohttp
import fsspec
import pado

of = fsspec.open("zip:///::https://github.com/ap--/pado-tcga/releases/latest/download/pado-tcga-dataset.zip")
ds = pado.PadoDataset(of)

print(ds.describe())
```


## Acknowledgements

Build with :heart: by Andreas Poehlmann
