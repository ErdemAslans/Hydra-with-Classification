from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass


@dataclass
class TrainerConfig:
    _target_: str = "pytorch_lightning.Trainer"
    max_epochs: int = 10
    log_every_n_steps: int = 10
    accelerator: str = "gpu"
    devices: int = -1


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(group="trainer", name="trainer_schema", node=TrainerConfig)
