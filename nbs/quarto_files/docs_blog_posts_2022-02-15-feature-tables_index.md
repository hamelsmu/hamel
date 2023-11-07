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

# Customizing Table Output

Author and customize markdown tables using Quarto

This post provides an overview of these capabilities in Quarto. For more
detail about all the features Quarto for authoring tables, see
[Tables](../../../../docs/authoring/tables.html).

Features

Authoring

Tables

Author

JJ Allaire

Published

February 15, 2022

## On this page

-   <a href="#markdown-tables" id="toc-markdown-tables"
    class="nav-link active" data-scroll-target="#markdown-tables">Markdown
    Tables</a>
-   <a href="#explicit-column-widths" id="toc-explicit-column-widths"
    class="nav-link" data-scroll-target="#explicit-column-widths">Explicit
    Column Widths</a>
-   <a href="#computations" id="toc-computations" class="nav-link"
    data-scroll-target="#computations">Computations</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/blog/posts/2022-02-15-feature-tables/index.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

Quarto includes a number of features aimed at making it easy to to
author and customize markdown table output, including:

-   Specifying column alignment and widths.
-   Providing captions, subcaptions, and cross-references.
-   Generating tables dynamically from executable code cells.

This post provides an overview of these capabilities in Quarto. For more
detail about all the features Quarto for authoring tables, see
[Tables](../../../../docs/authoring/tables.html).

## Markdown Tables

The most commonly used markdown table is known as a pipe table. Pipe
tables support specifying per column alignment as well as captions. For
example:

    | Default | Left | Right | Center |
    |---------|:-----|------:|:------:|
    | 12      | 12   |    12 |   12   |
    | 123     | 123  |   123 |  123   |
    | 1       | 1    |     1 |   1    |

    : Demonstration of pipe table sytnax

Here is the table rendered to HTML:

<table class="table">
<caption>Demonstration of pipe table syntax</caption>
<thead>
<tr class="header header">
<th>Default</th>
<th style="text-align: left;">Left</th>
<th style="text-align: right;">Right</th>
<th style="text-align: center;">Center</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td>12</td>
<td style="text-align: left;">12</td>
<td style="text-align: right;">12</td>
<td style="text-align: center;">12</td>
</tr>
<tr class="even even">
<td>123</td>
<td style="text-align: left;">123</td>
<td style="text-align: right;">123</td>
<td style="text-align: center;">123</td>
</tr>
<tr class="odd odd">
<td>1</td>
<td style="text-align: left;">1</td>
<td style="text-align: right;">1</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

Demonstration of pipe table syntax

#### Caption Location

By default, table captions are positioned above tables. You can modify
this behavior using the `tbl-cap-location` option. For example:

    ---
    tbl-cap-location: top
    ---

## Explicit Column Widths

Beyond standard pipe table syntax for expressing column width, you can
also explicitly specify columns widths using the `tbl-colwidths`
attribute or document-level option. For an individual markdown table,
add the attribute after the caption. For example:

    | fruit  | price  |
    |--------|--------:
    | apple  | 2.05   |
    | pear   | 1.37   |
    | orange | 3.09   |

    : Fruit prices {tbl-colwidths="[75,25]"}

Note that this option is specified at the top level so that it can be
shared by both PDF and HTML formats. If you are only targeting a single
format you can place it alongside other `format` specific options.

Valid values for the caption location include:

<table class="table">
<thead>
<tr class="header header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td><code>top</code></td>
<td>Position the caption above the table.</td>
</tr>
<tr class="even even">
<td><code>bottom</code></td>
<td>Position the caption below the table.</td>
</tr>
<tr class="odd odd">
<td><code>margin</code></td>
<td>Position the caption in the margin.</td>
</tr>
</tbody>
</table>

## Computations

All of the options described above work for tables produced by
executable code cells. For example, here we apply the `tbl-cap`,
`tbl-colwidths` and `tbl-caption-location` options to a code cell:

    ```{r}
    #| tbl-cap: "Cars"
    #| tbl-colwidths: [60,40]
    #| tbl-cap-location: margin

    library(knitr)
    kable(head(cars))
    ```

In addition to the above, which focused on some of the features of
Quarto when writing pipe tables in markdown, you can also author tables
using grid syntax. You review the
[documentation](../../../../docs/authoring/tables.html). for more
detail.

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

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
