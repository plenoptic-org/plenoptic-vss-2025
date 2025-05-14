# plenoptic-vss-2025

Material for [satellite at VSS, 2025](https://www.visionsciences.org/2025-plenoptic-satellite/). See the website for more details.

> [!INFO]
> The rest of this README is for contributors to the workshop.

## Building the site locally

> [!WARNING]
> For some reason, we need `jupyterlab < 4.3` in order to get the link highlighting working. There's a class, `.jp-ThemedContainer`, which removes the link styling. Possibly related to [this PR](https://github.com/jupyterlab/jupyterlab/pull/16519) or [this issue](https://github.com/jupyterlab/jupyterlab/issues/13493).

To build the site locally, clone this repo and install it in a fresh python 3.11 environment (`pip install -r requirements.txt`). Then run `make -C docs html O="-T"` and open `docs/build/html/index.html` in your browser.

## strip_text.py

This script creates two copies of each file found at `docs/source/full/*md`, the copies are placed at `docs/source/users/*.md` and `docs/source/presenters/*.md`. Neither of these copies are run; the presenters version is intended as a reference for presenters, while the users version is what users will start with.

For this to work:
- The title should be on a line by itself, use `#` (e.g., `# My awesome title`) and be the first such line (so no comments above it).
- All headers must be markdown-style (using `#`), rather than using `------` underneath them.
- You may need to place blank newlines before/after any `div` opening or closing. I think if you don't place newlines after the `div` opening, it will consider everything after it part of a markdown block (which is probably not what you want if it's a `{code-cell}`).

Full notebook:
- Will not render any markdown wrapped in a div with `class='render-user'` or `class='render-presenter'` (but will render those wrapped in `class='render-all'`)
- Will not render or run any code wrapped in a div at all! Thus, for code that you want in all notebooks, add `:tag: [render-all]`, but for code that you only want in the user / presenter notebook, wrap it in a div with `class='render-user'` / `class='render-presenter'`. 
- Similarly, wrapping colon-fence blocks (which use `:::`, e.g., admonitions) are messed up when you wrap them in a `div`. But they have a `:class:` attribute themselves, so just add the appropriate `render` class there. See the "Download" admonition at the top of each notebook for an example.

Presenters version preserves:
- All markdown headers.
- All code blocks.
- Only colon-fence blocks (e.g., admonitions) that have the class `render-presenter` or `render-all`
- Only markdown wrapped in a `<div class='render-presenter'>` or `<div class='render-all'>`.

Users version preserves:
- All markdown headers.
- Only code blocks with `:tag: [render-all]` *OR* wrapped in a `<div class='render-user'>`. For code blocks in render-user divs, you should probably also add the `skip-execution` tag
- Only colon-fence blocks (e.g., admonitions) that have the class `render-user` or `render-all`
- Only markdown wrapped in a `<div class='render-user>` or `<div class='render-all'>`.

    
## binder

See [nemos Feb 2024 workshop](https://github.com/flatironinstitute/nemos-workshop-feb-2024) for details on how to set up the Binder
