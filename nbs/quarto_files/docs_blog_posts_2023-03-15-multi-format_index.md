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

# Multi-format Publishing

Automatically link to other formats in HTML documents

In Quarto 1.3, additional formats listed in HTML documents will
automatically be linked in an “Other Formats” section near the top of
the page.

Features

Authoring

Quarto 1.3

Author

Charlotte Wickham

Published

March 15, 2023

## Other Formats

-   <a href="index.ipynb" download="index.ipynb"><em></em>Jupyter</a>
-   [MS Word](index.docx)

Quarto 1.3 Feature

This post is part of a series highlighting new features in the 1.3
release of Quarto. Get the latest release at
<https://quarto.org/docs/download>.

Starting in Quarto 1.3, HTML pages (either standalone or in a website)
can automatically include links to other formats specified in the
document front matter. For example, the following document front matter:

    title: Sample Page
    author: Norah Jones
    date: last-modified
    toc: true
    format: 
      html: default
      ipynb: default

Results in an HTML page that includes a link to the additional notebook
format in the right margin below the table of contents:

<img src="other-format.png" class="border img-fluid"
alt="Screenshot of a HTML page that includes a link to the Jupyter format below the table of contents under the heading Other Formats." />

If a table of contents is enabled for the page, the additional formats
will be automatically placed within the table of contents as a new
section. If no table of contents is displayed, the additional formats
will be displayed in the right margin at the top of the document.

Links to additional formats are displayed by default, but you can
control whether they are shown or even which specific formats are
included with the `format-links` YAML option.

Read more about this feature on the [Multi-format
page](../../../../docs/prerelease/1.3/multi-format.html) of the
pre-release highlights.

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
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/blog/posts/2023-03-15-multi-format/index.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
