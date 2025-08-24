from teleport.config import DestinationPath, TeleportConfig, DestinationName


def list_destinations() -> dict[DestinationName, DestinationPath]:
    return TeleportConfig.from_system().get_system_destinations()
