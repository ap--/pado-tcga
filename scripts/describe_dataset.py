import fsspec
import pado

of = fsspec.open("zip:///::https://github.com/ap--/pado-tcga/releases/latest/download/pado-tcga-dataset.zip")
ds = pado.PadoDataset(of)

print(ds.describe())

