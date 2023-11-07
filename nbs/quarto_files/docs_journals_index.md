<a href="../../index.html" class="navbar-brand navbar-brand-logo"><img
src="../../quarto.png" class="navbar-logo" alt="Quarto logo." /></a>

<span class="navbar-toggler-icon"></span>

-   <a href="../../index.html" class="nav-link"><span
    class="menu-text">Overview</span></a>
-   <a href="../../docs/get-started/index.html" class="nav-link"><span
    class="menu-text">Get Started</span></a>
-   <a href="../../docs/guide/index.html" class="nav-link"><span
    class="menu-text">Guide</span></a>
-   <a href="../../docs/extensions/index.html" class="nav-link"><span
    class="menu-text">Extensions</span></a>
-   <a href="../../docs/reference/index.html" class="nav-link"><span
    class="menu-text">Reference</span></a>
-   <a href="../../docs/gallery/index.html" class="nav-link"><span
    class="menu-text">Gallery</span></a>
-   <a href="../../docs/blog/index.html" class="nav-link"><span
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
    -   <a href="../../docs/faq/index.html" class="dropdown-item"><em></em>
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
-   <a href="#journal-formats" id="toc-journal-formats" class="nav-link"
    data-scroll-target="#journal-formats">Journal Formats</a>
-   <a href="#creating-formats" id="toc-creating-formats" class="nav-link"
    data-scroll-target="#creating-formats">Creating Formats</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/journals/index.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Journal Articles

## Overview

Quarto supports the creation of custom formats that extend base formats
like `pdf`, `html`, and `docx`. The custom format system is very
flexible, and has been designed to accommodate the creation of articles
for publishing in professional Journals.

A major focus is single-source publishing: the same Quarto document
source should be capable of producing both HTML and LaTeX output, and
should also be capable of creating the LaTeX required for submission to
multiple Journals. Key capabilities that enable this include:

-   The ability to flexibly adapt the native LaTeX templates provided by
    Journals for use with Pandoc.

-   The use of spans and divs to apply formatting (which enables
    targeting by CSS for HTML output and LaTeX macros/environments for
    PDF output).

-   A standardized schema for authors and affiliations so that you can
    express this data once and then have it automatically formatted
    according to the styles required for various Journals.

-   The use of Citation Style Language (CSL) to automate the formatting
    of citations and bibliographies according to whatever style is
    required by various Journals.

## Journal Formats

The Quarto team has developed several Journal formats and made them
available within the
[quarto-journals](https://github.com/quarto-journals/) GitHub
organization. These formats include:

-   [ACM](https://github.com/quarto-journals/acm)
    [(preview)](https://quarto-journals.github.io/acm/)
-   [PLOS](https://github.com/quarto-journals/plos)
    [(preview)](https://quarto-journals.github.io/plos/)
-   [ASA](https://github.com/quarto-journals/jasa)
    [(preview)](https://quarto-journals.github.io/jasa/)
-   [Elsevier](https://github.com/quarto-journals/elsevier)
    [(preview)](https://quarto-journals.github.io/elsevier/)
-   [Biophysical](https://github.com/quarto-journals/biophysical-journal)
    [(preview)](https://quarto-journals.github.io/biophysical-journal/)
-   [ACS](https://github.com/quarto-journals/acs)
    [(preview)](https://quarto-journals.github.io/acs/)
-   [JSS](https://github.com/quarto-journals/jss)
    [(preview)](https://quarto-journals.github.io/jss/)

Many more formats will be added over time and we welcome proposals from
the community for contributed formats (please post an issue at
<https://github.com/quarto-journals/article-format-template/issues> if
you are interested in contributing a format).

The `quarto use template` command can be used to create an article from
one these formats. For example:

    Terminal

    quarto use template quarto-journals/acm
    quarto use template quarto-journals/plos
    quarto use template quarto-journals/elsevier
    quarto use template quarto-journals/acs
    quarto use template quarto-journals/jss

Note that the above commands will create a brand new article with
default contents. In some cases you may want to use a Journal format in
an existing document or project without copying the entire template. In
that case you can just add the format extension by itself. For example:

    Terminal

    quarto add quarto-journals/acm
    quarto add quarto-journals/plos

Follow the links for any of the formats above to learn more about how to
use them with your own articles.

## Creating Formats

While the list of supported journals on
[quarto-journals](https://github.com/quarto-journals/) will grow over
time, it’s likely that many users will want to create their own Journal
formats. Creating a new format typically involves:

1.  Adapting the LaTeX template typically provided by Journals for use
    with Quarto.
2.  Selecting the appropriate citation processing and style for use with
    the format.
3.  Creating a `template.qmd` that demonstrates using the format.
4.  Optionally, ensuring that both HTML and LaTeX articles are well
    supported.

See the article on [Journal Formats](../../docs/journals/formats.html)
for additional details on creating your own formats.

Proudly supported by [<img
src="https://www.rstudio.com/assets/img/posit-logo-fullcolor-TM.svg"
class="img-fluid" width="65" alt="Posit" />](https://posit.co)

-   <a href="../../about.html" class="nav-link"></a>

    About

-   <a href="../../docs/faq/index.html" class="nav-link"></a>

    FAQ

-   <a href="../../license.html" class="nav-link"></a>

    License

-   <a href="../../trademark.html" class="nav-link"></a>

    Trademark

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
