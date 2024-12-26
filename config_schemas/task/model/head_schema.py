from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class HeadConfig:
    _target_: str = MISSING


@dataclass
class IdentityHeadConfig(HeadConfig):
    _target_: str = "heads.IdentityHead"


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(group="task/model/head", name="identity_head_schema", node=IdentityHeadConfig)
