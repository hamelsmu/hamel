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

-   <a href="#overview" id="toc-overview" class="nav-link active"
    data-scroll-target="#overview">Overview</a>
    -   <a href="#html-tables-are-now-processed-in-every-format"
        id="toc-html-tables-are-now-processed-in-every-format" class="nav-link"
        data-scroll-target="#html-tables-are-now-processed-in-every-format">HTML
        tables are now processed in every format</a>
    -   <a href="#bootstrap-classes-can-be-added-to-tables"
        id="toc-bootstrap-classes-can-be-added-to-tables" class="nav-link"
        data-scroll-target="#bootstrap-classes-can-be-added-to-tables">Bootstrap
        classes can be added to tables</a>
    -   <a href="#embedded-markdown-content-can-be-specified"
        id="toc-embedded-markdown-content-can-be-specified" class="nav-link"
        data-scroll-target="#embedded-markdown-content-can-be-specified">Embedded
        Markdown content can be specified</a>
-   <a href="#limitations" id="toc-limitations" class="nav-link"
    data-scroll-target="#limitations">Limitations</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/prerelease/1.3/tables.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# HTML Table Processing

Pre-release Feature

This feature is new in the upcoming Quarto 1.3 release. To use the
feature now, you’ll need to
[download](https://quarto.org/docs/download/prerelease) and install the
Quarto pre-release.

## Overview

In Quarto 1.3, we have made some changes to how tables are processed.
Recent Pandoc versions have added support for parsing HTML tables into
Pandoc’s native data structures (including features such as rowspans and
colspans), and Quarto now leverages this to make it easier to produce
properly formatted tables in more formats.

### HTML tables are now processed in every format

Specifically, Quarto will now attempt to parse HTML tables in `RawBlock`
nodes in `html` format and convert them to Markdown tables, regardless
of output format (intentionally including non-HTML formats). As a
result, you can now use HTML table syntax in your documents and they
will be properly converted to Markdown tables for all formats, and
libraries which emit computational tables in HTML format can work in
other output formats. In addition, this will allow Lua filters to
manipulate the content of tables specified in HTML format.

Note

If you’re a library author, we hope that you will consider emitting HTML
tables in your output. This will allow your users to use the full power
of Quarto’s table processing in all formats.

With that said, it’s possible that our processing of HTML tables
interferes with your library’s processing. If this is the case, you can
disable Quarto’s processing of HTML tables by adding the following data
attribute to your table:

    <table data-quarto-disable-processing="true">
      ...
    </table>

### Bootstrap classes can be added to tables

Bootstrap table classes given as attributes next to a table caption are
now inserted into the `<table>` element. The classes permitted are those
that apply expressly to the entire table, and these are: `"primary"`,
`"secondary"`, `"success"`, `"danger"`, `"warning"`, `"info"`,
`"light"`, `"dark"`, `"striped"`, `"hover"`, `"active"`, `"bordered"`,
`"borderless"`, `"sm"`, `"responsive"`, `"responsive-sm"`,
`"responsive-md"`, `"responsive-lg"`, `"responsive-xl"`,
`"responsive-xxl"`. For example, the following Markdown table will be
rendered with row stripes and the rows will also be highlighted on
hover:

    | fruit  | price  |
    |--------|--------|
    | apple  | 2.05   |
    | pear   | 1.37   |
    | orange | 3.09   |

    : Fruit prices {.striped .hover}

### Embedded Markdown content can be specified

In addition, Quarto now supports the specification of embedded Markdown
content in tables. This is done by providing a data attribute `qmd` or
`qmd-base64` in an embedded `span` or `div` node. These nodes can appear
anywhere that such content is allowed: table headers, footers, cells,
captions, etc. For example, consider the following table:

    <table>
      <caption><span data-qmd="As described in @Lovelace1864, computers are great."></span></caption>
      <thead>
        <tr>
          <th><span data-qmd="_Header 1_"></span></th>
          <th><span data-qmd="_Header 2_"></span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span data-qmd=""></span></td>
          <td>Regular output</td>
        </tr>
      </tbody>
    </table>

The `span` nodes with the `data-qmd` attribute will be processed as
embedded Markdown content. This allows you to embed arbitrary Markdown
content in your tables, including citations, videos, etc. One thing to
keep in mind is that the content of `data-qmd` needs to be escaped
properly. Authors of libraries which generate table outputs should
consider using the `data-qmd-base64` attribute, which will be decoded
and then processed by Quarto.

## Limitations

Quarto **doesn’t** support processing of:

-   nested `<table>` elements.
-   invalid HTML tables. Make sure your emitted HTML [passes
    validation](https://validator.w3.org/).

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
