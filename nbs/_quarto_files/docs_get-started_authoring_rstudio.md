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
-   <a href="#publishing" id="toc-publishing" class="nav-link"
    data-scroll-target="#publishing">Publishing</a>
-   <a href="#learning-more" id="toc-learning-more" class="nav-link"
    data-scroll-target="#learning-more">Learning More</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/get-started/authoring/rstudio.qmd"
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

In this tutorial we’ll show you how to author Quarto documents in
RStudio. In particular, we’ll discuss the various document formats you
can produce with the same source code and show you how to add components
like table of contents, equations, citations, etc. The [visual markdown
editor](../../../docs/visual-editor/) in RStudio makes many of these
tasks easier so we’ll highlight its use in this tutorial, but note that
it’s possible to accomplish these tasks in the source editor as well.

If you would like to follow along step-by-step in your own environment,
make sure that you have the [latest
release](https://posit.co/download/rstudio-desktop/) of RStudio
(v2023.06), which you can download
[here](https://posit.co/download/rstudio-desktop/), installed.

## Output Formats

Quarto supports rendering notebooks to dozens of different output
formats. By default, the `html` format is used, but you can specify an
alternate format (or formats) within document options.

### Format Options

You can choose the format you want to render your Quarto document to at
the time of creating your new document. To create a new document, go to
**File** &gt; **New File** &gt; **Quarto Document…** Alternatively, use
the command palette (accessible via Ctrl+Shift+P), search for **Create a
new Quarto document** and hit return.

In the **Title** field, give a title for your document (e.g. the
screenshot below suggests “Housing Prices”) and add your name to the
**Author** field. Next, you will select the output format for your
document. By default, RStudio suggests using HTML as the output, let’s
leave that default for now.

<img src="images/rstudio-new-document.png"
class="border img-fluid quarto-figure-center" width="600"
alt="Pop up menu for creating a new document. The title field shows that we entered &quot;Housing Prices&quot; and the author field shows the name &quot;Mine Çetinkaya-Rundel&quot;. HTML format is selected via the radio button. All else is left as default choices (e.g., Engine is Knitr and the Use visual markdown editor checkbox is checked)." />

A new document will be created with the following YAML.

    ---
    title: "Housing Prices"
    author: "Mine Çetinkaya-Rundel"
    ---

Note that our format choice (HTML) is not even reflected in the YAML as
it is the default output format for Quarto documents. However you can
directly edit the YAML to change the output format, e.g. to PDF (`pdf`)
or MS Word (`docx`). Add `format: pdf` to your document’s YAML as shown
below.

    ---
    title: "Housing Prices"
    author: "Mine Çetinkaya-Rundel"
    format: pdf
    ---

Unfortunately, this document has no content, so rendering it would not
result in very interesting output. To make it a bit easier to
demonstrate all the features we want to highlight in this tutorial,
let’s close this empty document and start with one that has a little bit
of content in it. If you would like to follow along step-by-step in your
own environment, download the Quarto document (`.qmd`) below and open it
in RStudio.

<a href="_authoring.qmd" download="authoring.qmd">Download
authoring.qmd</a>

In order to create PDFs you will need to install a recent distribution
of [LaTeX](https://www.latex-project.org/). We recommend the use of
TinyTeX (which is based on TexLive), which you can install with the
following command:

    Terminal

    quarto install tinytex

See the article on [PDF
Engines](../../../docs/output-formats/pdf-engine.html) for details on
using other LaTeX distributions and PDF compilation engines.

Once you have LaTeX setup, click on <span
class="kbd"><img src="images/rstudio-render-button.png" width="25" height="20" /></span>
**Render** (or use the keyboard shortcut ⇧⌘K). We recommend also
checking the box for **Render on Save** for a live preview of your
changes. As shown below, you should see the rendered PDF in the Viewer
in RStudio.

<img src="images/rstudio-pdf-preview.png"
class="border column-page-right img-fluid"
alt="RStudio with authoring.qmd open. On the left: Source code in the visual editor. On the left: Rendered document as a PDF in the Viewer." />

Next, let’s add an option to the YAML, e.g. to add line numbers to the
code chunks (`code-line-numbers: true`). Add this option to your
document’s YAML as shown below, paying attention to the indentation
scheme. Under `format:` our format choice `pdf` is indented (with two
spaces) and it’s followed by `:` to indicate that further options for
that format will be specified. In the next line, further indented by two
spaces, we add `code-line-numbers: true`.

    ---
    title: "Housing Prices"
    author: "Mine Çetinkaya-Rundel"
    format:
      pdf:
        code-line-numbers: true
    ---

If you checked **Render on Save** earlier, just save the document after
making this change for a live preview. Otherwise render the document to
see your updates reflected, including a table of contents that looks
like the following.

<img src="images/rstudio-code-line-numbers.png"
class="border img-fluid quarto-figure-center"
alt="Rendered version of authoring.qmd as PDF, with line numbers next to each of the lines of code chunks." />

An incredibly exciting format option that we won’t go into too much
detail in this tutorial is `revealjs`. Yes, you can make presentations
with Quarto as well! In fact, Quarto supports a variety of formats for
creating presentations, including `revealjs` for HTML slides, `pptx` for
PowerPoint, and `beamer` for LaTeX/PDF. The
[Presentations](../../../docs/presentations/) article gives a thorough
walk through of creating slide decks with Quarto.

### Multiple Formats

Some documents you create will have only a single output format, however
in many cases it will be desirable to support multiple formats. Let’s
add the `html` and `docx` formats to our document and modify some
options specific to each format.

    ---
    title: "Housing Prices"
    author: "Mine Çetinkaya-Rundel"
    highlight-style: pygments
    format:
      html: 
        code-fold: true
        html-math-method: katex
      pdf:
        geometry: 
          - top=30mm
          - left=30mm
      docx: default
    ---

There’s a lot to take in here! Let’s break it down a bit. The first two
lines are generic document metadata that aren’t related to output
formats at all.

    ---
    title: "Housing Prices"
    author: "Mine Çetinkaya-Rundel"
    ---

The next line is a document format option that *applies to all formats*,
which is why it is specified at the root level.

    ---
    highlight-style: pygments
    ---

Next, we have the `format` option, where we provide format-specific
options.

    ---
    format:
      html: 
        code-fold: true
        html-math-method: katex
      pdf:
        geometry: 
          - top=30mm
          - left=30mm
      docx: default
    ---

The `html` and `pdf` formats each provide an option or two. For example,
for the HTML output we want the user to have control over whether to
show or hide the code (`code-fold: true`) and use `katex` for math text.
For PDF we define some margins. The `docx` format is a bit different—it
specifies `docx: default`. This indicates that we just want to use all
of the default options for the format.

## Rendering

Clicking the <span
class="kbd"><img src="images/rstudio-render-button.png" width="25" height="21" /></span>
**Render** button (or using the keyboard shortcut <span
class="kbd">⇧⌘K</span>) in RStudio will render the document to the first
format listed in the YAML.

<img src="images/rstudio-html-preview.png" class="border img-fluid"
alt="Rendered version of authoring.qmd as HTML. There is no table of contents and the code chunks are folded, hiding the code." />

Note that the <span
class="kbd"><img src="images/rstudio-render-button.png" width="25" height="21" /></span>
**Render** button also has a drop down menu that enables you to render
to any of the formats listed in YAML front matter:

<img src="images/rstudio-render-formats.png" class="border img-fluid" />

If you would like to render to all formats, you can do so with the
[**quarto**](https://github.com/quarto-dev/quarto-r) package, which
provides an R interface to the Quarto CLI. For example, to render the
current document, use `quarto::quarto_render()`. You can also specify
the name of the document you want to render as well as the output
format(s).

    quarto::quarto_render(
      "authoring.qmd", 
      output_format = c("pdf", "html", "docx")
    )

As a result, you will see three new files appear in your Files pane:

-   `authoring.docx`
-   `authoring.html`
-   `authoring.pdf`

<img src="images/rstudio-files-pane.png"
class="border img-fluid quarto-figure-center" width="600"
alt="RStudio Files pane, with four document, all titled authoring, but with different suffixes: docx, html, pdf, qmd." />

## Sections

You can use a table of contents and/or section numbering to make it
easier for readers to navigate your document. Do this by adding the
`toc` and/or `number-sections` options to document options. Note that
these options are typically specified at the root level because they are
shared across all formats.

    ---
    title: "Housing Prices"
    author: "Mine Çetinkaya-Rundel"
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
          - left=30mm
      docx: default
    ---

Here’s what this document looks like when rendered to HTML.

<img src="images/rstudio-toc-secnum.png" class="border img-fluid"
alt="Rendered version of authoring.qmd as HTML with numbered sections and a table of contens on the top right. The table of contents shows three sections: Introduction, Exploratory data analysis (with subsections Data visualization and Summary statistics), and Modeling." />

There are lots of options available for controlling how the table of
contents and section numbering behave. See the output format
documentation
(e.g. [HTML](../../../docs/output-formats/html-basics.html),
[PDF](../../../docs/output-formats/pdf-basics.html), [MS
Word](../../../docs/output-formats/ms-word.html)) for additional
details.

## Equations

If you are using the visual editor mode, you can add LaTeX equations to
Quarto documents in RStudio using the [Insert
Anything](../../../docs/visual-editor/index.html#insert-anything) tool.
You can access it with <span class="kbd">/</span> at the beginning of an
empty block or <span class="kbd">Cmd+/</span> anywhere else.

<img src="images/rstudio-insert-equation.png"
class="border img-fluid quarto-figure-center" width="600"
alt="Insert anything tool in the RStudio visual editor being used to insert a display math." />

Display equations (in a new line) are delimited with `$$…$$` while
inline equations are delimited with `$…$`. Add the following as display
math in the document.

    price = \hat{\beta}_0 + \hat{\beta}_1 \times area + \epsilon

RStudio displays a rendered version of the tutorial as you type it in
the editor. See the documentation on [markdown
equations](../../../docs/authoring/markdown-basics.html#equations) for
additional details.

<img
src="../../../docs/get-started/authoring/images/rstudio-equation-render.png"
class="border img-fluid" />

## Citations

The Insert Anything tool can also be used to insert citations to your
document.

<img src="images/rstudio-insert-citation.png" class="img-fluid"
width="700" alt="Using the visual editor insert citation tool." />

In the next window you can insert a citation via from a variety of
sources including your document bibliography,
[Zotero](../../../docs/visual-editor/technical.html#citations-from-zotero)
personal or group libraries,
[DOI](../../../docs/visual-editor/technical.html#citations-from-dois)
(Document Object Identifier) references, and searches of
[Crossref](https://www.crossref.org/),
[DataCite](https://datacite.org/), or
[PubMed](https://pubmed.ncbi.nlm.nih.gov/). You can find out more about
citations with the visual editor
[here](../../../docs/visual-editor/technical.html#citations).

Select **From DOI** on the left and copy-and-paste the DOI
[`10.1093/comjnl/27.2.97`](https://doi.org/10.1093/comjnl/27.2.97) in
the search bar and hit **Search**. Then, select the found reference, and
**Insert** it into your document.

<img src="images/rstudio-insert-citaton-menu.png" class="img-fluid"
alt="Insert citation to Knuth, D&#39;s Literate Programming article via DOI." />

If this is the first citation you are adding to your document, RStudio
will automatically create a bibliography file for you. This file is
called `references.bib` by default and RStudio will also add
`bibliography: references.bib` to your document’s YAML metadata.

Note that items within the bibliography are cited using the `@citeid`
syntax. Add the following text to your document.

    We're going to do this analysis using literate programming [@knuth1984].

References will be included at the end of the document, so we include a
`## References` heading at the bottom of the notebook. You might also
add `.unnumbered` class to this section by clicking on the three dots
(<span class="kbd">…</span>) to edit its attributes.

<img src="images/rstudio-references-section.png"
class="border img-fluid" width="700"
alt="Edit Attributes window for the section title References. The image shows that this menu can be accessed by cliking on the three dots." />

Here is what this document looks like when rendered (with middle
sections removed to highlight the relevant parts.

<img src="images/rstudio-references.png" class="border img-fluid"
alt="Document with a single citation and a references section at the end." />

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

For example, to add a label to the equation inserted earlier, click on
the three dots to edit its attributes and use the suggested format
(starting with `#eq-`) to label the equation.

<img src="images/rstudio-crossref-equation.png" class="border img-fluid"
alt="Add label to an equation using the visual editor. The label added is #eq-slr." />

Then, add a cross reference using the Insert Anything tool in the visual
editor. You might add a sentence like
`"We can fit a simple linear regression model of the form shown in"` to
contextualize the cross reference and then add the reference to the end
of that sentence.

<img src="images/rstudio-crossref-equation-insert.png"
class="border img-fluid"
alt="Use the insert anything tool in the visual editor to insert a cross reference." />

In the Insert Cross Reference menu, navigate to the desired cross
reference entity on the left, and select the equation labeled earlier.

<img src="images/rstudio-crossref-insert-menu.png"
class="border img-fluid"
alt="Use the insert cross reference menu, select Equations on the left side, and select an equation to cross reference." />

Alternatively, start typing the label of the equation to be referenced
in the visual editor, and the autofill tool will bring up the cross
references to choose from.

<img src="images/rstudio-crossref-eq-autofill.png"
class="border img-fluid"
alt="Cross reference an equation by starting to type out its label." />

Below we illustrate cross-referencing various types of entities using
fragments from the document you’ve been working with.

    We present the results of exploratory data analysis in @sec-eda and the regression model in @sec-model.


    @fig-scatterplot displays the relationship between these two variables in a scatterplot.


    @tbl-stats displays basic summary statistics for these two variables.


    We can fit a simple linear regression model of the form shown in @eq-slr.

This examples include cross-referenced sections, figures, and equations.
The table below summarizes how we express each of these.

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
<td><code>@sec-eda</code></td>
<td><p>ID added to heading:</p>
<div id="cb14" class="sourceCode" data-code-copy="false">
<div class="sourceCode" id="cb1"><pre
class="sourceCode default code-with-copy"><code class="sourceCode default"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a># Exploratory data analysis {#sec-eda}</span></code></pre></div>
</div></td>
</tr>
<tr class="even even">
<td>Figure</td>
<td><code>@fig-scatterplot</code></td>
<td><p>YAML options in code cell:</p>
<div id="cb15" class="sourceCode" data-code-copy="false">
<div class="sourceCode" id="cb2"><pre
class="sourceCode default code-with-copy"><code class="sourceCode default"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>#| label: fig-scatterplot</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a>#| fig-cap: &quot;Scatterplot of price vs. area of houses in Duke Forest&quot;</span></code></pre></div>
</div></td>
</tr>
<tr class="odd odd">
<td>Table</td>
<td><code>@tbl-stats</code></td>
<td><p>YAML options in code cell:</p>
<div id="cb16" class="sourceCode" data-code-copy="false">
<div class="sourceCode" id="cb3"><pre
class="sourceCode default code-with-copy"><code class="sourceCode default"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a>#| label: tbl-stats</span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a>#| tbl-cap: &quot;Summary statistics for price and area of houses in Duke Forest&quot;</span></code></pre></div>
</div></td>
</tr>
<tr class="even even">
<td>Equation</td>
<td><code>@eq-slr</code></td>
<td><p>At end of display equation:</p>
<div id="cb17" class="sourceCode">
<div class="sourceCode" id="cb4"><pre
class="sourceCode default code-with-copy"><code class="sourceCode default"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>$$ {#eq-slr}</span></code></pre></div>
</div></td>
</tr>
</tbody>
</table>

See the article on [Cross
References](../../../docs/authoring/cross-references.html) to learn
more, including how to customize caption and reference text (e.g. use
“Fig.” rather than “Figure”).

## Callouts

Callouts are an excellent way to draw extra attention to certain
concepts, or to more clearly indicate that certain content is
supplemental or applicable to only some scenarios.

Callouts are markdown divs that have special callout attributes. We can
insert a callout using the Insert Anything tool.

<img src="images/rstudio-insert-callout.png" class="border img-fluid"
alt="Insert Anything tool to insert a callout." />

In the subsequent dialogue you can select one of five types of callout
(note, tip, important, caution, or warning), customize its appearance
(default, simple, or minimal), and decide whether you want to show the
icon.

<img src="images/rstudio-callout-dialogue.png"
class="border img-fluid quarto-figure-center" width="500"
alt="Callout dialogue. Type note is selected with default appearance and show icon box is checked." />

Then, try inserting the following text in the callout box.

    This is a pretty incomplete analysis, but hopefully the document provides a good overview of some of the authoring features of Quarto!

Here is what a callout looks like in the visual editor.

<img src="images/rstudio-callout-note-source.png"
class="border img-fluid"
alt="Callout box in the visual editor. Callout text reads &quot;This is a pretty incomplete analysis, but hopefully the document provides a good overview of some of the authoring features of Quarto!&quot;" />

And here is the rendered callout in the output document.

<img src="images/rstudio-callout-note-rendered.png"
class="border img-fluid"
alt="Callout box in the rendered HTML document. Callout text reads &quot;This is a pretty incomplete analysis, but hopefully the document provides a good overview of some of the authoring features of Quarto!&quot;" />

You can learn more about the different types of callouts and options for
their appearance in the
[Callouts](../../../docs/authoring/callouts.html) documentation.

## Article Layout

The body of Quarto articles have a default width of approximately 700
pixels. This width is chosen to [optimize
readability](https://medium.com/ben-shoemate/optimum-web-readability-max-and-min-width-for-page-text-dee9987a27a0).
This normally leaves some available space in the document margins and
there are a few ways you can take advantage of this space.

We can use the `column: page-right` cell option to indicate we would
like our figure to occupy the full width of the screen, with some inset.
Go ahead and add this chunk option to the chunk labeled `fig-histogram`.

    #| label: fig-histogram
    #| fig-cap: "Histograms of individual variables"
    #| fig-subcap:
    #|   - "Histogram of `price`s"
    #|   - "Histogram of `area`s" 
    #| layout-ncol: 2
    #| column: page-right

Here is what the relevant section of the document looks like when
rendered.

<img src="images/rstudio-column-page-right-render.png"
class="border img-fluid"
alt="Rendered version of authoring.qmd as HTML. Exploratory data analysis section is shown, the side-by-side histograms span a width wider than the rest of the document." />

You can locate citations, footnotes, and asides in the margin. You can
also define custom column spans for figures, tables, or other content.
See the documentation on [Article
Layout](../../../docs/authoring/article-layout.html) for additional
details.

## Publishing

Once your document is rendered to HTML, you can publish to
[RPubs](https://rpubs.com/) (a free service from RStudio for sharing
documents on the web) simply by clicking the <span
class="kbd"><img src="images/rstudio-publish-button.png" width="25" height="23" /></span>
Publish button on the editor toolbar or preview window. Alternatively,
you can use the `quarto::quarto_publish_doc()` function.

    quarto::quarto_publish_doc(
      "authoring.qmd", 
      server = "rpubs.com"
      )

Other possible publishing options include RStudio Connect and ShinyApps
as well as GitHub Pages, Netlify, etc. The [Publishing
HTML](../../../docs/output-formats/html-publishing.html) article gives a
much more detailed overview of your publishing options.

If you followed along step-by-step with this tutorial, you should now
have a Quarto document that implements everything we covered. Otherwise,
you can download a completed version of `computations.qmd` below.

<a href="_authoring-complete.qmd"
download="authoring-complete.qmd">Download authoring-complete.qmd</a>

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
