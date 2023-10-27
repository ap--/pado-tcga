# pado-tcga

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
