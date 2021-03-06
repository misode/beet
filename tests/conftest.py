from pathlib import Path

from pytest_insta import Fmt

from beet import DataPack, ResourcePack


class FmtResourcePack(Fmt[ResourcePack]):
    extension = ".resource_pack"

    def load(self, path: Path) -> ResourcePack:
        return ResourcePack(path=next(path.iterdir()))

    def dump(self, path: Path, value: ResourcePack):
        value.save(path, overwrite=True)


class FmtDataPack(Fmt[DataPack]):
    extension = ".data_pack"

    def load(self, path: Path) -> DataPack:
        return DataPack(path=next(path.iterdir()))

    def dump(self, path: Path, value: DataPack):
        value.save(path, overwrite=True)
