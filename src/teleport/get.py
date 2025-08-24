from teleport.config import DestinationPath, TeleportConfig
from teleport.util import resolve_path


def get(destination_name: str) -> DestinationPath:
    config = TeleportConfig.from_system()
    return resolve_path(config.resolve_desitination(destination_name)).as_posix()
