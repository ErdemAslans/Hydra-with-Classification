from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class AdapterConfig:
    _target_: str = MISSING


@dataclass
class LinearAdapterConfig(AdapterConfig):
    _target_: str = "adapters.LinearAdapter"
    in_features: int = MISSING
    out_features: int = MISSING
    flatten_input: bool = False


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(group="task/model/adapter", name="linear_adapter_schema", node=LinearAdapterConfig)
