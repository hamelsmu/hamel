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

# Positioning Content in the Margin

Create ‘Tufte’ style documents with sidenotes, margin tables and
figures, and other margin content

This post demonstrates a few of the capabilities for positioning content
in the margin of the page. You can read more about the complete
capabilities in the the [Article Layout
Guide](../../../../docs/authoring/article-layout.html).

Features

Layout

Author

Charles Teague

Published

February 17, 2022

## On this page

-   <a href="#margin-figures" id="toc-margin-figures"
    class="nav-link active" data-scroll-target="#margin-figures">Margin
    Figures</a>
-   <a href="#margin-tables" id="toc-margin-tables" class="nav-link"
    data-scroll-target="#margin-tables">Margin Tables</a>
-   <a href="#other-content" id="toc-other-content" class="nav-link"
    data-scroll-target="#other-content">Other Content</a>
-   <a href="#margin-references" id="toc-margin-references" class="nav-link"
    data-scroll-target="#margin-references">Margin References</a>
    -   <a href="#asides" id="toc-asides" class="nav-link"
        data-scroll-target="#asides">Asides</a>
-   <a href="#margin-captions" id="toc-margin-captions" class="nav-link"
    data-scroll-target="#margin-captions">Margin Captions</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/blog/posts/2022-02-17-advanced-layout/index.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

Quarto supports a variety of page layout options that enable you to
author content that

-   Fills the main content region
-   Overflows the content region
-   Spans the entire page
-   Occupies the document margin

This post will demonstrate a few of the capabilities for positioning
content in the margin of the page. You can read more about the complete
capabilities in the the [Article Layout
Guide](../../../../docs/authoring/article-layout.html).  

## Margin Figures

Figures that you create using code cells can be placed in the margin by
using the `column: margin` code cell option. If the code produces more
than one figure, each of the figures will be placed in the margin.

    ```{r}
    #| label: fig-mtcars
    #| fig-cap: "MPG vs horsepower, colored by transmission."
    #| column: margin

    library(ggplot2)
    mtcars2 <- mtcars
    mtcars2$am <- factor(
      mtcars$am, labels = c('automatic', 'manual')
    )
    ggplot(mtcars2, aes(hp, mpg, color = am)) +
      geom_point() +  geom_smooth(formula = y ~ x, method = "loess") +
      theme(legend.position = 'bottom')
    ```

<figure>
<img src="index_files/figure-html/fig-mtcars-1.png"
class="img-fluid figure-img" width="672"
alt="Figure 1: MPG vs horsepower, colored by transmission." />
<figcaption aria-hidden="true">Figure 1: MPG vs horsepower, colored by
transmission.</figcaption>
</figure>

## Margin Tables

You an also place tables in the margin of your document by specifying
`column: margin`.

    ```{r}
    #| column: margin

    knitr::kable(
      mtcars[1:3, 1:3]
    )
    ```

<table class="table table-sm table-striped small">
<thead>
<tr class="header header">
<th style="text-align: left;"></th>
<th style="text-align: right;">mpg</th>
<th style="text-align: right;">cyl</th>
<th style="text-align: right;">disp</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td style="text-align: left;">Mazda RX4</td>
<td style="text-align: right;">21.0</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">160</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Mazda RX4 Wag</td>
<td style="text-align: right;">21.0</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">160</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Datsun 710</td>
<td style="text-align: right;">22.8</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">108</td>
</tr>
</tbody>
</table>

## Other Content

You can also place content in the margin by targeting the margin column
using a div with the .`column-margin` class. For example:

    ::: {.column-margin}
    We know from *the first fundamental theorem of calculus* that for $x$ in $[a, b]$:


    $$\frac{d}{dx}\left( \int_{a}^{x} f(u)\,du\right)=f(x).$$

    :::

We know from *the first fundamental theorem of calculus* that for <span
class="math inline">\\(x\\)</span> in <span class="math inline">\\(\[a,
b\]\\)</span>:

<span class="math display">\\\[\frac{d}{dx}\left( \int\_{a}^{x}
f(u)\\,du\right)=f(x).\\\]</span>

## Margin References

Footnotes and the bibliography typically appear at the end of the
document, but you can choose to have them placed in the margin by
setting the following option\[^1\] in the document front matter:

    ---
    reference-location: margin
    citation-location: margin
    ---

With these options set, footnotes and citations will (respectively) be
automatically be placed in the margin of the document rather than the
bottom of the page. As an example, when I cite <span class="citation"
cites="xie2018">Xie, Allaire, and Grolemund
(<a href="#ref-xie2018" role="doc-biblioref">2018</a>)</span>, the
citation bibliography entry itself will now appear in the margin.

Xie, Yihui, J. J. Allaire, and Garrett Grolemund. 2018. *R Markdown: The
Definitive Guide*. Boca Raton, Florida: Chapman; Hall/CRC.
<https://bookdown.org/yihui/rmarkdown>.

### Asides

Asides allow you to place content aside from the content it is placed
in. Asides look like footnotes, but do not include the footnote mark
(the superscript number).

This is a span that has the class `aside` which places it in the margin
without a footnote number.

    [This is a span that has the class aside which places it in the margin without a footnote number.]{.aside}

## Margin Captions

For figures and tables, you may leave the content in the body of the
document while placing the caption in the margin of the document. Using
`cap-location: margin` in a code cell or document front matter to
control this. For example:

    ```{r}
    #| label: fig-cap-margin
    #| fig-cap: "MPG vs horsepower, colored by transmission."
    #| cap-location: margin

    library(ggplot2)
    mtcars2 <- mtcars
    mtcars2$am <- factor(
      mtcars$am, labels = c('automatic', 'manual')
    )
    ggplot(mtcars2, aes(hp, mpg, color = am)) +
      geom_point() +  geom_smooth(formula = y ~ x, method = "loess") +
      theme(legend.position = 'bottom')
    ```

<figure>
<img src="index_files/figure-html/fig-cap-margin-1.png"
class="img-fluid figure-img" width="672"
alt="Figure 2: MPG vs horsepower, colored by transmission." />
<figcaption aria-hidden="true">Figure 2: MPG vs horsepower, colored by
transmission.</figcaption>
</figure>

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
