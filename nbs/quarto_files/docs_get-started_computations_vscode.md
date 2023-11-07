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

1.  Tutorial: Computations

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
-   <a href="#cell-execution" id="toc-cell-execution" class="nav-link"
    data-scroll-target="#cell-execution">Cell Execution</a>
-   <a href="#cell-output" id="toc-cell-output" class="nav-link"
    data-scroll-target="#cell-output">Cell Output</a>
-   <a href="#code-folding" id="toc-code-folding" class="nav-link"
    data-scroll-target="#code-folding">Code Folding</a>
-   <a href="#figures" id="toc-figures" class="nav-link"
    data-scroll-target="#figures">Figures</a>
-   <a href="#multiple-figures" id="toc-multiple-figures" class="nav-link"
    data-scroll-target="#multiple-figures">Multiple Figures</a>
-   <a href="#next-up" id="toc-next-up" class="nav-link"
    data-scroll-target="#next-up">Next Up</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/get-started/computations/vscode.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Tutorial: Computations

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

Quarto has a wide variety of options available for controlling how code
and computational output appear within rendered documents. In this
tutorial we’ll take a `.qmd` file that has some numeric output and
plots, and cover how to apply these options.

This tutorial will make use of the `matplotlib` and `plotly` Python
packages. The commands you can use to install them are given in the
table below.

<table class="table" style="width:86%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 70%" />
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

If you want to follow along step-by-step in your own environment, create
a `computations.qmd` file and copy the following content into it.

    ---
    title: Quarto Computations
    jupyter: python3
    ---

    ## NumPy

    ```{python}
    import numpy as np
    a = np.arange(15).reshape(3, 5)
    a
    ```

    ## Matplotlib

    ```{python}
    import matplotlib.pyplot as plt

    fig = plt.figure()
    x = np.arange(10)
    y = 2.5 * np.sin(x / 20 * np.pi)
    yerr = np.linspace(0.05, 0.2, 10)

    plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
    plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
    plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
                 label='uplims=True, lolims=True')

    upperlimits = [True, False] * 5
    lowerlimits = [False, True] * 5
    plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
                 label='subsets of uplims and lolims')

    plt.legend(loc='lower right')
    plt.show(fig)
    ```

    ## Plotly

    ```{python}
    import plotly.express as px
    import plotly.io as pio
    gapminder = px.data.gapminder()
    gapminder2007 = gapminder.query("year == 2007")
    fig = px.scatter(gapminder2007, 
                     x="gdpPercap", y="lifeExp", color="continent", 
                     size="pop", size_max=60,
                     hover_name="country")
    fig.show()
    ```

Then, execute the **Quarto: Preview** command. You can alternatively use
the <span class="kbd">Ctrl+Shift+K</span> keyboard shortcut, or the
**Preview** button at the top right of the editor:

<img src="../../../docs/tools/images/vscode-preview-button.png"
class="border img-fluid"
alt="The top of the Visual Studio code editor. The right side of the editor tab area includes a Preview button." />

Note that on the Mac you should use `Cmd` rather than `Ctrl` as the
prefix for all Quarto keyboard shortcuts.

Here is what you should see within VS Code:

<img src="images/vscode-computations-preview.png"
class="border column-page-outset-right img-fluid"
alt="Side-by-side preview of text editor on the left and live preview in the browser on the right." />

## Cell Execution

As you author a document you may want to execute one or more cells
without re-rendering the entire document. You can do this using the
**Run Cell** button above the code cell. Click that button to execute
the cell (output is shown side by side in the Jupyter interactive
console):

<img src="../../../docs/tools/images/vscode-execute-cell.png"
class="border img-fluid"
alt="VS Code with two panes open, vscode.qmd source code on the right, and the interactive output of that code shown in a second pane on the left." />

There are a variety of commands and keyboard shortcuts available for
executing cells:

<table class="table">
<thead>
<tr class="header header">
<th>Quarto Command</th>
<th>Keyboard Shortcut</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td>Run Current Cell</td>
<td><kbd>⇧⌘ Enter</kbd></td>
</tr>
<tr class="even even">
<td>Run Selected Line(s)</td>
<td><kbd>⌘ Enter</kbd></td>
</tr>
<tr class="odd odd">
<td>Run Next Cell</td>
<td><kbd>⌥⌘ N</kbd></td>
</tr>
<tr class="even even">
<td>Run Previous Cell</td>
<td><kbd>⌥⌘ P</kbd></td>
</tr>
<tr class="odd odd">
<td>Run All Cells</td>
<td><kbd>⌥⌘ R</kbd></td>
</tr>
<tr class="even even">
<td>Run Cells Above</td>
<td><kbd>⇧⌥⌘ P</kbd></td>
</tr>
<tr class="odd odd">
<td>Run Cells Below</td>
<td><kbd>⇧⌥⌘ N</kbd></td>
</tr>
</tbody>
</table>

## Cell Output

All of the code in the source file is displayed within the rendered
document. However, in some cases, you may want to hide all of the code
and just show the output. Let’s go ahead and specify `echo: false`
within the document `execute` options to prevent code from being
printed.

    ---
    title: Quarto Computations
    execute:
      echo: false
    jupyter: python3
    ---

Re-render the document and the preview will update to show the output
with no code (remember that you do not need to save the file before
rendering, as this happens automatically when you render).

<img src="images/exec-echo-false-preview.png" class="border img-fluid"
alt="Output of computations.qmd with &#39;echo: false&#39; set, shows Title, resulting array in NumPy section, line chart in Matplotlib section, and interactive bubble chart in Plotly section." />

You might want to selectively enable code `echo` for some cells. To do
this add the `echo: true` cell option. Try this with the NumPy cell.

    ```{python}
    #| echo: true

    import numpy as np
    a = np.arange(15).reshape(3, 5)
    a
    ```

Re-render note that the code is now included for the NumPy cell.

<img src="images/exec-echo-true-preview.png" class="border img-fluid"
alt="Rendered NumPy section of computations.qmd which shows the code and the resulting array." />

There a large number of other options available for cell output, for
example `warning` to show/hide warnings (which can be especially helpful
for package loading messages), `include` as a catch all for preventing
any output (code or results) from being included in output, and `error`
to prevent errors in code execution from halting the rendering of the
document (and print the error in the rendered document).

See the [Jupyter Cell
Options](https://quarto.org/docs/reference/cells/cells-jupyter.html)
documentation for additional details.

## Code Folding

Rather than hiding code entirely, you might want to fold it and allow
readers to view it at their discretion. You can do this via the
`code-fold` option. Remove the `echo` option we previously added and add
the `code-fold` HTML format option.

    ---
    title: Quarto Computations
    format:
      html:
        code-fold: true
    jupyter: python3
    ---

Render the document. Now a “Code” widget is available above the output
of each cell.

<img src="images/code-fold-preview.png" class="border img-fluid"
alt="Rendered NumPy section of computations.qmd which shows a toggleable section that is labelled &#39;Code&#39; and the resulting array." />

You can also provide global control over code folding. Try adding
`code-tools: true` to the HTML format options.

    ---
    title: Quarto Computations
    format:
      html:
        code-fold: true
        code-tools: true
    jupyter: python3
    ---

Render the document and you’ll see that a code menu appears at the top
right of the document that provides global control over showing and
hiding code.

<img src="images/text-editor-code-tools-preview.png"
class="border img-fluid"
alt="Rendered version of the computations.qmd document. A new code widget appears on top right of the document. The screenshot shows that the widget is clicked on, which reveals a drop down menu with three choices: Show All Code, Hide All Code, and View Source. In the background is the rendered document. The title is followed by some text, which is followed by a Code widget that would expand if clicked on, which is followed by the output of the code. The Code widgets are folded, so the code is not visible in the rendered document." />

## Figures

Let’s improve the appearance of our Matplotlib output. It could
certainly stand to be wider, and it would be nice to provide a caption
and a label for cross-referencing.

Go ahead and modify the Matplotlib cell to include `label` and `fig-cap`
options as well as a call to `fig.set_size_inches()` to set a larger
figure size with a wider aspect ratio:

    ```{python}
    #| label: fig-limits
    #| fig-cap: "Errorbar limit selector"

    import matplotlib.pyplot as plt

    fig = plt.figure()
    fig.set_size_inches(12, 7)
    ```

After re-rendering the document you’ll see the updated plot:

<img src="images/figure-options-preview.png" class="border img-fluid"
alt="Rendered Matplotlib section of computations.qmd which includes a toggleable code-folding widget, the figure, and a caption under the figure that reads &#39;Figure 1: Errorbar limit selection.&#39;" />

## Multiple Figures

The Plotly cell visualizes GDP and life expectancy data from a single
year (2007). Let’s plot another year next to it for comparison and add a
caption and subcaptions. Since this will produce a wider visualization
we’ll also use the `column` option to lay it out across the entire page
rather than being constrained to the body text column.

There are quite a few changes to this cell. Copy and paste this code
into `computations.qmd` if you want to try them locally:

    #| label: fig-gapminder
    #| fig-cap: "Life Expectancy and GDP"
    #| fig-subcap:
    #|   - "Gapminder: 1957"
    #|   - "Gapminder: 2007"
    #| layout-ncol: 2
    #| column: page

    import plotly.express as px
    import plotly.io as pio
    gapminder = px.data.gapminder()
    def gapminder_plot(year):
        gapminderYear = gapminder.query("year == " + 
                                        str(year))
        fig = px.scatter(gapminderYear, 
                         x="gdpPercap", y="lifeExp",
                         size="pop", size_max=60,
                         hover_name="country")
        fig.show()
        
    gapminder_plot(1957)
    gapminder_plot(2007)

Render the document and the preview will update as follows:

<img src="images/plotly-preview.png" class="border img-fluid"
alt="Output of Plotly section which shows two charts side-by-side. The first has a caption below that reads &#39;(a) Gapminder: 1957&#39;, the second&#39;s caption reads &#39;(b) Gapminder 2007&#39;. Below both figures, there&#39;s a caption that reads &#39;Figure 1: Life Expectancy and GDP (Data from World Bank via gapminder.org).&#39;" />

Let’s discuss some of the new options used here. You’ve seen `fig-cap`
before but we’ve now added a `fig-subcap` option:

    #| fig-cap: "Life Expectancy and GDP"
    #| fig-subcap:
    #|   - "Gapminder: 1957"
    #|   - "Gapminder: 2007"

For code cells with multiple outputs adding the `fig-subcap` option
enables us to treat them as subfigures.

We also added an option to control how multiple figures are laid out—in
this case we specified side-by-side in two columns:

    #| layout-ncol: 2

If you have 3, 4, or more figures in a panel there are many options
available for customizing their layout. See the article
[Figures](../../../docs/authoring/figures.html) for details.

Finally, we added an option to control the span of the page that our
figures occupy:

    #| column: page

This allows our figure display to span out beyond the normal body text
column. See the documentation on [Article
Layout](../../../docs/authoring/article-layout.html) to learn about all
of the available layout options.

## Next Up

You’ve now covered the basics of customizing the behavior and output of
executable code in Quarto documents.

Next, check out the the [Authoring Tutorial](../authoring/) to learn
more about output formats and technical writing features like citations,
crossrefs, and advanced layout.

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
