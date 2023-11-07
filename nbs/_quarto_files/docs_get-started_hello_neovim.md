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
-   <a href="#code-cells" id="toc-code-cells" class="nav-link"
    data-scroll-target="#code-cells">Code Cells</a>
-   <a href="#next-up" id="toc-next-up" class="nav-link"
    data-scroll-target="#next-up">Next Up</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/get-started/hello/neovim.qmd"
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

In this tutorial we’ll show you how to use Quarto with Neovim. While we
cover the basics here, you will also want to review the article on
[Using Neovim with Quarto](../../../docs/tools/neovim.html) to learn
more about installing, using, and customizing Neovim for Quarto.

If you already have Neovim configured to your liking, you may only want
to add the [quarto-nvim](https://github.com/quarto-dev/quarto-nvim)
plugin and only refer to this guide for inspiration and seeing the
possibilities. But if you are entirely new to Neovim or want to simply
try out a configuration already set up for data science with Quarto, you
should head over to this [kickstarter
configuration](https://github.com/jmbuhr/quarto-nvim-kickstarter). This
is also what we will be using for this tutorial.

Note

Neovim is a highly customizable editor. So much so that Neovim core
member TJ Devries has recently coined the term Personal Development
Environments (PDE)<a href="#fn1" id="fnref1" class="footnote-ref"
role="doc-noteref"><sup>1</sup></a> to separate the concept from
Integrated Development Environments (IDEs) such as VS Code and RStudio.

Out of the box neovim is fairly minimal. To work efficiently and get all
the nice features, you have to configure it. You have to make it your
own. If this approach sounds enticing to you, read on. Welcome to the
rabbit hole. 🐰

You can also watch [this video](https://youtu.be/3sj7clNowlA) for a
quick guide to getting started with the kickstarter configuration
alongside this write-up.

# An error occurred.

<a href="https://www.youtube.com/watch?v=3sj7clNowlA"
target="_blank">Try watching this video on www.youtube.com</a>, or
enable JavaScript if it is disabled in your browser.

The Quarto Neovim plugin aims to not reinvent the wheel. Existing
plugins in the Neovim ecosystem are leveraged to provide the full
experience. Some of the features provided by `quarto-nvim` and enhanced
by plugins found in the kickstarter configuration are:

-   Preview for Quarto documents.
-   Syntax highlighting for markdown and embedded languages
-   Completion for embedded languages (e.g. Python, R, Julia, etc.)
-   Commands and key-bindings for running cells and selected lines.
-   Completion for bibliography references, file paths, LaTeX math
    symbols, emoji.
-   Optional spellchecking and completion.
-   Code snippets.
-   Export of code chunks into standalone scripts.

See the article on [Using Neovim with
Quarto](../../../docs/tools/neovim.html) for all of the details.

### Basic Workflow

Quarto `.qmd` files contain a combination of markdown and executable
code cells. Here’s what it might look like in Neovim to edit and preview
a `.qmd` file:

<img src="./images/neovim-overview.png" class="border img-fluid"
alt="Three windows arranged side by side. The window on the left is a qmd file opened in Neovim. The upper window on the right is a web browser. The contents of the qmd document are rendered by Quarto in the browser window. The third window is a rendered graph showing the output of executing a code chunk in the qmd file." />

The document on the right is *rendered* into the HTML version you see on
the left. This is the basic model for Quarto publishing—take a source
document and render it to a variety of [output
formats](https://quarto.org/docs/output-formats/all-formats.html),
including HTML, PDF, MS Word, etc.

The tutorials will make use of the `matplotlib` and `plotly` Python
packages—the commands you can use to install them are given in the table
below.

<table class="table" style="width:91%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 75%" />
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
[IJulia](https://julialang.github.io/IJulia.jl/stable/) kernel) or using
R (via the [knitr package](https://github.com/yihui/knitr)), are also
well supported. See the articles on [Using
Julia](../../../docs/computations/julia.html) and [Using
R](../../../docs/computations/r.html) for additional details.

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
    ax.plot(theta, r);
    ax.set_rticks([0.5, 1, 1.5, 2]);
    ax.grid(True);
    plt.show()
    ```

To render and preview, execute the **QuartoPreview** command by pressing
`:` to enter command mode and typing the command (there is
autocompletion if you press the <span class="kbd">tab</span> key). In
the kickstarter configuration, there are more shortcuts starting with
<span class="kbd">space q</span> (spacebar followed by q, in normal
mode).

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

2.  Save the file using either `:w` in normal mode or `ctrl-s`
    <a href="#fn2" id="fnref2" class="footnote-ref"
    role="doc-noteref"><sup>2</sup></a>

The document is rendered, and the browser preview is updated. This is
the basic workflow for authoring with Quarto.

### Running Cells

You don’t need to fully render documents in order to iterate on code
cells. With the provided configuration we can open a terminal of our
choosing using the leader key (`<space>`) followed by`c` (for code) and
then `p` (for python) or `i` (for ipython).

If you wait a little in between the key presses a small window pops up
at the bottom of your screen to tell you about existing keybindings:

<img
src="../../../docs/get-started/hello/images/neovim-open-terminal.png"
class="img-fluid" />

We can navigate between the code and the terminal using `ctrl` plus vim
direction keys and enter commands into the python REPL by going into
insert mode in this terminal buffer.

To send code to the python REPL from quarto we navigate to one of our
code blocks and press `<space><cr>` (space bar followed by Enter). The
plugin responsible for sending code to various places,
[vim-slime](https://github.com/jpalardy/vim-slime) will prompt us with
the question which terminal to send the code to, pre filled with the
latest terminal we created.

<img src="../../../docs/get-started/hello/images/neovim-send-code.png"
class="img-fluid" />

If you want to use <span class="kbd">ctrl+Enter</span> to send code just
like in RStudio, you are going to have to tell your terminal emulator to
send the correct key codes. For example, in the
[kitty](https://github.com/kovidgoyal/kitty) terminal the configuration
looks as follows:

    map ctrl+shift+enter no_op
    map shift+enter send_text all \x1b[13;2u
    map ctrl+enter send_text all \x1b[13;5u

This is what the kickstarter configuration has been tested with.

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

Then re-render the document by saving it. You’ll notice that the code is
now shown above the plot, where previously it was hidden with a **Code**
button that could be used to show it.

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

## Next Up

You now know the basics of creating and authoring Quarto documents. The
following tutorials explore Quarto in more depth:

-   [Tutorial: Computations](../computations/) — Learn how to tailor the
    behavior and output of executable code blocks.

-   [Tutorial: Authoring](../authoring/) — Learn more about output
    formats and technical writing features like citations, crossrefs,
    and advanced layout.

See the article on [Using Neovim with
Quarto](../../../docs/tools/neovim.html) to learn more about installing,
using, and customizing Neovim for Quarto.

## Footnotes

1.  In [this
    video](https://www.youtube.com/watch?v=QMVIJhC9Veg)<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a>

2.  if you are using the kickstarter configuration – otherwise `ctrl-s`
    puts your terminal in a waiting mode until you press `ctrl+q`, which
    can be
    confusing<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a>

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
