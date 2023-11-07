<a href="../../../index.html"
class="navbar-brand navbar-brand-logo"><img src="../../../quarto.png"
class="navbar-logo" alt="Quarto logo." /></a>

<span class="navbar-toggler-icon"></span>

-   <a href="../../../index.html" class="nav-link"><span
    class="menu-text">Overview</span></a>
-   <a href="../../../docs/get-started/index.html" class="nav-link"><span
    class="menu-text">Get Started</span></a>
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

## On this page

-   <a href="#crossreferenceable-elements-take-arbitrary-content"
    id="toc-crossreferenceable-elements-take-arbitrary-content"
    class="nav-link active"
    data-scroll-target="#crossreferenceable-elements-take-arbitrary-content">Crossreferenceable
    elements take arbitrary content</a>
-   <a href="#custom-crossreferenceable-types"
    id="toc-custom-crossreferenceable-types" class="nav-link"
    data-scroll-target="#custom-crossreferenceable-types">Custom
    crossreferenceable types</a>
    -   <a href="#example-supplemental-figures-and-tables"
        id="toc-example-supplemental-figures-and-tables" class="nav-link"
        data-scroll-target="#example-supplemental-figures-and-tables">Example:
        supplemental figures and tables</a>
-   <a href="#changes-in-html-output" id="toc-changes-in-html-output"
    class="nav-link" data-scroll-target="#changes-in-html-output">Changes in
    HTML output</a>
-   <a href="#cross-referenceable-listings-of-executable-code-blocks"
    id="toc-cross-referenceable-listings-of-executable-code-blocks"
    class="nav-link"
    data-scroll-target="#cross-referenceable-listings-of-executable-code-blocks">Cross-referenceable
    listings of executable code blocks:</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/prerelease/1.4/crossref.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Crossreferenceable elements

## Crossreferenceable elements take arbitrary content

Crossreferenceable elements now support any kind of content. In previous
versions, Quarto figures needed (for the most part) to be images; Quarto
tables needed to be `Table` elements, and so on. In v1.4, you can
declare a Figure like this:

    ::: {#fig-1}

    ::: {.figure-content}
    This is the figure content.
    :::

    This is a caption.

    :::

Here, the identifier of the figure is still `fig-1`, but the content of
the “Figure” is a fenced Div with any kind of content. The figure itself
is still referenced by `@fig-1`. The prefix `fig` identifies the type of
crossreferenceable element. By default, Quarto v1.4 has support for
Figures (`fig-`), Tables (`tbl-`) and Listings (`lst-`).

## Custom crossreferenceable types

In addition, Quarto v1.4 supports custom crossreferenceable types. If
your document has a large number of, say diagrams or videos, you might
want to refer to them directly as such. To use them, add the following
to your document or project metadata:

    crossref:
      custom: 
        - # crossreferenceable elements with captions are `float`
          kind: float

          # the prefix for reference in output ("In Figure 1, ..")
          prefix: Diagram 

          # the prefix for captions ("Figure 1: ..")
          name: Diagram

          # the prefix for the reference identifier ("In @fig-1, ...")
          ref-type: dia

          # the name of the custom environment in latex output
          latex-env: diagram 

          # used as the file extension for the auxiliary file
          # generated by latex during the collation process
          # if omitted, `lo${ref-type}` is used.
          latex-list-of-file-extension: lod

        - kind: float
          ref-type: supptbl
          latex-env: supptbl
          prefix: Table S
          name: Table S

          # when `false`, don't insert a number between `prefix`, `name` 
          # and the crossref numbering. In this case, crossrefs will be
          # `Table S1`, `Table S2`, etc.
          space-before-numbering: false
          
          # used to create the title, here "List of Supplementary Tables" in LaTeX
          latex-list-of-description: Supplementary Table

### Example: supplemental figures and tables

Using custom crossreferenceable types, you can define “Supplemental
Figures”, by creating a new prefix (eg, `supptbl` above) and giving it
the same appearance as regular figures. Then, if you only use this
prefix for figures in the supplements, you will get a fresh crossref
counter.

## Changes in HTML output

Keep in mind the following changes in the HTML output of figures, etc:

-   The DOM structure for HTML figures used to be such that the
    following CSS selector would work:

        div#fig-elephant > figure > figcaption.figure-caption

    In Quarto v1.4, this is now

        div#fig-elephant > figure.quarto-float.quarto-float-fig > figcaption.quarto-float-caption.quarto-float-fig

    Here’s a minimal, full HTML output for a figure:

        <div id="fig-1" class="quarto-figure quarto-figure-center anchored">
          <figure class="quarto-float quarto-float-fig figure">
          <div aria-describedby="fig-1-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca">
            <img src="./img/content.jpg">
          </div>
          <figcaption id="fig-1-caption-0ceaefa1-69ba-4598-a22c-09a6ac19f8ca" class="figure quarto-float-caption quarto-float-fig">
          Figure&nbsp;1: This is a caption.
          </figcaption>
          </figure>
        </div>

    Concretely:

    -   All crossreferenceable elements use the `figure` HTML element
        with class `quarto-float`.
    -   Different float types are differentiated by the CSS class
        `quarto-float-fig` (or `-tbl`, `-lst`, or the `ref_type` of
        custom crossref types) as well as the additional CSS class
        `figure`, `table`, etc. If the element is a subfloat, this will
        be `quarto-subfloat-fig`.
    -   Similarly, float captions use the `figcaption` element with
        class `quarto-float-caption` (or `quarto-subfloat-caption` if
        they’re a subfloat), and are differentiated by the same
        additional CSS classes.

    This setup lets all “floats” be uniformly targeted by a single CSS
    rule, as well as allowing specific float types and their captions be
    targeted by a single additional CSS selector.

-   Images by themselves used to have a surrounding paragraph; they no
    longer do.

-   Floats include an extra div for ARIA referencing, so that captions
    are referenced appropriately and uniformly. As a result, a table
    appears inside a float, its caption will be hoisted to the figure
    node itself

## Cross-referenceable listings of executable code blocks:

To create crossreferenceable code listings from executable code blocks,
use `lst-label` and `lst-cap`.

    ```{r}
    #| label: fig-1
    #| fig-cap: A figure caption
    #| lst-label: lst-1
    #| lst-cap: A listing caption
    plot(1:10)
    ```

    See @fig-1 and @lst-1.

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
