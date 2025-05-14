#!/usr/bin/env python3

import re
import os
import pathlib
from glob import glob

USER_NB_EXPLAIN="""
This notebook has had all its explanatory text removed and has not been run.
 It is intended to be downloaded and run locally (or on the provided binder)
 while listening to the presenter's explanation. In order to see the fully
 rendered of this notebook, go [here]({})"""
PRESENTER_NB_EXPLAIN="""
This notebook has had all its explanatory text removed and has not been run.
 It is intended to be downloaded and run locally (or on the provided binder)
 while listening to the presenter's explanation. In order to see the fully
 rendered of this notebook, go [here]({})"""

for md in glob("docs/source/full/*md"):

    # don't do this on index or if we've already removed text
    if "index" in md or "stripped" in md:
        continue

    user_md = pathlib.Path(md.replace("full", "users").replace(".md", "-users.md"))
    user_ipynb = f"{user_md.stem}.ipynb"
    presenter_md = pathlib.Path(md.replace("full", "presenters").replace(".md", "-presenters.md"))
    presenter_ipynb = f"{presenter_md.stem}.ipynb"
    os.makedirs(user_md.parent, exist_ok=True)
    os.makedirs(presenter_md.parent, exist_ok=True)

    # make it a path object here, because we can't do string replace on path objects
    md = pathlib.Path(md)
    ipynb = f"{md.stem}.ipynb"
    local_path = f"../../full/{md.name}"

    contents = md.read_text()

    title = re.search("^# .*", contents, re.MULTILINE).group()

    # this matches the following (split by |, regex's or):
    # - the document metadata header
    # - all markdown headers (e.g., # TITLE)
    # - all code cells
    # - all divs with a render class
    # - all admonitions (in colon fences)
    regex_str = "---.*?---|^#.*?$|```{code-cell}.*?```|<div class=.render.*?/div>|:::.*?:::"
    preserved_text = re.findall(regex_str, contents, re.MULTILINE | re.DOTALL)

    # now we're producing two versions of the notebook: one for users and one for
    # presenters.

    # presenters notebook has the document metadata, all markdown headers, all code, all
    # admonitions with the render-presenter or render-all class, and div with class
    # render-presenter or render-all
    presenter_text = []
    for t in preserved_text:
        if ":::" in t:
            if "render-presenter" in t or "render-all" in t:
                presenter_text.append(t)
        elif "<div" in t and "render" in t:
            if "render-presenter" in t or "render-all" in t:
                # remove all divs
                t = re.sub(".*div.*", "", t)
                presenter_text.append(t)
        else:
            presenter_text.append(t)
    presenter_text = "\n".join(presenter_text)
    presenter_text = presenter_text.replace(title, title + PRESENTER_NB_EXPLAIN.format(local_path))
    presenter_text = presenter_text.replace(ipynb, presenter_ipynb)
    presenter_md.write_text(presenter_text)

    # user notebook has the document metadata, all markdown headers, no code unless
    # marked, all admonitions with the render-user or render-all class, and div with class
    # render-user or render-all
    user_text = []
    empty_code_cell = "```{code-cell}\n# enter code here\n```\n"
    for t in preserved_text:
        if "<div" in t and "render" in t:
            if "render-user" in t or "render-all" in t:
                # remove all divs
                t = re.sub("\s*</?div.*", "", t)
                user_text.append(t)
        elif ":::" in t:
            if "render-user" in t or "render-all" in t:
                user_text.append(t)
        elif "{code-cell}" in t:
            if "render-all" in t:
                user_text.append(t)
            elif "{code-cell}" not in user_text[-1]:
                user_text.append(empty_code_cell)
        else:
            user_text.append(t)
    user_text = "\n".join(user_text)
    user_text = user_text.replace(title, title + USER_NB_EXPLAIN.format(local_path))
    user_text = user_text.replace(ipynb, user_ipynb)
    user_md.write_text(user_text)
