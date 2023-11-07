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

# Code Annotation

Add line based annotations to your code chunks

In Quarto 1.3, you can add line based annotations to code chunks to
highlight or explain parts of your code.

Features

Authoring

Quarto 1.3

Author

Charlotte Wickham

Published

March 13, 2023

Quarto 1.3 Feature

This post is part of a series highlighting new features in the 1.3
release of Quarto. Get the latest release at
<https://quarto.org/docs/download>.

Code blocks and executable code cells in Quarto may now include
line-based annotations. Line-based annotations provide a way to attach
explanation to lines of code much like footnotes.

For example, this code uses annotation to describe the steps in an R
dplyr pipeline in plain language:

    library(tidyverse)
    library(palmerpenguins)
    11penguins |>
    22  mutate(
        bill_ratio = bill_depth_mm / bill_length_mm,
        bill_area  = bill_depth_mm * bill_length_mm
      )

1  
<span code-cell="annotated-cell-1" code-lines="3"
code-annotation="1">Take `penguins`, and then,</span>

2  
<span code-cell="annotated-cell-1" code-lines="4,5,6,7"
code-annotation="2">add new columns for the bill ratio and bill
area.</span>

The default HTML annotation style displays annotations in a list below
the code block. Clicking on the annotation number in the list highlights
the relevant lines in the code. Other HTML styles hide the annotations,
revealing them in a tooltip when a user hovers or selects a marker.

The PDF format also allows for annotations, numbering, and displaying
the annotation text below the code. In other formats, like Word and
GitHub Markdown, annotations are instead labeled with the line of code
(or lines of code) to which the annotation text applies.

-   <span id="tabset-1-1-tab" class="nav-link active" bs-toggle="tab"
    bs-target="#tabset-1-1" role="tab" aria-controls="tabset-1-1"
    aria-selected="true">PDF</span>
-   <span id="tabset-1-2-tab" class="nav-link" bs-toggle="tab"
    bs-target="#tabset-1-2" role="tab" aria-controls="tabset-1-2"
    aria-selected="false">GitHub Flavored Markdown</span>

<img src="annote-pdf.png" class="img-fluid"
alt="Screenshot of output in PDF format showing code annotation." />

    ``` r
    library(tidyverse)
    library(palmerpenguins)
    penguins |>
      mutate(
        bill_ratio = bill_depth_mm / bill_length_mm,
        bill_area  = bill_depth_mm * bill_length_mm
      )
    ```

    Line 3  
    Take `penguins`, and then,

    Lines 4-7  
    add new columns for the bill ratio and bill area.

To add code annotation to a code block, you need to add two things:
specially formatted code comments in your code cell, and an ordered list
below the code cell with the annotation text:

1  
<span code-cell="annotated-cell-1" code-lines="3"
code-annotation="1">**Code Comments**: Each annotated line in the code
cell should be terminated with a comment (using the code cell’s language
comment character) followed by a space and then an annotation number
enclosed in angle brackets (e.g. `# <2>`). You may repeat an annotation
number if the annotation spans multiple lines.</span>

2  
<span code-cell="annotated-cell-1" code-lines="4,5,6,7"
code-annotation="2">**Ordered List**: An ordered list should appear
immediately after the code cell, and include the contents of each
annotation. Each numbered item in the ordered list will correspond to
the line(s) of code with the same annotation number.</span>

For example, the annotations above were produced by including the
following in the Quarto document:

    ```r
    library(tidyverse)
    library(palmerpenguins)
    penguins |>                                      # <1>
      mutate(                                        # <2>
        bill_ratio = bill_depth_mm / bill_length_mm, # <2>
        bill_area  = bill_depth_mm * bill_length_mm  # <2>
      )                                              # <2>
    ```
    1. Take `penguins`, and then,
    2. add new columns for the bill ratio and bill area.

You can read more about how to control the annotation style, and whether
annotations appear at all on the [Code Annotation
page](../../../../docs/prerelease/1.3/code-annotation.html) of the
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
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/blog/posts/2023-03-13-code-annotation/index.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
