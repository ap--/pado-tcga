"""pado_tcga.providers"""
from __future__ import annotations

import multiprocessing
import pathlib

from pado.create import create_image_provider
from pado.images.providers import ImageProvider

DATASET_BASE = pathlib.Path(__file__).parent.joinpath("dataset")


def create_tcga_image_provider() -> ImageProvider:

    ip = create_image_provider(
        "s3://tcga-2-open/",
        "**/*.svs",
        output_urlpath=DATASET_BASE,
        identifier="tcga",
        checksum=True,
        resume=False,
        ignore_broken=True,
        progress=True,
        workers=max(1, multiprocessing.cpu_count()),
        search_storage_options={"anon": True},
        output_storage_options=None,
    )
    return ip


if __name__ == "__main__":
    create_tcga_image_provider()
