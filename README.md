# Test Databricks Delta Share Access

A minimal tool to test access to Delta Share tables.

## Requirements

- ASDF package manager w/ UV and Python plugins

Otherwise install the follwing python and UV versions with your prefered method
- Python 3.12
- UV 0.8.2


## Setup

### 0. Setup ASDF

Install ASDF and plugins:

- [ASDF Install Guide](https://asdf-vm.com/guide/getting-started.html)

ASDF Plugins
```bash
asdf plugin add uv https://github.com/asdf-community/asdf-uv.git;
asdf plugin add python https://github.com/asdf-community/asdf-python.git
```

### 1. Install Python & UV

Install required packages:
```bash
asdf install;
```


### 2. Add Delta Sharing credentials to repositories root directoy `/config.share`

## Usage

List all available tables:
```bash
uv run main.py
```

Get table information and sample data:
```bash
uv run main.py --table <share_name>.<schema_name>.<table_name>
```