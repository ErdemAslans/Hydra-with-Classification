from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING


@dataclass
class BackboneConfig:
    _target_: str = MISSING


@dataclass
class ResNet18BackboneConfig(BackboneConfig):
    _target_: str = "backbones.ResNet18"
    pretrained: bool = True


@dataclass
class ResNet34BackboneConfig(BackboneConfig):
    _target_: str = "backbones.ResNet34"
    pretrained: bool = True


@dataclass
class ResNet50BackboneConfig(BackboneConfig):
    _target_: str = "backbones.ResNet50"
    pretrained: bool = True


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(group="task/model/backbone", name="resnet18_schema", node=ResNet18BackboneConfig)
    cs.store(group="task/model/backbone", name="resnet34_schema", node=ResNet34BackboneConfig)
    cs.store(group="task/model/backbone", name="resnet50_schema", node=ResNet50BackboneConfig)
