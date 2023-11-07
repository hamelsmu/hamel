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

-   <a href="#finer-control-over-table-processing"
    id="toc-finer-control-over-table-processing" class="nav-link active"
    data-scroll-target="#finer-control-over-table-processing">Finer control
    over table processing</a>
-   <a href="#include-quarto-markdown-in-latex-raw-blocks"
    id="toc-include-quarto-markdown-in-latex-raw-blocks" class="nav-link"
    data-scroll-target="#include-quarto-markdown-in-latex-raw-blocks">Include
    Quarto markdown in LaTeX Raw Blocks</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/prerelease/1.4/ast.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# AST processing changes in v1.4

In Quarto v1.3, we added support for parsing HTML tables as native
Pandoc elements, so that sophisticated table layouts are available in
more formats. Quarto v1.4 extends this in a few ways.

## Finer control over table processing

In v1.3, this HTML processing could be disabled only by specifying an
option in the HTML table itself, using
`quarto-disable-processing="true"`.

In v1.4, this behavior can be controlled by document- and project-level
metadata, using the `html-table-processing: none` YAML option:

    ---
    html-table-processing: none
    ---

    No HTML tables in this document will be processed.

    ```{r}
    library(huxtable)
    # your huxtable tables won't be processed by quarto
    ```

In addition, you can disable the processing selectively in parts of the
document, by surrounding the elements with a fenced div having the
attribute `{html-table-processing="none"}`:

    ---
    html-table-processing: none
    ---

    No HTML tables in this document will be processed.

    ::: {html-table-processing="none"}

    ```{r}
    library(huxtable)
    # your huxtable tables won't be processed by quarto because of
    # the surrounding div
    ```

    :::

    ```{r}
    library(gt)
    # your gt tables will be processed as in 1.3
    ```

## Include Quarto markdown in LaTeX Raw Blocks

In Quarto v1.3, HTML rawblocks can contain the syntax
`<span data-qmd="<<markdown-content>>"/>` of
`<span data-qmd-base64="<<base64-encoded-markdown-content>>"` to allow
libraries that emit raw blocks to benefit from Quarto features such as
crossref resolution and shortcodes.

In Quarto v1.4, this feature is also available in LaTeX formats. If the
syntax `\QuartoMarkdownBase64{<<base64-encoded-markdown-content>>}` is
detected by Quarto, the contents will be decoded, processed in Quarto
(including user filters), and then inserted back into the LaTeX raw
block.

This is useful for third-party libraries that seek to emit LaTeX content
that nevertheless can have “quarto content”. Note that, unlike the HTML
feature, Quarto currently only supports base-64 encoded content in LaTeX
blocks.

Note that, unlike the HTML table parsing feature, this LaTeX feature
cannot currently be disabled. We expect this to not be necessary because
`QuartoMarkdownBase64` is unlikely to conflict with existing LaTeX
environments.

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
