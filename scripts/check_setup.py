#!/usr/bin/env python3

try:
    from rich import print
except ImportError:
    print("rich not found. Try running pip install rich.")
    print("The following will not be pretty...")
import pathlib
import sys
import subprocess
import warnings
import os

repo_dir = pathlib.Path(__file__).parent.parent

errors = 0

python_version = sys.version.split('|')[0]
if '3.11' in python_version:
    print(f":white_check_mark: Python version: {python_version}")
else:
    print(f":x: Python version: {python_version}. Create a new virtual environment.")
    errors += 1
try:
    import plenoptic as po
except ModuleNotFoundError:
    errors += 1
    print(":x: plenoptic not found. Try running [bold]pip install plenoptic[/bold]")
else:
    print(f":white_check_mark: plenoptic version: {po.__version__}")

try:
    import torch
except ModuleNotFoundError:
    errors += 1
    print(":x: pytorch not found. Try running [bold]pip install torch[/bold]")
else:
    print(f":white_check_mark: pytorch version: {torch.__version__}")
    gpu = torch.cuda.is_available()
    if gpu:
        print(":white_check_mark: GPU available")
    else:
        print(":x: No GPU found. That's okay, everything will run, but it will be slower.")

p = subprocess.run(['jupyter', '--version'], capture_output=True)
if p.returncode != 0:
    errors += 1
    print(":x: jupyter not found. Try running [bold]pip install jupyter[/bold]")
else:
    # convert to str from bytestring
    stdout = '\n'.join(p.stdout.decode().split('\n')[1:])
    print(f":white_check_mark: jupyter found with following core packages:\n{stdout}")

p = subprocess.Popen(['jupyter', 'labextension', 'list'], stderr=subprocess.PIPE)
if os.name == "nt":
    search_cmd = "findstr"
else:
    search_cmd = "grep"
try:
    output = subprocess.check_output([search_cmd, 'myst'], stdin=p.stderr).decode().lower()
    p.wait()
except subprocess.CalledProcessError:
    errors += 1
    print(":x: jupyterlab_myst not found. Try running [bold]pip install jupyterlab_myst[/bold]")
else:
    if 'enabled' in output and 'ok' in output:
        with warnings.catch_warnings():
            # this import may give a deprecation warning about how jupyter handles paths
            warnings.simplefilter("ignore")
            import jupyterlab_myst
        print(f":white_check_mark: jupyterlab_myst version:\n{jupyterlab_myst.__version__}")
    else:
        errors += 1
        print(":x: jupyterlab_myst not set up correctly! Look at the output of `jupyter labextension list` and try running [bold]pip install jupyterlab_myst[/bold]")

repo_dir = pathlib.Path(__file__).parent.parent / 'notebooks'
gallery_dir = pathlib.Path(__file__).parent.parent / 'docs' / 'source' / 'full'
nbs = list(repo_dir.glob('**/*ipynb'))
gallery_scripts = [nb for nb in list(gallery_dir.glob('**/*md'))
                   if 'checkpoint' not in nb.name]
missing_nb = [f.stem for f in gallery_scripts
              if not any([f.stem == nb.stem.replace('-users', '') for nb in nbs])]
if len(missing_nb) == 0:
    print(":white_check_mark: All notebooks found")
else:
    errors += 1
    print(f":x: Following notebooks missing: {', '.join(missing_nb)}")
    print("   Did you run [bold]python scripts/setup.py[/bold]?")

if errors == 0:
    print("\n:tada::tada: Congratulations, setup successful!")
else:
    print(f"\n:worried: [red bold]{errors} Errors found.[/red bold]\n")
    print("Unfortunately, your setup was unsuccessful.")
    print("Try to resolve following the suggestions above.")
    print("If you encountered multiple installation errors, run [bold] pip install -r requirements[/bold]")
    print("If you are unable to fix your setup yourself, please come to the satellite event room at")
    print("12:30pm and show us the output of this command.")
