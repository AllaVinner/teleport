from teleport.config import TeleportConfig


def clear():
    config = TeleportConfig()
    config.write_to_system()
