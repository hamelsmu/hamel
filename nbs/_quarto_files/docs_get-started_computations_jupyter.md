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
-   <a href="#cell-output" id="toc-cell-output" class="nav-link"
    data-scroll-target="#cell-output">Cell Output</a>
-   <a href="#code-folding" id="toc-code-folding" class="nav-link"
    data-scroll-target="#code-folding">Code Folding</a>
-   <a href="#multiple-figures" id="toc-multiple-figures" class="nav-link"
    data-scroll-target="#multiple-figures">Multiple Figures</a>
-   <a href="#next-up" id="toc-next-up" class="nav-link"
    data-scroll-target="#next-up">Next Up</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/get-started/computations/jupyter.qmd"
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
tutorial we’ll take a simple notebook that has some numeric output and
plots, and cover how to apply these options.

If you want to follow along step-by-step in your own environment,
download the notebook below:

<a href="_computations.ipynb" download="computations.ipynb">Download
computations.ipynb</a>

Then, create a new directory to work within and copy the notebook into
this directory.

Once you’ve done that, switch to this directory in a Terminal, install
notebook dependencies (if necessary), and open Jupyter Lab to get
started working with the notebook. The commands you can use for
installation and opening Jupyter Lab are given in the table below.

<table class="table" style="width:92%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 76%" />
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
class="sourceCode bash code-with-copy"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="ex">python3</span> <span class="at">-m</span> pip install jupyter matplotlib plotly</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="ex">python3</span> <span class="at">-m</span> jupyter lab computations.ipynb</span></code></pre></div>
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
class="sourceCode powershell code-with-copy"><code class="sourceCode powershell"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>py <span class="op">-</span>m pip install jupyter matplotlib plotly</span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>py <span class="op">-</span>m jupyter lab computations<span class="op">.</span><span class="fu">ipynb</span></span></code></pre></div>
</div>
</div></td>
</tr>
</tbody>
</table>

The notebook as we start out is shown below. Note that none of the cells
are executed yet.

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

<img src="images/jupyter-computations.png" class="border img-fluid"
alt="Screen shot of computations.ipynb Jupyter notebook with NumPy, Matplotlib, and Plotly code cells shown." />

Next, create a new Terminal within Jupyter Lab to use for Quarto
commands.

<img src="../hello/images/jupyter-terminal.png" class="border img-fluid"
alt="Screenshot of menu items in Jupuyter Lab: File &gt; New &gt; Terminal." />

Finally, run `quarto preview` in the Terminal, and position Jupyter Lab
side-by-side with the browser showing the preview.

    Terminal

    quarto preview computations.ipynb

<img src="images/jupyter-computations-preview.png"
class="border img-fluid"
alt="Side-by-side preview of notebook on the left and live preview in the browser on the right." />

Go ahead and run all of the cells and then save the notebook. You’ll see
that the preview updates immediately.

## Cell Output

All of the code in the notebook is displayed within the rendered
document. However, for some documents, you may want to hide all of the
code and just show the output. Let’s go ahead and specify `echo: false`
within the document `execute` options to prevent code from being
printed.

    ---
    title: Quarto Computations
    execute:
      echo: false
    jupyter: python3
    ---

<img src="images/jupyter-execute-echo-false.png"
class="border img-fluid"
alt="Screen shot of metadata section of Jupyter notebook with &#39;echo: false&#39; included under the &#39;execute:&#39; option." />

Save the notebook after making this change. The preview will update to
show the output with no code.

<img src="images/exec-echo-false-preview.png" class="border img-fluid"
alt="Output of notebook with echo: false set, shows resulting array in NumPy section, line chart in Numpy section, and interactive bubble chart in Plotly section." />

You might want to selectively enable code `echo` for some cells. To do
this add the `echo: true` cell option. Try this with the NumPy cell.

    ```{python}
    #| echo: true

    import numpy as np
    a = np.arange(15).reshape(3, 5)
    a
    ```

<img src="images/jupyter-exec-echo-true.png" class="border img-fluid"
alt="Screen shot of NumPy section of Jupyter notebook with &#39;echo: true&#39; set as a cell option for the code cell." />

Save the notebook and note that the code is now included for the NumPy
cell.

<img src="images/exec-echo-true-preview.png" class="border img-fluid"
alt="Screen shot of rendered NumPy section of Jupyter notebook which shows the code and the resulting array." />

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
    execute:
       code-fold: true
    jupyter: python3
    ---

<img src="images/jupyter-code-fold.png" class="border img-fluid"
alt="Screen shot of metadata section of Jupyter notebook with &#39;code-fold: true&#39; included under the &#39;html:&#39; option, which is under the `format:` option." />

Save the notebook. Now a “Code” widget is available above the output of
each cell.

<img src="images/code-fold-preview.png" class="border img-fluid"
alt="Screen shot of rendered NumPy section of Jupyter notebook which shows a toggleable section that is labelled &#39;Code&#39; and the resulting array." />

You can also provide global control over code folding. Try adding
`code-tools: true` to the HTML format options.

    ---
    title: Quarto Computations
    execute:
       code-fold: true
       code-tools: true
    jupyter: python3
    ---

<img src="images/jupyter-code-tools.png" class="border img-fluid"
alt="Metadata section of Jupyter notebook with &#39;code-tools: true&#39; added to the HTML format options." />

Save the notebook and you’ll see that a code menu appears at the top
right of the document that provides global control over showing and
hiding code.

<img src="images/code-tools-preview.png" class="border img-fluid"
alt="Output of notebook with &#39;code-tools: true&#39; which includes a Code dropdown button next to the document header with two options: Show All Code, and Hide All Code." />

    ```{python}
    #| label: fig-limits
    #| fig-cap: "Errorbar limit selector"

    import matplotlib.pyplot as plt

    fig = plt.figure()
    fig.set_size_inches(12, 7)
    ```

Let’s improve the appearance of our Matplotlib output. It could
certainly stand to be wider, and it would be nice to provide a caption
and a label for cross-referencing.

Go ahead and modify the Matplotlib cell to include `label` and `fig-cap`
options as well as a call to `fig.set_size_inches()` to set a larger
figure size with a wider aspect ratio.

    ```{python}
    #| label: fig-limits
    #| fig-cap: "Errorbar limit selector"

    import matplotlib.pyplot as plt

    fig = plt.figure()
    fig.set_size_inches(12, 7)
    ```

<img src="images/jupyter-figure-options.png" class="border img-fluid"
alt="Code cell with label and fig-cap options added, as well as a call to set the figure size explicitly." />

Execute the cell to see the updated plot. Then, save the notebook so
that the Quarto preview is updated.

<img src="images/figure-options-preview.png" class="border img-fluid"
alt="Output of Matplotlib section of notebook which includes a caption under the figure that reads &#39;Figure 1: Errorbar limit selection.&#39;" />

## Multiple Figures

The Plotly cell visualizes GDP and life expectancy data from a single
year (2007). Let’s plot another year next to it for comparison and add a
caption and subcaptions. Since this will produce a wider visualization
we’ll also use the `column` option to lay it out across the entire page
rather than being constrained to the body text column.

There are quite a few changes to this cell. Copy and paste the code
below into the notebook if you want to try them locally.

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

Run the modified cell then save the notebook. The preview will update as
follows:

<img src="images/plotly-preview.png" class="border img-fluid"
alt="Output of Plotly section which shows two charts side-by-side. The first has a caption below that reads &#39;(a) Gapminder: 1957&#39;, the second&#39;s caption reads &#39;(b) Gapminder 2007&#39;. Below both figures, there&#39;s a caption that reads &#39;Figure 1: Life Expectancy and GDP (Data from World Bank via gapminder.org).&#39;" />

Let’s discuss some of the new options used here. You’ve seen `fig-cap`
before but we’ve now added a `fig-subcap` option.

    #| fig-cap: "Life Expectancy and GDP"
    #| fig-subcap:
    #|   - "Gapminder: 1957"
    #|   - "Gapminder: 2007"

For code cells with multiple outputs adding the `fig-subcap` option
enables us to treat them as subfigures.

We also added an option to control how multiple figures are laid out—in
this case we specified side-by-side in two columns.

    #| layout-ncol: 2

If you have 3, 4, or more figures in a panel there are many options
available for customizing their layout. See the article on
[Figures](../../../docs/authoring/figures.html) for details.

Finally, we added an option to control the span of the page that our
figures occupy.

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
