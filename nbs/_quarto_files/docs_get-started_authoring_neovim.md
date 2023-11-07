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

1.  Tutorial: Authoring

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
-   <a href="#output-formats" id="toc-output-formats" class="nav-link"
    data-scroll-target="#output-formats">Output Formats</a>
    -   <a href="#format-options" id="toc-format-options" class="nav-link"
        data-scroll-target="#format-options">Format Options</a>
    -   <a href="#multiple-formats" id="toc-multiple-formats" class="nav-link"
        data-scroll-target="#multiple-formats">Multiple Formats</a>
-   <a href="#rendering" id="toc-rendering" class="nav-link"
    data-scroll-target="#rendering">Rendering</a>
-   <a href="#sections" id="toc-sections" class="nav-link"
    data-scroll-target="#sections">Sections</a>
-   <a href="#equations" id="toc-equations" class="nav-link"
    data-scroll-target="#equations">Equations</a>
-   <a href="#citations" id="toc-citations" class="nav-link"
    data-scroll-target="#citations">Citations</a>
-   <a href="#cross-references" id="toc-cross-references" class="nav-link"
    data-scroll-target="#cross-references">Cross References</a>
-   <a href="#callouts" id="toc-callouts" class="nav-link"
    data-scroll-target="#callouts">Callouts</a>
-   <a href="#article-layout" id="toc-article-layout" class="nav-link"
    data-scroll-target="#article-layout">Article Layout</a>
-   <a href="#learning-more" id="toc-learning-more" class="nav-link"
    data-scroll-target="#learning-more">Learning More</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/get-started/authoring/neovim.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Tutorial: Authoring

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

In this tutorial we’ll explore more of Quarto’s authoring features.
We’ll cover rendering documents in multiple formats and show you how to
add components like table of contents, equations, citations,
cross-references, and more.

## Output Formats

Quarto supports rendering notebooks to dozens of different [output
formats](../../../docs/output-formats/all-formats.html). By default, the
`html` format is used, but you can specify an alternate format (or
formats) within document options.

### Format Options

Let’s create a new file (`authoring.qmd`) and define various formats for
it to be rendered to, adding some options to each of the formats. As a
reminder, document options are specified in YAML at the beginning of the
source file.

    ---
    title: "Quarto Document"
    author: "Norah Jones"
    format: pdf
    ---

We specified `pdf` as the default output format (if we exclude the
`format` option then it will default to `html`).

Let’s add some options to control our PDF output.

    ---
    title: "Quarto Document"
    author: "Norah Jones"
    format: 
      pdf: 
        toc: true
        number-sections: true
    ---

### Multiple Formats

Some documents you create will have only a single output format, however
in many cases it will be desirable to support multiple formats. Let’s
add the `html` and `docx` formats to our document.

    ---
    title: "Quarto Document"
    author: "Norah Jones"
    toc: true
    number-sections: true
    highlight-style: pygments
    format: 
      html: 
        code-fold: true
        html-math-method: katex
      pdf: 
        geometry: 
          - top=30mm
          - left=20mm
      docx: default
    ---

There’s a lot to take in here! Let’s break it down a bit. The first two
lines are generic document metadata that aren’t related to output
formats at all.

    title: "Quarto Document"
    author: "Norah Jones"

The next three lines are document format options that *apply to all
formats*. which is why they are specified at the root level.

    toc: true
    number-sections: true
    highlight-style: pygments

Next, we have the `format` option, where we provide format-specific
options.

    format:
      html: 
        code-fold: true
        html-math-method: katex
      pdf:
        geometry: 
          - top=30mm
          - left=30mm
      docx: default

The `html` and `pdf` formats each provide an option or two. For example,
for the HTML output we want the user to have control over whether to
show or hide the code (`code-fold: true`) and use `katex` for math text.
For PDF we define some margins. The `docx` format is a bit different—it
specifies `docx: default`. This means just use all of the default
options for the format.

## Rendering

The formats specified within document options define what is rendered by
default. If we render the document with all the options given above
using the following.

    Terminal

    quarto render authoring.qmd

Then the following files would be created.

-   `authoring.html`
-   `authoring.pdf`
-   `authoring.docx`

We can select one or more formats using the `--to` option.

    Terminal

    quarto render authoring.qmd --to docx
    quarto render authoring.qmd --to docx,pdf

Note that the target file (in this case `authoring.qmd`) should always
be the very first command line argument.

If needed we can also render formats that aren’t specified within
document options.

    Terminal

    quarto render authoring.qmd --to odt

Since the `odt` format isn’t included within document options, the
default options for the format will be used.

## Sections

You can use a table of contents and/or section numbering to make it
easier for readers to navigate your document. Do this by adding the
`toc` and/or `number-sections` options to document options. Note that
these options are typically specified at the root level because they are
shared across all formats.

    ---
    title: Quarto Basics
    author: Norah Jones
    date: 'May 22, 2021'
    toc: true
    number-sections: true
    ---

    ## Colors

    - Red
    - Green 
    - Blue

    ## Shapes

    - Square
    - Circle
    - Triangle

    ## Textures

    - Smooth
    - Bumpy
    - Fuzzy

Here’s what this document looks like when rendered to HTML.

<img src="images/sections-render.png" class="border img-fluid" />

There are lots of options available for controlling how the table of
contents and section numbering behave. See the output format
documentation
(e.g. [HTML](../../../docs/output-formats/html-basics.html),
[PDF](../../../docs/output-formats/pdf-basics.html), [MS
Word](../../../docs/output-formats/ms-word.html)) for additional
details.

## Equations

You can use LaTeX equations within markdown.

    Einstein's theory of special relatively that expresses the equivalence of mass and energy:

    $E = mc^{2}$

This appears as follows when rendered.

Einstein’s theory of special relatively that expresses the equivalence
of mass and energy:

<span class="math inline">\\(E = mc^{2}\\)</span>

Inline equations are delimited with `$…$`. To create equations in a new
line (display equation) use `$$…$$`. See the documentation on [markdown
equations](../../../docs/authoring/markdown-basics.html#equations) for
additional details.

## Citations

To cite other works within a Quarto document. First create a
bibliography file in a supported format (BibTeX or CSL). Then, link the
bibliography to your document using the `bibliography` YAML metadata
option.

Here’s a document that includes a bibliography and single citation.

    ---
    title: Quarto Basics
    format: html
    bibliography: references.bib
    jupyter: python3
    ---

    ## Overview

    Knuth says always be literate [@knuth1984].

    ```{python}
    1 + 1
    ```

    ## References

Note that items within the bibliography are cited using the `@citeid`
syntax.

     Knuth says always be literate [@knuth1984].

References will be included at the end of the document, so we include a
`## References` heading at the bottom of the source file.

Here is what this document looks like when rendered.

<img
src="../../../docs/get-started/authoring/images/citations-render.png"
class="border img-fluid" width="600"
alt="Rendered document with references section at the bottom the content of which reads &#39;Knuth, Donald E. 1984. Literate Programming. The Computer Journal 27 (2): 97-111.&#39;" />

  
The `@` citation syntax is very flexible and includes support for
prefixes, suffixes, locators, and in-text citations. See the
documentation on [Citations and
Footnotes](../../../docs/authoring/footnotes-and-citations.html) to
learn more.

## Cross References

Cross-references make it easier for readers to navigate your document by
providing numbered references and hyperlinks to figures, tables,
equations, and sections. Cross-reference-able entities generally require
a label (unique identifier) and a caption.

This example illustrates cross-referencing various types of entities.

    ---
    title: Quarto Crossrefs
    format: html
    jupyter: python3
    ---

    ## Overview

    See @fig-simple in @sec-plot for a demonstration of a simple plot. 

    See @eq-stddev to better understand standard deviation.

    ## Plot {#sec-plot}

    ```{python}
    #| label: fig-simple
    #| fig-cap: "Simple Plot"
    import matplotlib.pyplot as plt
    plt.plot([1,23,2,4])
    plt.show()
    ```

    ## Equation {#sec-equation}

    $$
    s = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \overline{x})^2}
    $$ {#eq-stddev}

We cross-referenced sections, figures, and equations. The table below
shows how we expressed each of these.

<table class="table">
<colgroup>
<col style="width: 20%" />
<col style="width: 30%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header header">
<th>Entity</th>
<th>Reference</th>
<th>Label / Caption</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td>Section</td>
<td><code>@sec-plot</code></td>
<td><p>ID added to heading:</p>
<div id="cb15" class="sourceCode" data-code-copy="false">
<div class="sourceCode" id="cb1"><pre
class="sourceCode default code-with-copy"><code class="sourceCode default"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a># Plot {#sec-plot}</span></code></pre></div>
</div></td>
</tr>
<tr class="even even">
<td>Figure</td>
<td><code>@fig-simple</code></td>
<td><p>YAML options in code cell:</p>
<div id="cb16" class="sourceCode" data-code-copy="false">
<div class="sourceCode" id="cb2"><pre
class="sourceCode default code-with-copy"><code class="sourceCode default"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>#| label: fig-simple</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>#| fig-cap: &quot;Simple Plot&quot;</span></code></pre></div>
</div></td>
</tr>
<tr class="odd odd">
<td>Equation</td>
<td><code>@eq-stddev</code></td>
<td><p>At end of display equation:</p>
<div id="cb17" class="sourceCode">
<div class="sourceCode" id="cb3"><pre
class="sourceCode default code-with-copy"><code class="sourceCode default"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>$$ {#eq-stddev}</span></code></pre></div>
</div></td>
</tr>
</tbody>
</table>

And finally, here is what this document looks like when rendered.

<img
src="../../../docs/get-started/authoring/images/crossref-render.png"
class="border img-fluid" width="600"
alt="Rendered page with linked cross references to figures and equations." />

See the article on [Cross
References](../../../docs/authoring/cross-references.html) to learn
more, including how to customize caption and reference text (e.g. use
“Fig.” rather than “Figure”).

## Callouts

Callouts are an excellent way to draw extra attention to certain
concepts, or to more clearly indicate that certain content is
supplemental or applicable to only some scenarios.

Callouts are markdown divs that have special callout attributes. To
create a callout within a markdown cell, type the following in your
document.

    ::: {.callout-note}
    Note that there are five types of callouts, including:
    `note`, `tip`, `warning`, `caution`, and `important`.
    :::

This appears as follows when rendered.

Note

Note that there are five types of callouts, including `note`, `tip`,
`warning`, `caution`, and `important`.

You can learn more about the different types of callouts and options for
their appearance in the
[Callouts](../../../docs/authoring/callouts.html) documentation.

## Article Layout

The body of Quarto articles have a default width of approximately 700
pixels. This width is chosen to [optimize
readability](https://medium.com/ben-shoemate/optimum-web-readability-max-and-min-width-for-page-text-dee9987a27a0).
This normally leaves some available space in the document margins and
there are a few ways you can take advantage of this space.

In this example, we use the `reference-location` option to indicate that
we would like footnotes to be placed in the right margin.

We also use the `column: screen-inset` cell option to indicate we would
like our figure to occupy the full width of the screen, with a small
inset.

    ---
    title: Quarto Layout
    format: html
    reference-location: margin
    jupyter: python3
    ---

    ## Placing Colorbars

    Colorbars indicate the quantitative extent of image data.
    Placing in a figure is non-trivial because room needs to
    be made for them. The simplest case is just attaching a 
    colorbar to each axes:^[See the [Matplotlib Gallery](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/colorbar_placement.html) to explore colorbars further].

    ```{python}
    #| code-fold: true
    #| column: screen-inset
    import matplotlib.pyplot as plt
    import numpy as np

    fig, axs = plt.subplots(2, 2)
    fig.set_size_inches(20, 8)
    cmaps = ['RdBu_r', 'viridis']
    for col in range(2):
        for row in range(2):
            ax = axs[row, col]
            pcm = ax.pcolormesh(
              np.random.random((20, 20)) * (col + 1),
              cmap=cmaps[col]
            )
            fig.colorbar(pcm, ax=ax)
    plt.show()
    ```

Here is what this document looks like when rendered.

<img src="images/layout-render.png" class="border img-fluid"
alt="Document with Quarto Layout title at the top followed by Placing Colorbars header with text below it. Next to the text is a footnote in the page margin. Below the text is a toggleable code widget to hide/reveal the code followed by four plots displayed in two rows and two columns." />

You can locate citations, footnotes, and
[asides](https://quarto.org/docs/authoring/article-layout.html#asides)
in the margin. You can also define custom column spans for figures,
tables, or other content. See the documentation on [Article
Layout](../../../docs/authoring/article-layout.html) for additional
details.

## Learning More

You’ve now learned the basics of using Quarto! Once you feel comfortable
creating and customizing documents here are a few more things to
explore:

-   [Presentations](../../../docs/presentations/index.html) — Author
    PowerPoint, Beamer, and Revealjs presentations using the same syntax
    you’ve learned for creating documents.

-   [Websites](../../../docs/websites/) — Publish collections of
    documents as a website. Websites support multiple forms of
    navigation and full-text search.

-   [Blogs](../../../docs/websites/website-blog.html) — Create a blog
    with an about page, flexible post listings, categories, RSS feeds,
    and over twenty themes.

-   [Books](../../../docs/books/) — Create books and manuscripts in
    print (PDF, MS Word) and online (HTML, ePub) formats.

-   [Interactivity](../../../docs/interactive/) — Include interactive
    components to help readers explore the concepts and data you are
    presenting more deeply.

See the article on [Using Neovim with
Quarto](../../../docs/tools/neovim.html) to learn more about installing,
using, and customizing Neovim for Quarto.

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
