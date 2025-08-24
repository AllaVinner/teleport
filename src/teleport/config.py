from __future__ import annotations
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError
import toml

from teleport.context import Platform, get_context
from teleport.exceptions import TeleportException


CONFIG_FILE_NAME = ".dotman.toml"

DestinationPath = str
DestinationName = str


class DestinationConfig(BaseModel):
    links: dict[Platform, DestinationPath]


class TeleportConfig(BaseModel):
    destinations: dict[DestinationName, DestinationPath | DestinationConfig] = Field(
        default_factory=lambda: dict()
    )

    @staticmethod
    def get_config_path():
        context = get_context()
        dotfile_map = {
            Platform.linux: Path(context.home, ".config/teleport/teleport.toml"),
            Platform.mac: Path(context.home, ".config/teleport/teleport.toml"),
            Platform.windows: Path(context.home, ".config/teleport/teleport.toml"),
        }
        return dotfile_map[context.platform]

    @classmethod
    def from_system(cls) -> TeleportConfig:
        config_path = cls.get_config_path()
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config_dict = toml.load(f)
        except FileNotFoundError:
            raise TeleportException("Teleport config not initialized.")
        try:
            config = TeleportConfig.model_validate(config_dict)
        except ValidationError as e:
            raise TeleportException(str(e))
        return config

    def write(self, path: Path) -> None:
        config_dict = self.model_dump(mode="json", exclude_unset=True)
        if config_dict == dict():
            config_dict = self.__class__(destinations=dict()).model_dump(mode="json")
        with open(path, "w", encoding="utf-8") as f:
            toml.dump(config_dict, f)

    def write_to_system(self):
        config_path = self.get_config_path()
        self.write(config_path)

    def get_system_destinations(self) -> dict[DestinationName, DestinationPath]:
        return {
            name: self.resolve_desitination(name) for name in self.destinations.keys()
        }

    def resolve_desitination(
        self,
        destination_name: DestinationName,
    ) -> DestinationPath:
        destination = self.destinations.get(destination_name)
        if destination is None:
            raise TeleportException(
                f"Destination name {destination_name} not configured."
            )
        elif isinstance(destination, DestinationPath):
            return destination
        else:
            context = get_context()
            return destination.links[context.platform]
