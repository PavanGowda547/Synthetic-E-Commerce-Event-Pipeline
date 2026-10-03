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
