#!/usr/bin/env python3

try:
    import click
    import plenoptic
except ImportError:
    raise ImportError(
        "We couldn't find an important package, which likely means"
        " we're not running from the right virtual "
        "environment! Did you forget to activate your virtual env"
        " (using `source` or `conda activate`, depending on how "
        "you set it up)"
    )
import pathlib
import shutil
import subprocess
import re
import os
import warnings


@click.command()
def main():
    repo_dir = pathlib.Path(__file__).parent.parent
    nb_dir = repo_dir / 'notebooks'
    scripts_dir = repo_dir / 'scripts'
    docs_nb_dir = repo_dir / 'docs' / 'source' / 'users'
    print("Preparing notebooks...")
    shutil.rmtree(docs_nb_dir, ignore_errors=True)
    shutil.rmtree(repo_dir / 'docs' / 'source' / 'presenters', ignore_errors=True)
    subprocess.run(['python', repo_dir / 'scripts' / 'strip_text.py'], cwd=repo_dir)
    for f in docs_nb_dir.glob('*md'):
        output_f = (nb_dir / f.name.replace('md', 'ipynb')).absolute()
        output_f.parent.mkdir(exist_ok=True)
        subprocess.run(['jupytext', f.absolute(), '-o', output_f,
                        '--from', 'myst'], cwd=repo_dir)
        nb_contents = re.sub(r'../_static/', r'../docs/source/_static/',
                             output_f.read_text())
        output_f.write_text(nb_contents)


if __name__ == '__main__':
    main()
