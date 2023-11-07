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
-   <a href="#code-linking" id="toc-code-linking" class="nav-link"
    data-scroll-target="#code-linking">Code Linking</a>
-   <a href="#figures" id="toc-figures" class="nav-link"
    data-scroll-target="#figures">Figures</a>
-   <a href="#multiple-figures" id="toc-multiple-figures" class="nav-link"
    data-scroll-target="#multiple-figures">Multiple Figures</a>
-   <a href="#data-frames" id="toc-data-frames" class="nav-link"
    data-scroll-target="#data-frames">Data Frames</a>
-   <a href="#inline-code" id="toc-inline-code" class="nav-link"
    data-scroll-target="#inline-code">Inline Code</a>
-   <a href="#caching" id="toc-caching" class="nav-link"
    data-scroll-target="#caching">Caching</a>
-   <a href="#next-up" id="toc-next-up" class="nav-link"
    data-scroll-target="#next-up">Next Up</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/get-started/computations/rstudio.qmd"
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

Quarto supports executable code blocks within markdown. This allows you
to create fully reproducible documents and reports—the code required to
produce your output is part of the document itself, and is automatically
re-run whenever the document is rendered.

In this tutorial we’ll show you how to author fully reproducible
computational documents with Quarto in RStudio.

If you would like to follow along step-by-step in your own environment,
download the Quarto document (`.qmd`) below, open it in RStudio, and
click on <span
class="kbd"><img src="images/rstudio-render-button.png" width="25" height="20" /></span>
**Render** (or use the keyboard shortcut ⇧⌘K). We recommend also
checking the box for **Render on Save** for a live preview of your
changes.

<a href="_computations.qmd" download="computations.qmd">Download
computations.qmd</a>

Note that you will need to open this document in RStudio v2022.07 or
later, which you can download
[here](https://posit.co/download/rstudio-desktop/).

## Cell Output

By default, the code and its output are displayed within the rendered
document.

<img src="images/rstudio-computations-preview.png"
class="border column-page-right img-fluid"
alt="RStudio window with computations.qmd open in the visual editor (on the right) and the rendered document (on the left). The document is titled Quarto Computations and contains some text and code. The rendered version also shows a visualization." />

However, for some documents, you may want to hide all of the code and
just show the output. To do so, specify `echo: false` within the
`execute` option in the YAML.

    ---
    title: "Quarto Computations"
    execute:
      echo: false
    ---

If you checked **Render on Save** earlier, just save the document after
making this change for a live preview. Otherwise render the document to
see your updates reflected. The result will look like the following.

<img src="images/rstudio-exec-echo-false.png" class="border img-fluid"
alt="Rendered computations.qmd document with title Quarto Computations, some descriptive text, and a plot. Code is not shown." />

You might want to selectively enable code `echo` for some cells. To do
this add the `echo: true` cell option. Try this with the chunk labelled
`scatterplot`.

    #| label: scatterplot
    #| echo: true

    ggplot(mpg, aes(x = hwy, y = cty, color = cyl)) +
      geom_point(alpha = 0.5, size = 2) +
      scale_color_viridis_c() +
      theme_minimal()

Save the document again and note that the code is now included for the
`scatterplot` chunk.

<img src="images/rstudio-exec-echo-true-preview.png"
class="border img-fluid"
alt="Rendered computations.qmd document with title Quarto Computations, some descriptive text, and a plot. Code is shown for the plot, but not for package loading." />

The `echo` option can be set to `true`, `false`, or `fenced`. The last
one might be of special interest for writing documentation and teaching
materials as it allows you to include the fenced code delimiter in your
code output to emphasize that executable code requires that delimiter.
You can read more about this option in the [Fenced
Echo](https://quarto.org/docs/computations/execution-options.html#fenced-echo)
documentation.

There are a large number of other options available for cell output, for
example `warning` for showing/hiding warnings (which can be especially
helpful for package loading messages), `include` as a catch all for
preventing any output (code or results) from being included in output,
and `error` to prevent errors in code execution from halting the
rendering of the document (and print the error in the rendered
document).

See the [Knitr Cell
Options](https://quarto.org/docs/reference/cells/cells-knitr.html)
documentation for additional details.

## Code Folding

Rather than hiding code entirely, you might want to fold it and allow
readers to view it at their discretion. You can do this via the
`code-fold` option. Remove the `echo` option we previously added and add
the `code-fold` HTML format option.

    ---
    title: "Quarto Computations"
    format:
      html:
        code-fold: true
    ---

Save the document again and note that new Code widgets are now included
for each code chunk.

<img src="images/rstudio-code-fold-preview.png"
class="border column-page-right img-fluid"
alt="RStudio with computations.qmd open. On the right is the visual editor. The YAML has title and format defined. Title is Quarto Computations. Format is html, and code-fold option is set to true. On the right is the rendered version of the document. The title is followed by some text, which is followed by a Code widget that would expand if clicked on, which is followed by some more text, another code widget, and finally the plot. The Code widgets are folded, so the code is not visible in the rendered document." />

You can also provide global control over code folding. Try adding
`code-tools: true` to the HTML format options.

    ---
    title: "Quarto Computations"
    format:
      html:
        code-fold: true
        code-tools: true
    ---

Save the document and you’ll see that a code menu appears at the top
right of the rendered document that provides global control over showing
and hiding all code.

<img src="images/rstudio-code-tools-preview.png"
class="border img-fluid"
alt="Rendered version of the computations.qmd document. A new code widget appears on top right of the document. The screenshot shows that the widget is clicked on, which reveals a drop down menu with three choices: Show All Code, Hide All Code, and View Source. In the background is the rendered document. The title is followed by some text, which is followed by a Code widget that would expand if clicked on, which is followed by some more text, another code widget, and finally the plot. The Code widgets are folded, so the code is not visible in the rendered document." />

## Code Linking

The `code-link` option enables hyper-linking of functions within code
blocks to their online documentation. Try adding `code-link: true` to
the HTML format options.

    ---
    title: "Quarto Computations"
    format:
      html:
        code-link: true
    ---

Save the document and observe that the functions are now clickable
hyperlinks.

<img src="images/rstudio-code-link-preview.png"
class="column-page-right img-fluid"
alt="Rendered version of the computations.qmd document. The document contains a title (Quarto Computations), text, code chunks, and a plot. The screenshot shows that function names in code chunks are clickable, and clicking on one brings you to documentation on the package website (which is shown on the foreground of the image). The function shown is theme_minimal() from ggplot2." />

Note that code linking is currently implemented only for the knitr
engine via the [downlit](https://downlit.r-lib.org/) package. A
limitation of downlit currently prevents code linking if
`code-line-numbers` and/or `code-annotations` are also `true`.

## Figures

We can improve the appearance and accessibility of our plot. We can
change its aspect ratio by setting `fig-width` and `fig-height`, provide
a `fig-cap`, modify its `label` for cross referencing, and add
[alternative
text](https://medium.com/nightingale/writing-alt-text-for-data-visualization-2a218ef43f81)
with `fig-alt`.

We’ll add the following chunk options.

    #| label: fig-scatterplot
    #| fig-cap: "City and highway mileage for 38 popular models of cars."
    #| fig-alt: "Scatterplot of city vs. highway mileage for cars, where points are colored by the number of cylinders. The plot displays a positive, linear, and strong relationship between city and highway mileage, and mileage increases as the number of cylinders decreases."
    #| fig-width: 6
    #| fig-height: 3.5

Save the document to see the updated plot. Note that we have also
updated the narrative with a [cross
reference](https://quarto.org/docs/authoring/cross-references.html#computations)
to this figure using the following.

    @fig-scatterplot shows a positive, strong, and linear relationship between the city and highway mileage of these cars.

<img src="images/rstudio-figure-options.png"
class="border column-page-right img-fluid"
alt="RStudio with computations.qmd open. On the right is the visual editor. The YAML has title and format defined. Title is Quarto Computations. Format is html, and code-fold option is set to true. Compared to earlier images on the page, the code chunk shows the new chunk options added to the code chunk. On the right is the rendered version of the document. The title is followed by some text, which is followed by a Code widget that would expand if clicked on, which is followed by some more text, another code widget, and finally the plot. The Code widgets are folded, so the code is not visible in the rendered document." />

## Multiple Figures

Let’s add another plot to our chunk—a scatterplot where the points are
colored by engine displacement, using a different color scale. Our goal
is to display these plots side-by-side (i.e., in two columns), with a
descriptive subcaption for each plot. Since this will produce a wider
visualization we’ll also use the `column` option to lay it out across
the entire page rather than being constrained to the body text column.

There are quite a few changes to this chunk. To follow along, copy and
paste the options outlined below into your Quarto document.

    #| label: fig-mpg
    #| fig-cap: "City and highway mileage for 38 popular models of cars."
    #| fig-subcap:
    #|   - "Color by number of cylinders"
    #|   - "Color by engine displacement, in liters"
    #| layout-ncol: 2
    #| column: page

    ggplot(mpg, aes(x = hwy, y = cty, color = cyl)) +
      geom_point(alpha = 0.5, size = 2) +
      scale_color_viridis_c() +
      theme_minimal()

    ggplot(mpg, aes(x = hwy, y = cty, color = displ)) +
      geom_point(alpha = 0.5, size = 2) +
      scale_color_viridis_c(option = "E") +
      theme_minimal()

Additionally, replace the existing text that describes the visualization
with the following.

    The plots in @fig-mpg show the relationship between city and highway mileage for 38 popular models of cars.
    In @fig-mpg-1 the points are colored by the number of cylinders while in @fig-mpg-2 the points are colored by engine displacement.

Then, save the document and inspect the rendered output, which should
look like the following.

<img src="images/rstudio-multi-figure-preview.png"
class="border img-fluid"
alt="Rendered version of the computations.qmd document with a new plot. The document contains a title (Quarto Computations), text, code chunks, and figure include two side-by-side subfigures, each scatterplots. The text shows clickable cross reference links to Figure 1, Figure 1a, and Figure 1b." />

Let’s discuss some of the new options used here. You’ve seen `fig-cap`
before but we’ve now added a `fig-subcap` option.

    #| fig-cap: "City and highway mileage for 38 popular models of cars."
    #| fig-subcap:
    #|   - "Color by number of cylinders"
    #|   - "Color by engine displacement, in liters"

For code cells with multiple outputs adding the `fig-subcap` option
enables us to treat them as subfigures.

We also added an option to control how multiple figures are laid out—in
this case we specified side-by-side in two columns.

    #| layout-ncol: 2

If you have 3, 4, or more figures in a panel there are many options
available for customizing their layout. See the article [Figure
Layout](../../../docs/authoring/figures.html#figure-panels) for details.

Finally, we added an option to control the span of the page that our
figures occupy.

    #| column: page

This allows our figure display to span out beyond the normal body text
column. See the documentation on [Article
Layout](../../../docs/authoring/article-layout.html) to learn about all
of the available layout options.

## Data Frames

You can control how data frames are printed by default using the
`df-print` document option. Available options include:

<table class="table">
<thead>
<tr class="header header">
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td><code>default</code></td>
<td>Use the default S3 method for the data frame.</td>
</tr>
<tr class="even even">
<td><code>kable</code></td>
<td>Markdown table using the <a
href="https://bookdown.org/yihui/rmarkdown-cookbook/kable.html"><code>knitr::kable()</code></a>
function.</td>
</tr>
<tr class="odd odd">
<td><code>tibble</code></td>
<td>Plain text table using the <a
href="https://tibble.tidyverse.org/"><code>tibble</code></a>
package.</td>
</tr>
<tr class="even even">
<td><code>paged</code></td>
<td>HTML table with paging for row and column overflow (implemented
using <a
href="https://pkgs.rstudio.com/rmarkdown/reference/paged_table.html"><code>rmarkdown::paged_table()</code></a>)</td>
</tr>
</tbody>
</table>

For example, here we specify that we want `paged` printing for data
frames:

    ---
    title: "Document"
    format: 
       html:
         df-print: paged
    ---

## Inline Code

To include executable expressions within markdown, enclose the
expression in `` `r ` ``. For example, we can use inline code to state
the number of observations in our data. Try adding the following
markdown text to your Quarto document.

    There are `r nrow(mpg)` observations in our data. 

Save your document and inspect the rendered output. The expression
inside the backticks has been executed and the sentence includes the
actual number of observations.

There are 234 observations in our data.

If the expression you want to inline is more complex, involving many
functions or a pipeline, we recommend including it in a code chunk (with
`echo: false`) and assigning the result to an object. Then, you can call
that object in your inline code.

For example, say you want to state the average city and highway mileage
in your data. First, compute these values in a code chunk.

    #| echo: false

    mean_cty <- round(mean(mpg$cty), 2)
    mean_hwy <- round(mean(mpg$hwy), 2)

Then, add the following markdown text to your Quarto document.

    The average city mileage of the cars in our data is `r mean_cty` and the average highway mileage is `r mean_hwy`. 

Save your document and inspect the rendered output.

The average city mileage of the cars in our data is 16.86 and the
average highway mileage is 23.44.

## Caching

If your document includes code chunks that take too long to compute, you
might want to cache the results of those chunks. You can use the `cache`
option either at the document level using the YAML execute option.

    execute:
      cache: true

However caching all code chunks in a document may not be preferable. You
can also indicate which chunks should be cached directly with using a
chunk option.

    #| cache: true

Try adding this chunk option to one of the code chunks in your document
that produces a plot and save. When the document is rendered, you’ll see
that a new folder has been created in your working directory with the
same name as your document and the suffix `_cache`. This folder contains
the cached results. You can find out more about caching in Quarto
documents in the
[Cache](https://quarto.org/docs/projects/code-execution.html#cache)
documentation.

If you followed along step-by-step with this tutorial, you should now
have a Quarto document that implements everything we covered. Otherwise,
you can download a completed version of `computations.qmd` below.

<a href="_computations-complete.qmd"
download="computations-complete.qmd">Download
computations-complete.qmd</a>

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
