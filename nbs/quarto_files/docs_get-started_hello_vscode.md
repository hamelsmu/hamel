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
    -   <a href="#basic-workflow" id="toc-basic-workflow" class="nav-link"
        data-scroll-target="#basic-workflow">Basic Workflow</a>
-   <a href="#render-and-preview" id="toc-render-and-preview"
    class="nav-link" data-scroll-target="#render-and-preview">Render and
    Preview</a>
    -   <a href="#how-it-works" id="toc-how-it-works" class="nav-link"
        data-scroll-target="#how-it-works">How it Works</a>
    -   <a href="#authoring" id="toc-authoring" class="nav-link"
        data-scroll-target="#authoring">Authoring</a>
    -   <a href="#running-cells" id="toc-running-cells" class="nav-link"
        data-scroll-target="#running-cells">Running Cells</a>
-   <a href="#yaml-options" id="toc-yaml-options" class="nav-link"
    data-scroll-target="#yaml-options">YAML Options</a>
-   <a href="#markdown" id="toc-markdown" class="nav-link"
    data-scroll-target="#markdown">Markdown</a>
-   <a href="#code-cells" id="toc-code-cells" class="nav-link"
    data-scroll-target="#code-cells">Code Cells</a>
-   <a href="#external-preview" id="toc-external-preview" class="nav-link"
    data-scroll-target="#external-preview">External Preview</a>
-   <a href="#next-up" id="toc-next-up" class="nav-link"
    data-scroll-target="#next-up">Next Up</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/get-started/hello/vscode.qmd"
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

In this tutorial we’ll show you how to use Quarto with VS Code. Before
getting started, you should install the [Quarto VS Code
Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto),
which includes many tools that enhance working with Quarto, including:

-   Integrated render and preview for Quarto documents.
-   Syntax highlighting for markdown and embedded languages
-   Completion and diagnostics for YAML options
-   Completion for embedded languages (e.g. Python, R, Julia, etc.)
-   Commands and key-bindings for running cells and selected lines.

You can install the Quarto extension from within the **Extensions** tab
in VS Code, from the [Extension
Marketplace](https://marketplace.visualstudio.com/items?itemName=quarto.quarto),
the [Open VSX Registry](https://open-vsx.org/extension/quarto/quarto) or
directly from a [VISX extension
file](https://github.com/quarto-dev/quarto-vscode#visx-install).

Note

This tutorial focuses on editing plain text Quarto `.qmd` files in VS
Code. Depending on your preferences and the task at hand there are two
other editing modes available for Quarto documents: the [Visual
Editor](../../../docs/visual-editor/vscode/index.html) and the [Notebook
Editor](../../../docs/tools/vscode-notebook.html). For the purposes of
learning we recommend you work through this tutorial using the VS Code
text editor, then after you’ve mastered the basics explore using the
other editing modes.

### Basic Workflow

Quarto `.qmd` files contain a combination of markdown and executable
code cells. Here’s what it might look like in VS Code to edit and
preview a `.qmd` file:

<img src="../../../docs/tools/images/vscode-render.png"
class="border img-fluid"
alt="Two windows arranged side by side. The window on the left is a qmd file opened in VSCode. The contents of this document are the same as the first part of the Getting Started: Welcome section of this website. The contents of this document are rendered by Quarto in the window on the right." />

The document on the left is *rendered* into the HTML version you see on
the right. This is the basic model for Quarto publishing—take a source
document and render it to a variety of [output
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

## Render and Preview

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

Note that if you are following along be sure to install the required
dependencies if you haven’t already:

<table class="table" style="width:89%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 73%" />
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
<div id="cb4" class="sourceCode" data-filename="Terminal">
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
<div id="cb5" class="sourceCode" data-filename="Terminal">
<div class="sourceCode" id="cb4"><pre
class="sourceCode powershell code-with-copy"><code class="sourceCode powershell"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>py <span class="op">-</span>m pip install jupyter matplotlib plotly</span></code></pre></div>
</div>
</div></td>
</tr>
</tbody>
</table>

To render and preview, execute the **Quarto: Preview** command. You can
alternatively use the <span class="kbd">Ctrl+Shift+K</span> keyboard
shortcut, or the **Preview** button at the top right of the editor:

<img src="../../../docs/tools/images/vscode-preview-button.png"
class="border img-fluid"
alt="The top of the Visual Studio code editor. The right side of the editor tab area includes a Preview button." />

Note that on the Mac you should use `Cmd` rather than `Ctrl` as the
prefix for all Quarto keyboard shortcuts.

### How it Works

When you render a `.qmd` file with Quarto, the executable code blocks
are processed by Jupyter, and the resulting combination of code,
markdown, and output is converted to plain markdown. Then, this markdown
is processed by [Pandoc](http://pandoc.org/), which creates the finished
format.

<img src="images/qmd-how-it-works.png"
class="img-fluid quarto-figure-left"
alt="Workflow diagram starting with a qmd file, then Jupyter, then md, then pandoc, then PDF, MS Word, or HTML." />

### Authoring

Let’s try making a small change and then re-rendering:

1.  Change the line of code that defines `theta` as follows:

        theta = 4 * np.pi * r

2.  Re-render the file (using **Quarto: Preview** or the <span
    class="kbd">Ctrl+Shift+K</span> shortcut) The document is rendered,
    and the browser preview is updated.

This is the basic workflow for authoring with Quarto.

You do not need to save the file before rendering (as this happens
automatically when you render). If you prefer, you can configure the
Quarto extension to render whenever you save a document. See the
documentation on [Render on
Save](../../../docs/tools/vscode.html#render-on-save) for additional
details.

### Running Cells

You don’t need to fully render documents in order to iterate on code
cells. You’ll notice that there is a **Run Cell** button above the code
cell. Click that button to execute the cell (output is shown side by
side in the Jupyter interactive console):

<img src="../../../docs/tools/images/vscode-execute-cell.png"
class="border img-fluid"
alt="VS Code with two panes open, vscode.qmd source code on the right, and the interactive output of that code shown in a second pane on the left." />

Execute the current cell with <span class="kbd">Ctrl+Shift+Enter</span>,
the current line(s) with <span class="kbd">Ctrl+Enter</span>, or
previous cells with <span class="kbd">Ctrl+Alt+P</span> (note that on
the Mac you should use `Cmd` rather than `Ctrl` as the prefix for all
Quarto keyboard shortcuts).

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

Then re-render the document (again, no need to save before rendering).
You’ll notice that the code is now shown above the plot, where
previously it was hidden with a **Code** button that could be used to
show it.

## Markdown

Narrative content is written using markdown. Here we specify a header
and a cross-reference to the figure created in the code cell below.

    ## Polar Axis

    For a demonstration of a line plot on a polar axis, see @fig-polar.

Try changing the header and re-rendering—the preview will update with
the new header text.

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
cross-reference-able. Try changing the `fig-cap` and/or the code then
re-rendering to see the updated preview.

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

## External Preview

In this tutorial we’ve demonstrated previewing rendered output in a pane
within VS Code. If you prefer to use an external browser for preview (or
have no preview triggered at all by rendering) you can use the **Preview
Type** option to specify an alternate behavior:

<img src="../../../docs/tools/images/vscode-preview-settings.png"
class="border img-fluid"
alt="VS Code settings interface with &#39;quarto preview type&#39; entered into the search bar. User settings reveals Quarto &gt; Render: Preview Type, with a dropdown to select location for document preview after render. The default, internal, is selected, which previews using a side-by-side panel in VS Code. The other two options in the dropdown are external and none." />

## Next Up

You now know the basics of creating and authoring Quarto documents. The
following tutorials explore Quarto in more depth:

-   [Tutorial: Computations](../computations/) — Learn how to tailor the
    behavior and output of executable code blocks.

-   [Tutorial: Authoring](../authoring/) — Learn more about output
    formats and technical writing features like citations, crossrefs,
    and advanced layout.

Additionally, may wish to learn about the other editing modes for Quarto
documents available within VS Code:

-   The [Visual Editor](../../../docs/visual-editor/vscode/index.html)
    for WYSIWYG editing of `.qmd` documents.

-   The [Notebook Editor](../../../docs/tools/vscode-notebook.html) for
    editing `.ipynb` notebooks.

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
