from teleport.config import TeleportConfig
from teleport.exceptions import TeleportException


def init():
    try:
        config = TeleportConfig.from_system()
        raise TeleportException(
            f"Teleport is already initialized at {TeleportConfig.get_config_path().as_posix()}"
        )
    except TeleportException:
        config = TeleportConfig(destinations=dict())
    config_path = TeleportConfig.get_config_path()
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config.write(config_path)
