from teleport.config import TeleportConfig
from teleport.exceptions import TeleportException


def remove(name: str) -> None:
    config = TeleportConfig.from_system()
    if name not in config.destinations:
        raise TeleportException(f"Destination name {name} not in configuration.")
    del config.destinations[name]
    config.write_to_system()
