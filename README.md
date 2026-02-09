# Test Databricks Delta Share Access

A minimal tool to test access to Delta Share tables.

## Requirements

- Python 3.12
- UV 0.8.2
- (optional but recommended) ASDF package manager w/ UV and Python plugins

## Setup

1. If using [ASDF](https://asdf-vm.com/) as your tool manager:

Install required packages:
    ```bash
    asdf install
    ```

Otherwise install python and UV with your prefered method 

2. Add Delta Sharing credentials to repositories root directoy `/config.share`

## Usage

List all available tables:
```bash
uv run main.py
```

Get table information and sample data:
```bash
uv run main.py --table <share_name>.<schema_name>.<table_name>
```