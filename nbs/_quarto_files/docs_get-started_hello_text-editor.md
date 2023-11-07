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
-   <a href="#editor-modes" id="toc-editor-modes" class="nav-link"
    data-scroll-target="#editor-modes">Editor Modes</a>
-   <a href="#rendering" id="toc-rendering" class="nav-link"
    data-scroll-target="#rendering">Rendering</a>
-   <a href="#authoring" id="toc-authoring" class="nav-link"
    data-scroll-target="#authoring">Authoring</a>
-   <a href="#yaml-options" id="toc-yaml-options" class="nav-link"
    data-scroll-target="#yaml-options">YAML Options</a>
-   <a href="#markdown" id="toc-markdown" class="nav-link"
    data-scroll-target="#markdown">Markdown</a>
-   <a href="#code-cells" id="toc-code-cells" class="nav-link"
    data-scroll-target="#code-cells">Code Cells</a>
-   <a href="#next-up" id="toc-next-up" class="nav-link"
    data-scroll-target="#next-up">Next Up</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/get-started/hello/text-editor.qmd"
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

In this tutorial we’ll show you how to use your favorite text editor
with Quarto. You’ll edit plain text `.qmd` files and preview the
rendered document in a web browser as you work.

Below is an overview of how this will look.

<img src="images/text-editor-quarto-preview.png"
class="border column-body-outset-right img-fluid"
alt="On the left: A VS Code notebook titled Quarto Basics containing some text, a code cell, and the result of the code cell, which is a line plot on a polar axis. On the right: Rendered version of the same notebook." />

The notebook on the left is *rendered* into the HTML version you see on
the right. This is the basic model for Quarto publishing—take a source
document (in this case a notebook) and render it to a variety of [output
formats](https://quarto.org/docs/output-formats/all-formats.html),
including HTML, PDF, MS Word, etc.

The tutorials will make use of the `matplotlib` and `plotly` Python
packages—the commands you can use to install them are given in the table
below.

<table class="table" style="width:88%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 72%" />
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
class="sourceCode bash code-with-copy"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="ex">python3</span> <span class="at">-m</span> pip install jupyter matplotlib plotly</span></code></pre></div>
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
class="sourceCode powershell code-with-copy"><code class="sourceCode powershell"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>py <span class="op">-</span>m pip install jupyter matplotlib plotly</span></code></pre></div>
</div>
</div></td>
</tr>
</tbody>
</table>

Note

Note that while this tutorial uses Python, using Julia (via the
[IJulia](https://julialang.github.io/IJulia.jl/stable/) kernel) is also
well supported. See the article on [Using
Julia](../../../docs/computations/julia.html) for additional details.

## Editor Modes

If you are using VS Code, you should install the [Quarto
Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto)
for VS Code before proceeding. The extension provides syntax
highlighting for markdown and embedded languages, completion for
embedded languages (e.g. Python, R, Julia, LaTeX, etc.), commands and
key-bindings for running cells and selected line(s), and much more.

There are also Quarto syntax highlighting modes available for several
other editors:

<table class="table">
<colgroup>
<col style="width: 30%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header header">
<th>Editor</th>
<th>Extension</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td>Emacs</td>
<td><a href="https://github.com/quarto-dev/quarto-emacs"
class="uri">https://github.com/quarto-dev/quarto-emacs</a></td>
</tr>
<tr class="even even">
<td>Vim / Neovim</td>
<td><a href="https://github.com/quarto-dev/quarto-vim"
class="uri">https://github.com/quarto-dev/quarto-vim</a></td>
</tr>
<tr class="odd odd">
<td>Neovim</td>
<td><a href="https://github.com/quarto-dev/quarto-nvim"
class="uri">https://github.com/quarto-dev/quarto-nvim</a></td>
</tr>
<tr class="even even">
<td>Sublime Text</td>
<td><a href="https://github.com/quarto-dev/quarto-sublime"
class="uri">https://github.com/quarto-dev/quarto-sublime</a></td>
</tr>
</tbody>
</table>

## Rendering

We’ll start out by rendering a simple example (`hello.qmd`) to a couple
of formats. If you want to follow along step-by-step in your own
environment, create a new file named `hello.qmd` and copy the following
content into it.

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

Next, open a Terminal and switch to the directory containing
`hello.qmd`.

Let’s start by rendering the document to a couple of formats.

    Terminal

    quarto render hello.qmd --to html
    quarto render hello.qmd --to docx

Note that the target file (in this case `hello.qmd`) should always be
the very first command line argument.

When you render a `.qmd` file with Quarto, the executable code blocks
are processed by Jupyter, and the resulting combination of code,
markdown, and output is converted to plain markdown. Then, this markdown
is processed by [Pandoc](http://pandoc.org/), which creates the finished
format.

<img src="images/qmd-how-it-works.png"
class="img-fluid quarto-figure-left"
alt="Workflow diagram starting with a qmd file, then Jupyter, then md, then pandoc, then PDF, MS Word, or HTML." />

## Authoring

The `quarto render` command is used to create the final version of your
document for distribution. However, during authoring you’ll use the
`quarto preview` command. Try it now from the Terminal with `hello.qmd`.

    Terminal

    quarto preview hello.qmd

This will render your document and then display it in a web browser.

<img src="images/quarto-preview.png" class="border img-fluid"
width="500"
alt="Rendered version of the earlier notebook in a web browser." />

You might want to position your editor and the browser preview
side-by-side so you can see changes as you work.

<img src="images/text-editor-quarto-preview.png"
class="border column-body-outset-right img-fluid"
alt="Side-by-side preview of notebook on the left and live preview in the browser on the right." />

To see live preview in action:

1.  Change the the line of code that defines `theta` as follows:

        theta = 4 * np.pi * r

2.  Save the file. The document is re-rendered, and the browser preview
    is updated.

This is the basic workflow for authoring with Quarto.

There are few different types of content in `hello.qmd`, let’s work a
bit with each type.

## YAML Options

At the top of the file there is a YAML block with document level
options.

    ---
    title: "Quarto Basics"
    format:
      html:
        code-fold: true
    jupyter: python3
    ---

Try changing the `code-fold` option to `false`:

    format: 
      html:
        code-fold: false

Then save the file. You’ll notice that the code is now shown above the
plot, where previously it was hidden with a **Code** button that could
be used to show it.

## Markdown

Narrative content is written using markdown. Here we specify a header
and a cross-reference to the figure created in the code cell below.

    ## Polar Axis

    For a demonstration of a line plot on a polar axis, see @fig-polar.

Try changing the header and saving the notebook—the preview will update
with the new header text.

## Code Cells

Code cells contain executable code to be run during render, with the
output (and optionally the code) included in the rendered document.

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

You are likely familiar with the Matplotlib code given here. However,
there are some less familiar components at the top of the code cell:
`label` and `fig-cap` options. Cell options are written in YAML using a
specially prefixed comment (`#|`).

In this example, the cell options are used to make the figure
cross-reference-able. Try changing the `fig-cap` and/or the code,
running the cell, and then saving the file to see the updated preview.

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
