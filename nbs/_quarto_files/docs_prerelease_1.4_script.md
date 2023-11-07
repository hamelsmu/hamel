<a href="../../../index.html"
class="navbar-brand navbar-brand-logo"><img src="../../../quarto.png"
class="navbar-logo" alt="Quarto logo." /></a>

<span class="navbar-toggler-icon"></span>

-   <a href="../../../index.html" class="nav-link"><span
    class="menu-text">Overview</span></a>
-   <a href="../../../docs/get-started/index.html" class="nav-link"><span
    class="menu-text">Get Started</span></a>
-   <a href="../../../docs/guide/index.html" class="nav-link"><span
    class="menu-text">Guide</span></a>
-   <a href="../../../docs/extensions/index.html" class="nav-link"><span
    class="menu-text">Extensions</span></a>
-   <a href="../../../docs/reference/index.html" class="nav-link"><span
    class="menu-text">Reference</span></a>
-   <a href="../../../docs/gallery/index.html" class="nav-link"><span
    class="menu-text">Gallery</span></a>
-   <a href="../../../docs/blog/index.html" class="nav-link"><span
    class="menu-text">Blog</span></a>
-   <a href="#" id="nav-menu-help" class="nav-link dropdown-toggle"
    role="button" data-bs-toggle="dropdown" aria-expanded="false"><span
    class="menu-text">Help</span></a>
    -   <a href="https://github.com/quarto-dev/quarto-cli/issues"
        class="dropdown-item"><em></em> <span class="dropdown-text">Report a
        Bug</span></a>
    -   <a href="https://github.com/quarto-dev/quarto-cli/discussions"
        class="dropdown-item"><em></em> <span class="dropdown-text">Ask a
        Question</span></a>
    -   <a href="../../../docs/faq/index.html" class="dropdown-item"><em></em>
        <span class="dropdown-text">FAQ</span></a>

<a href="https://twitter.com/quarto_pub"
class="quarto-navigation-tool px-1" aria-label="Quarto Twitter"
title="Quarto Twitter"><em></em></a>
<a href="https://github.com/quarto-dev/quarto-cli"
class="quarto-navigation-tool px-1" aria-label="Quarto GitHub"
title="Quarto GitHub"><em></em></a>
<a href="https://quarto.org/docs/blog/index.xml"
class="quarto-navigation-tool px-1" aria-label="Quarto Blog RSS"
title="Quarto Blog RSS"><em></em></a>

## On this page

-   <a href="#overview" id="toc-overview" class="nav-link active"
    data-scroll-target="#overview">Overview</a>
-   <a href="#render-and-preview" id="toc-render-and-preview"
    class="nav-link" data-scroll-target="#render-and-preview">Render and
    Preview</a>
-   <a href="#generating-markdown" id="toc-generating-markdown"
    class="nav-link" data-scroll-target="#generating-markdown">Generating
    Markdown</a>
-   <a href="#raw-cells" id="toc-raw-cells" class="nav-link"
    data-scroll-target="#raw-cells">Raw Cells</a>
-   <a href="#scripts-in-projects" id="toc-scripts-in-projects"
    class="nav-link" data-scroll-target="#scripts-in-projects">Scripts in
    Projects</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/prerelease/1.4/script.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Script Rendering for Jupyter

Pre-release Feature

This feature is new in the upcoming Quarto 1.4 release. To use the
feature now, you’ll need to
[download](https://quarto.org/docs/download/prerelease) and install the
Quarto pre-release.

## Overview

Quarto v1.4 includes support for rendering script files (e.g. `.py`,
`.jl`, or `.r`) that are specially formatted as notebooks. Script
rendering makes use of the [percent
format](https://jupytext.readthedocs.io/en/latest/formats-scripts.html)
that is supported by several other other tools including Spyder, VS
Code, PyCharm, and Jupytext.

For example, here is a Python script that includes both markdown and
code cells:

    script.py

    # %% [markdown] 
    # ---
    # title: Palmer Penguins
    # author: Norah Jones
    # date: 3/12/23
    # ---

    # %% 
    #| echo: false
    import pandas as pd
    df = pd.read_csv("palmer-penguins.csv")

    # %% [markdown]
    """
    ## Exploring the data

    See @fig-bill-sizes for an exploration of bill sizes by species.
    """

    # %% 
    #| label: fig-bill-sizes
    #| fig-cap: Bill Sizes by Species

    import matplotlib.pyplot as plt
    import seaborn as sns

    g = sns.FacetGrid(df, hue="species", height=3, aspect=3.5/1.5)
    g.map(plt.scatter, "bill_length_mm", "bill_depth_mm").add_legend()

Code cells are delimited by `# %%` and markdown cells are delimited by
`# %% [markdown]`. Markdown content can either be included in single
line comments (`#`) or multi-line strings (`"""`), both of which are
illustrated above.

Note that cell options are included as normal using `#|` prefixed
comments (e.g. `#| echo: false`). Also note that you can include blank
lines within cells (cells continue until another cell is encountered).

## Render and Preview

Rendering and previewing notebook scripts works exactly like `.qmd` and
`.ipynb` files. For example, the following commands are all valid:

    $ quarto render script.py
    $ quarto render script.jl

    $ quarto preview script.py
    $ quarto preview script.jl

Jupyter scripts rendered with Quarto must begin with a `# %% [markdown]`
cell (which normally includes the `title` and other YAML options). This
convention is how Quarto knows that it should parse code cells using the
percent format (as opposed to other notebook as script formats that may
be supported in the future).

Jupyter script rendering is supported for Python, Julia, and R. Note
that for R scripts, the [IRkernel](https://irkernel.github.io) will be
used to execute code cells rather than Knitr (support for the Knitr
[spin](https://bookdown.org/yihui/rmarkdown-cookbook/spin.html) script
format is planned but not yet implemented).

The latest version (v1.97.0) of the [Quarto VS Code
Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)
also implements support for render and preview of Jupyter scripts.

## Generating Markdown

Jupyter scripts are especially convenient when most of your document
consists of code that dynamically generates markdown. You can write
markdown from Python using functions in the `IPython.display` module.
For example:

    # %%
    #| echo: false
    radius = 10
    from IPython.display import Markdown
    Markdown(f"The _radius_ of the circle is **{radius}**.")

Note that dynamically generated markdown will still be enclosed in the
standard Quarto output divs. If you want to remove all of Quarto’s
default output enclosures use the `output: asis` option. For example:

    # %%
    #| echo: false
    #| output: asis
    radius = 10
    from IPython.display import Markdown
    Markdown(f"The _radius_ of the circle is **{radius}**.")

## Raw Cells

You can include raw cells (e.g. HTML or LaTeX) within scripts using the
`# %% [raw]` cell delimiter along with a `format` attribute, for
example:

    # %% [raw] format="html"
    """
    <iframe width="560" height="315" src="https://www.youtube.com/embed/lJIrF4YjHfQ?si=aP7PxA1Pz8IIoQUX"></iframe>
    """

## Scripts in Projects

Jupyter scripts can also be included within
[projects](../../../docs/projects/quarto-projects.html) (e.g. websites,
blogs, etc.). Scripts within projects are only rendered by Quarto when
they have a markdown cell at the top (e.g. `# %% [markdown]`).

If for some reason you need to ignore a script that begins with a
markdown cell, you can create an explict render list in `_quarto.yml`
that excludes individual scripts as required, for example:

    project:
      type: website
      render:
        - "*.{qmd,ipynb,py}"
        - "!utils.py"

Note that this technique is documented for the sake of completeness—in
practice you should almost never need to do this since Python scripts
rarely begin with `# %% [markdown]` unless you are authoring them
specifically as notebooks.

Proudly supported by [<img
src="https://www.rstudio.com/assets/img/posit-logo-fullcolor-TM.svg"
class="img-fluid" width="65" alt="Posit" />](https://posit.co)

-   <a href="../../../about.html" class="nav-link"></a>

    About

-   <a href="../../../docs/faq/index.html" class="nav-link"></a>

    FAQ

-   <a href="../../../license.html" class="nav-link"></a>

    License

-   <a href="../../../trademark.html" class="nav-link"></a>

    Trademark

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
