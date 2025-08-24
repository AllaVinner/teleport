from enum import Enum
from typing import Literal
from pathlib import Path

from teleport.config import TeleportConfig
from teleport.exceptions import TeleportException, Unreachable
from teleport.util import format_destination_path


class WriteMode(Enum):
    create = "create"
    update = "update"
    ensure = "ensure"


WriteModeLiteral = Literal["create", "update", "ensure"]


def add(
    name: str, path: Path | str, write_mode: WriteMode | WriteModeLiteral = "ensure"
) -> None:
    formatted_path = format_destination_path(path)
    write_mode = WriteMode(write_mode)
    config = TeleportConfig.from_system()
    if write_mode == WriteMode.ensure:
        pass
    elif write_mode == WriteMode.update:
        if name not in config.destinations:
            raise TeleportException(f"Destination name {name} is not configured.")
    elif write_mode == WriteMode.create:
        if name in config.destinations:
            raise TeleportException(f"Destination name {name} is already configured.")
    else:
        raise Unreachable("All write modes should have been implemented.")
    config.destinations[name] = formatted_path
    config.write_to_system()
