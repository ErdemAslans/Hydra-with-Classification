from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class LossFunctionConfig:
    _target_: str = MISSING


@dataclass
class CrossEntropyLossFunctionConfig(LossFunctionConfig):
    _target_: str = "torch.nn.CrossEntropyLoss"


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(group="task/loss_function", name="cross_entropy_loss_function_schema", node=CrossEntropyLossFunctionConfig)
