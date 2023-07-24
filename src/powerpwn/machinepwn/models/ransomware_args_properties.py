from pydantic import Field

from powerpwn.machinepwn.models.command_args_properties_base_model import CommandArgsPropertiesBaseModel


class RansomwareArgsProperties(CommandArgsPropertiesBaseModel):
    ransomware_crawl_depth: str = Field(help="Recursively search into subdirectories this many times")
    ransomware_directories_to_init_crawl: str = Field(help="A list of directories to begin crawl from separated by a command (e.g.'C:\\,D:\\')")
    ransomware_encryption_key: str = Field(help="an encryption key used to encrypt each file identified (AES256)")
