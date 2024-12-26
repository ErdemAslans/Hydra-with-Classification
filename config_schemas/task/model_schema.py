from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING

from config_schemas.task.model import backbone_schema, adapter_schema, head_schema


@dataclass
class ModelConfig:
    _target_: str = MISSING


@dataclass
class SimpleModelConfig(ModelConfig):
    _target_: str = "models.SimpleModel"
    backbone: backbone_schema.BackboneConfig = MISSING
    adapter: adapter_schema.AdapterConfig = MISSING
    head: head_schema.HeadConfig = MISSING


@dataclass
class CIFAR10ModelConfig(ModelConfig):
    _target_: str = "models.CIFAR10Model"
    backbone: backbone_schema.BackboneConfig = MISSING
    adapter: adapter_schema.AdapterConfig = MISSING
    head: head_schema.HeadConfig = MISSING


def setup_config() -> None:
    backbone_schema.setup_config()
    adapter_schema.setup_config()
    head_schema.setup_config()

    cs = ConfigStore.instance()
    cs.store(group="task/model", name="simple_model_schema", node=SimpleModelConfig)
    cs.store(group="task/model", name="cifar10_model_schema", node=SimpleModelConfig)
