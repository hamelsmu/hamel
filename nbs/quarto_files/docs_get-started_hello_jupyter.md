<a href="../../../index.html"
class="navbar-brand navbar-brand-logo"><img src="../../../quarto.png"
class="navbar-logo" alt="Quarto logo." /></a>

<span class="navbar-toggler-icon"></span>

-   <a href="../../../index.html" class="nav-link"><span
    class="menu-text">Overview</span></a>
-   <a href="../../../docs/get-started/index.html" class="nav-link active"
    aria-current="page"><span class="menu-text">Get Started</span></a>
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

1.  Tutorial: Hello, Quarto

<span class="flex-grow-1" role="button" bs-toggle="collapse"
bs-target=".quarto-sidebar-collapse-item" aria-controls="quarto-sidebar"
aria-expanded="false" aria-label="Toggle sidebar navigation"
onclick="if (window.quartoToggleHeadroom) { window.quartoToggleHeadroom(); }"></span>

-   <a href="../../../docs/get-started/index.html"
    class="sidebar-item-text sidebar-link"><span class="menu-text">Get
    Started</span></a>

-   <a href="../../../docs/get-started/hello/"
    class="sidebar-item-text sidebar-link"><span class="menu-text">Tutorial:
    Hello, Quarto</span></a>

-   <a href="../../../docs/get-started/computations/"
    class="sidebar-item-text sidebar-link"><span class="menu-text">Tutorial:
    Computations</span></a>

-   <a href="../../../docs/get-started/authoring/"
    class="sidebar-item-text sidebar-link"><span class="menu-text">Tutorial:
    Authoring</span></a>

## On this page

-   <a href="#overview" id="toc-overview" class="nav-link active"
    data-scroll-target="#overview">Overview</a>
-   <a href="#rendering" id="toc-rendering" class="nav-link"
    data-scroll-target="#rendering">Rendering</a>
-   <a href="#authoring" id="toc-authoring" class="nav-link"
    data-scroll-target="#authoring">Authoring</a>
-   <a href="#yaml-options" id="toc-yaml-options" class="nav-link"
    data-scroll-target="#yaml-options">YAML Options</a>
-   <a href="#markdown-cells" id="toc-markdown-cells" class="nav-link"
    data-scroll-target="#markdown-cells">Markdown Cells</a>
-   <a href="#code-cells" id="toc-code-cells" class="nav-link"
    data-scroll-target="#code-cells">Code Cells</a>
-   <a href="#next-up" id="toc-next-up" class="nav-link"
    data-scroll-target="#next-up">Next Up</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/get-started/hello/jupyter.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Tutorial: Hello, Quarto

-   <a href="vscode.html" class="nav-link"><img
    src="../images/vscode-logo.png" />VS Code</a>
-   <a href="jupyter.html" class="nav-link"><img
    src="../images/jupyter-logo.png" />Jupyter</a>
-   <a href="rstudio.html" class="nav-link"><img
    src="../images/rstudio-logo.png" />RStudio</a>
-   <a href="neovim.html" class="nav-link"><img
    src="../images/neovim-logo.svg" />Neovim</a>
-   <a href="text-editor.html" class="nav-link"><img
    src="../images/text-editor-logo.png" id="text-editor-logo" />Editor</a>

## Overview

In this tutorial we’ll show you how to use Jupyter Lab with Quarto.
You’ll edit code and markdown in Jupyter Lab, just as you would with any
notebook, and preview the rendered document in a web browser as you
work.

Below is an overview of how this will look.

<img src="images/jupyter-quarto-preview.png" class="img-fluid"
alt="On the left: A Jupyter notebook titled Quarto Basics containing some text, a code cell, and the result of the code cell, which is a line plot on a polar axis. On the right: Rendered version of the same notebook." />

The notebook on the left is *rendered* into the HTML version you see on
the right. This is the basic model for Quarto publishing—take a source
document (in this case a notebook) and render it to a variety of [output
formats](https://quarto.org/docs/output-formats/all-formats.html),
including HTML, PDF, MS Word, etc.

Note

Note that while this tutorial uses Python, using Julia (via the
[IJulia](https://julialang.github.io/IJulia.jl/stable/) kernel) is also
well supported. See the article on [Using
Julia](../../../docs/computations/julia.html) for additional details.

## Rendering

We’ll start out by opening a notebook (`hello.ipynb`) in Jupyter Lab and
rendering it to a couple of formats. If you want to follow along
step-by-step in your own environment, download the notebook below.

<a href="_hello.ipynb" download="hello.ipynb">Download hello.ipynb</a>

Then, create a new directory to work within, copy the notebook into this
directory, and switch to this directory in a Terminal.

Next, execute these commands to install JupyterLab along with the
packages used in the tutorial (`matplotlib` and `plotly),` and to open
the tutorial notebook:

<table class="table" style="width:90%;">
<colgroup>
<col style="width: 22%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header header">
<th>Platform</th>
<th>Commands</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td>Mac/Linux</td>
<td><div class="code-with-filename">
<div class="code-with-filename-file">
<pre><code>Terminal</code></pre>
</div>
<div id="cb1" class="sourceCode" data-filename="Terminal">
<div class="sourceCode" id="cb2"><pre
class="sourceCode bash code-with-copy"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="ex">python3</span> <span class="at">-m</span> pip install jupyter jupyterlab</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="ex">python3</span> <span class="at">-m</span> pip install matplotlib plotly</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="ex">python3</span> <span class="at">-m</span> jupyter lab hello.ipynb</span></code></pre></div>
</div>
</div></td>
</tr>
<tr class="even even">
<td>Windows</td>
<td><div class="code-with-filename">
<div class="code-with-filename-file">
<pre><code>Terminal</code></pre>
</div>
<div id="cb2" class="sourceCode" data-filename="Terminal">
<div class="sourceCode" id="cb4"><pre
class="sourceCode bash code-with-copy"><code class="sourceCode bash"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="ex">py</span> <span class="at">-m</span> pip install jupyter jupyterlab</span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a><span class="ex">py</span> <span class="at">-m</span> pip install matplotlib plotly</span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a><span class="ex">py</span> <span class="at">-m</span> jupyter lab hello.ipynb</span></code></pre></div>
</div>
</div></td>
</tr>
</tbody>
</table>

Here is our notebook in Jupyter Lab.

    ---
    title: "Quarto Basics"
    format:
      html:
        code-fold: true
    jupyter: python3
    ---

    For a demonstration of a line plot on a polar axis, see @fig-polar.

    ```{python}
    #| label: fig-polar
    #| fig-cap: "A line plot on a polar axis"

    import numpy as np
    import matplotlib.pyplot as plt

    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi * r
    fig, ax = plt.subplots(
      subplot_kw = {'projection': 'polar'} 
    )
    ax.plot(theta, r)
    ax.set_rticks([0.5, 1, 1.5, 2])
    ax.grid(True)
    plt.show()
    ```

<img src="images/jupyter-basics.png" class="border img-fluid"
alt="A Jupyter notebook titled Quarto Basics containing some text, a code cell, and the result of the code cell, which is a line plot on a polar axis." />

Next, create a new Terminal within Jupyter Lab to use for Quarto
commands.

<img src="images/jupyter-terminal.png" class="border img-fluid"
alt="Screenshot of menu items in Jupuyter Lab: File &gt; New &gt; Terminal." />

And finally, render the notebook to a couple of formats.

    Terminal

    quarto render hello.ipynb --to html
    quarto render hello.ipynb --to docx

Note that the target file (in this case `hello.ipynb`) should always be
the very first command line argument.

When you render a Jupyter notebook with Quarto, the contents of the
notebook (code, markdown, and outputs) are converted to plain markdown
and then processed by [Pandoc](http://pandoc.org/), which creates the
finished format.

<img src="images/ipynb-how-it-works.png"
class="img-fluid quarto-figure-left" style="margin-left: 15px;"
width="516"
alt="Workflow diagram starting with a Jupyter notebook, then md, then pandoc, then PDF, MS Word, or HTML." />

## Authoring

The `quarto render` command is used to create the final version of your
document for distribution. However, during authoring you’ll use the
`quarto preview` command. Try it now from the Terminal with
`hello.ipynb`.

    Terminal

    quarto preview hello.ipynb

This will render your document and then display it in a web browser.

<img src="images/quarto-preview.png" class="border img-fluid"
width="500"
alt="Rendered version of the earlier notebook in a web browser." />

You might want to position Jupyter Lab and the browser preview
side-by-side so you can see changes as you work.

<img src="images/jupyter-quarto-preview.png" class="img-fluid"
alt="Side-by-side preview of notebook on the left and live preview in the browser on the right." />

To see live preview in action:

1.  Change the the line of code that defines `theta` as follows:

        theta = 4 * np.pi * r

2.  Re-run the code cell to generate a new version of the plot.

3.  Save the notebook (the preview will update automatically).

This is the basic workflow for authoring with Quarto. Once you are
comfortable with this, we also recommend installing the [Quarto
JupyterLab Extension](../../../docs/tools/jupyter-lab-extension.html)
which provides additional tools for working with Quarto in JupyterLab.

There are few different types of cells in our notebook, let’s work a bit
with each type.

## YAML Options

You are likely already familiar with markdown and code cells, but there
is a new type of cell (“Raw”) that is used for document-level YAML
options.

    ---
    title: "Quarto Basics"
    format:
      html:
        code-fold: true
    jupyter: python3
    ---

<img src="images/jupyter-yaml.png" class="border img-fluid"
alt="YAML of the notebook with the fields title, format, and jupyter. Title is set to Quarto Basics with title: &quot;Quarto Basics&quot;. Format is defined as html in the next line, and within the html format, code-fold is set to true. Jupyter is set to python3 with jupyter: python3." />

Try changing the `code-fold` option to `false`.

    format: 
      html:
        code-fold: false

Then save the notebook. You’ll notice that the code is now shown above
the plot, where previously it was hidden with a **Code** button that
could be used to show it.

## Markdown Cells

Markdown cells contain raw markdown that will be passed through to
Quarto during rendering. You can use any valid Quarto [markdown
syntax](../../../docs/authoring/markdown-basics.html) in these cells.
Here we specify a header and a cross-reference to the figure created in
the code cell below.

    ## Polar Axis

    For a demonstration of a line plot on a polar axis, see @fig-polar.

<img src="images/jupyter-markdown.png" class="border img-fluid"
alt="A Markdown cell with the title Polar Axis as a second level header and text that reads &#39;For a demonstration of a line plot on a polar axis, see @fig-polar.&#39;" />

Try changing the header and saving the notebook—the preview will update
with the new header text.

## Code Cells

You are likely already familiar with code cells, like the one shown
below.

    ```{python}
    #| label: fig-polar
    #| fig-cap: "A line plot on a polar axis"

    import numpy as np
    import matplotlib.pyplot as plt

    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi * r
    fig, ax = plt.subplots(
      subplot_kw = {'projection': 'polar'} 
    )
    ax.plot(theta, r)
    ax.set_rticks([0.5, 1, 1.5, 2])
    ax.grid(True)
    plt.show()
    ```

<img src="images/jupyter-cell.png" class="border img-fluid"
alt="A code cell with cell options for label and fig-cap and the code required to create the line plot on a polar axis." />

But there are some new components at the top of the code cell: `label`
and `fig-cap`options. Cell options are written in YAML using a specially
prefixed comment (`#|`).

In this example, the cell options are used to make the figure
cross-reference-able. Try changing the `fig-cap` and/or the code,
running the cell, and then saving the notebook to see the updated
preview.

There are a wide variety of [cell
options](../../../docs/reference/cells/cells-jupyter.html) that you can
apply to tailor your output. We’ll delve into these options in the next
tutorial.

Note

One particularly useful cell option for figures is `fig-alt`, which
enables you to add alternative text to images for users with visual
impairments. See Amy Cesal’s article on [Writing Alt Text for Data
Visualization](https://medium.com/nightingale/writing-alt-text-for-data-visualization-2a218ef43f81)
to learn more.

## Next Up

You now know the basics of creating and authoring Quarto documents. The
following tutorials explore Quarto in more depth:

-   [Tutorial: Computations](../computations/) — Learn how to tailor the
    behavior and output of executable code blocks.

-   [Tutorial: Authoring](../authoring/) — Learn more about output
    formats and technical writing features like citations, crossrefs,
    and advanced layout.

Additionally, you may want to install the [Quarto JupyterLab
Extension](../../../docs/tools/jupyter-lab-extension.html) which
provides additional tools for working with Quarto in JupyterLab.

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
