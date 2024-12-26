## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)


## Project Overview

This project demonstrates how to build a scalable and maintainable machine learning pipeline for MNIST classification using PyTorch Lightning and Hydra. By integrating Hydra for configuration management, the project ensures that experiments are reproducible and easily configurable.

## Features

- **Modular Configuration:** Separate configuration files for different components like models, data modules, optimizers, and training settings.
- **Hydra Integration:** Simplifies configuration management with hierarchical and dynamic parameter overrides.
- **PyTorch Lightning:** Streamlines the training loop, making the code cleaner and more maintainable.
- **Model Checkpointing:** Automatically saves the best models based on validation accuracy.
- **Logging with TensorBoard:** Visualize training metrics in real-time.

## Installation

### Prerequisites

- Python 3.7 or higher
- Git

### Clone the Repository

```bash
git clone https://github.com/yourusername/mnist-classification-hydra.git
cd mnist-classification-hydra
