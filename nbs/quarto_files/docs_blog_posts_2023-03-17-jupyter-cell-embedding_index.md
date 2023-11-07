<a href="../../../../index.html"
class="navbar-brand navbar-brand-logo"><img src="../../../../quarto.png"
class="navbar-logo" alt="Quarto logo." /></a>

<span class="navbar-toggler-icon"></span>

-   <a href="../../../../index.html" class="nav-link"><span
    class="menu-text">Overview</span></a>
-   <a href="../../../../docs/get-started/index.html" class="nav-link"><span
    class="menu-text">Get Started</span></a>
-   <a href="../../../../docs/guide/index.html" class="nav-link"><span
    class="menu-text">Guide</span></a>
-   <a href="../../../../docs/extensions/index.html" class="nav-link"><span
    class="menu-text">Extensions</span></a>
-   <a href="../../../../docs/reference/index.html" class="nav-link"><span
    class="menu-text">Reference</span></a>
-   <a href="../../../../docs/gallery/index.html" class="nav-link"><span
    class="menu-text">Gallery</span></a>
-   <a href="../../../../docs/blog/index.html" class="nav-link"><span
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
    -   <a href="../../../../docs/faq/index.html"
        class="dropdown-item"><em></em> <span
        class="dropdown-text">FAQ</span></a>

<a href="https://twitter.com/quarto_pub"
class="quarto-navigation-tool px-1" aria-label="Quarto Twitter"
title="Quarto Twitter"><em></em></a>
<a href="https://github.com/quarto-dev/quarto-cli"
class="quarto-navigation-tool px-1" aria-label="Quarto GitHub"
title="Quarto GitHub"><em></em></a>
<a href="https://quarto.org/docs/blog/index.xml"
class="quarto-navigation-tool px-1" aria-label="Quarto Blog RSS"
title="Quarto Blog RSS"><em></em></a>

# Jupyter Notebook Cell Embedding

Embed output from an external Jupyter Notebook in a Quarto document

Quarto 1.3 adds support for embedding cells from a Jupyter Notebook into
a Quarto document via an `embed` shortcode. In HTML documents, links are
automatically added that point to a rendered version of the external
notebook.

Features

Authoring

Quarto 1.3

Author

Charlotte Wickham

Published

March 17, 2023

## Notebooks

-   [Palmer Penguins](penguins-preview.html)

Quarto 1.3 Feature

This post is part of a series highlighting new features in the 1.3
release of Quarto. Get the latest release at
<https://quarto.org/docs/download>.

Starting in Quarto 1.3, you can include the output of an external
Jupyter notebook in a Quarto document with the `embed` shortcode. To
embed a notebook cell, provide the path to a Jupyter Notebook and a cell
identifier. For example, this notebook called `penguins.ipynb` has a
cell labelled `fig-bill-scatter`:

<img src="notebook-simple.png" class="img-fluid"
alt="A screenshot of a Jupyter Notebook with the name &#39;penguins.ipynb&#39;, with a cell highlighted that has the code chunk option label set to fig-bill-scatter. Below the cell is a plot that has been output." />

You can use the following shortcode to embed the output of this cell:

    {{< embed penguins.ipynb#fig-bill-scatter >}}

This will embed the plot as follows:

Figure 1: A scatterplot of bill dimensions for penguins, made with
Altair.

<a href="penguins-preview.html#cell-fig-bill-scatter" id="nblink-1"
class="quarto-notebook-link">Source: Palmer Penguins</a>

A link to the source notebook is automatically provided beneath the
plot. Following the link takes users to a rendered version of the
notebook, allowing them to explore the notebook without having to
download and run it locally. For example, clicking on the link to
`penguins.ipynb` gets you to a page that looks like the following:

<img src="notebook-view.png" class="border img-fluid"
alt="A screenshot of webpage with the title &#39;penguins.ipynb&#39;, a large blue button labelled &#39;Download Notebook&#39;, followed by the notebook contents." />

Beyond this basic usage, head to the [Jupyter Cell Embedding highlight
docs](../../../../docs/authoring/notebook-embed.html) to learn how to:

-   Specify cells in multiple ways, see [Specifying
    Cells](../../../../docs/authoring/notebook-embed.html#specifying-cells).

-   Control the output using code cell options in the source Notebook,
    including things like figure captions, figure layout, and code
    display, see [Code Cell
    Options](../../../../docs/authoring/notebook-embed.html#code-cell-options).

-   Include the cell code along with the output by adding an `echo`
    option to the shortcode, see [Embedding
    Code](../../../../docs/authoring/notebook-embed.html#embedding-code).

-   Customize or exclude the link to the source notebook, see [Links to
    Source
    Notebooks](../../../../docs/authoring/notebook-embed.html#linked-source-notebooks).

Subscribe

<span style="font-size: 0.9em;">Enjoy this blog? Get notified of new
posts by email:</span>

Proudly supported by [<img
src="https://www.rstudio.com/assets/img/posit-logo-fullcolor-TM.svg"
class="img-fluid" width="65" alt="Posit" />](https://posit.co)

-   <a href="../../../../about.html" class="nav-link"></a>

    About

-   <a href="../../../../docs/faq/index.html" class="nav-link"></a>

    FAQ

-   <a href="../../../../license.html" class="nav-link"></a>

    License

-   <a href="../../../../trademark.html" class="nav-link"></a>

    Trademark

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/blog/posts/2023-03-17-jupyter-cell-embedding/index.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
