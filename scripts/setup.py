#!/usr/bin/env python3

import click
import pathlib
import requests
import subprocess

NB_DOWNLOAD_URL = "https://labforcomputationalvision.github.io/plenoptic-cshl-vision-2024/_downloads/dbf6e61da9e91ccf52bab94fae2ee5d8/introduction-stripped.ipynb"
NB_URL = "https://labforcomputationalvision.github.io/plenoptic-cshl-vision-2024/introduction-stripped.html"

def download_notebook():
    print("Unable to run strip_text script (if you're on Windows, this is expected), trying to download notebook manually...")
    try:
        r = requests.get(NB_DOWNLOAD_URL)
        with open('introduction-stripped.ipynb', 'wb') as f:
            f.write(r.content)
    except Exception as e:
        raise Exception(f"Unable to download notebook, go to {NB_URL} and download it manually") from e
    else:
        print("Downloaded notebook successfully!")

@click.command()
def main():
    repo_dir = pathlib.Path(__file__).parent.parent
    docs_dir = repo_dir / 'docs' / 'source'
    scripts_dir = repo_dir / 'scripts'
    try:
        ret = subprocess.run(['bash', scripts_dir / 'strip_text.sh'], cwd=repo_dir)
        # we hit this if the bash script doesn't run correctly (e.g., because they don't
        # have sed on their path)
        if ret.returncode != 0:
            download_notebook()
        else:
            subprocess.run(['jupytext', docs_dir / 'introduction-stripped.md',
                            '-o', 'introduction-stripped.ipynb', '--from', 'myst'],
                           cwd=repo_dir)
            print("Successfully converted notebook!")
    # we hit this if the user doesn't have bash
    except FileNotFoundError as e:
        download_notebook()


if __name__ == '__main__':
    main()
