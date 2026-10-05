# We are using __future__ module to tell python that the type hints can be ignored at the time of execution
from __future__ import annotations

# random module for generating synthetic data
import random
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import path

import click
import numpy as np
import yaml

# locating the file path of the parent's parent folder and storing their respective location.
CONFIG_DIR = Path(__file__).parent.parent / "config"
PREDEFINED_DIR = Path(__file__).parent.parent / "data" / "predefined"

@click.group()
def cli():
    """Synthetic e-commerce event data generator (bronze layer)."""

# This is the first command that gets used in the project, this command() is a function uder the group() function and has 3 arguments namely : num_products, num_users, seed
# The show_deafult parameter in the option so with that, if we use --help we will be able to see the default without seeing actual code, which helps a lot in simulating synthetic data
# The subprocess executes the python program as second process and runs it independently. 
@cli.command()
@click.option("--num-products", default=4000, show_default=True)
@click.option("--num-users", default=20000, show_default=True)
@click.option("--seed", default=42, show_default=True)
def seed(num_products, num_users, seed):
    """Generate the predefined product/user catalog (run this once)."""
    script = Path(__file__).parent.parent / "data" / "seed" / "generate_catalog.py"
        subprocess.run(
        [sys.executable, str(script),
         "--num-products", str(num_products),
         "--num-users", str(num_users),
         "--seed", str(seed)],
        check=True,
    )

if __name__ == "__main__":
    cli()
