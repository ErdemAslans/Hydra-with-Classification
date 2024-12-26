from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass
from omegaconf import MISSING

from config_schemas import data_module_schema, trainer_schema, task_schema


@dataclass
class Config:
    data_module: data_module_schema.DataModuleConfig = MISSING
    task: task_schema.TaskConfig = MISSING
    trainer: trainer_schema.TrainerConfig = MISSING


def setup_config() -> None:
    data_module_schema.setup_config()
    trainer_schema.setup_config()
    task_schema.setup_config()

    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)
