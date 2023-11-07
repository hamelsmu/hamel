<a href="./index.html" class="navbar-brand navbar-brand-logo"><img
src="./quarto.png" class="navbar-logo" alt="Quarto logo." /></a>

<span class="navbar-toggler-icon"></span>

-   <a href="./index.html" class="nav-link"><span
    class="menu-text">Overview</span></a>
-   <a href="./docs/get-started/index.html" class="nav-link"><span
    class="menu-text">Get Started</span></a>
-   <a href="./docs/guide/index.html" class="nav-link"><span
    class="menu-text">Guide</span></a>
-   <a href="./docs/extensions/index.html" class="nav-link"><span
    class="menu-text">Extensions</span></a>
-   <a href="./docs/reference/index.html" class="nav-link"><span
    class="menu-text">Reference</span></a>
-   <a href="./docs/gallery/index.html" class="nav-link"><span
    class="menu-text">Gallery</span></a>
-   <a href="./docs/blog/index.html" class="nav-link"><span
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
    -   <a href="./docs/faq/index.html" class="dropdown-item"><em></em> <span
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

## On this page

-   <a href="#rule-0-please-submit-your-bug-report-anyway"
    id="toc-rule-0-please-submit-your-bug-report-anyway"
    class="nav-link active"
    data-scroll-target="#rule-0-please-submit-your-bug-report-anyway">Rule
    0: Please submit your bug report anyway!</a>
-   <a href="#small-is-beautiful-aim-for-a-single-document-with-10-lines"
    id="toc-small-is-beautiful-aim-for-a-single-document-with-10-lines"
    class="nav-link"
    data-scroll-target="#small-is-beautiful-aim-for-a-single-document-with-10-lines">Small
    is beautiful: Aim for a single document with ~10 lines</a>
-   <a href="#formatting-make-githubs-markdown-work-for-us"
    id="toc-formatting-make-githubs-markdown-work-for-us" class="nav-link"
    data-scroll-target="#formatting-make-githubs-markdown-work-for-us">Formatting:
    Make GitHub’s markdown work for us</a>
    -   <a
        href="#dont-hold-back-tell-us-anything-you-think-might-make-a-difference"
        id="toc-dont-hold-back-tell-us-anything-you-think-might-make-a-difference"
        class="nav-link"
        data-scroll-target="#dont-hold-back-tell-us-anything-you-think-might-make-a-difference">Don’t
        hold back: Tell us anything you think might make a difference</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/bug-reports.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Bug Reports

How to make an actionable bug report for Quarto

We want to hear about Quarto bugs and, we want to fix those bugs! The
following guidance will help us be as efficient as we can.

### Rule 0: Please submit your bug report anyway!

We have a better chance to fix your code quickly if you follow the
instructions below. Still, we know that this takes work and isn’t always
possible.

**We would rather have a record of the problem than not know about it**.

We appreciate bug reports even if you are unable to take any or all of
the following steps:

### Small is beautiful: Aim for a single document with ~10 lines

The most helpful thing you can do to help us is to provide a minimal,
self-contained, and reproducible example.

-   **minimal**: This will often mean turning your large website project
    into a project with a single small document, and a single large
    `.qmd` file into a small (ideally, about 10-20 total lines of code)
    example. By doing this, you might also be able to learn more
    specifically what the problem is.
-   **self-contained**: The more software dependencies we need to
    understand and install, the harder it is to track the bug down. As
    you reduce the code, remove as many dependencies as possible.
-   **reproducible**: If we cannot run your example, we cannot track the
    bug down. Please make sure the file you submitted is enough to
    trigger the bug on its own.

## Formatting: Make GitHub’s markdown work for us

The easiest way to include a `.qmd` file in a comment is to wrap it in a
code block. To make sure that GitHub doesn’t format your own `.qmd`,
start and end your block with more backticks than you use in your `.qmd`
file. In order to show `.qmd` files with three backticks (the most
common case), use *four* backticks in your GitHub Issue:

    ```
    This is a code block
    ```

Sometimes you might need more backticks:

    ````
    This is a four backticks block.

    ```
    This is a code block
    ```
    ````

### Don’t hold back: Tell us anything you think might make a difference

Although we want the `.qmd` file to be small, we still can use as much
information from you as you’re willing to share. Tell us all!,
including:

-   The version of quarto you’re running
-   The operating system you’re running
-   The IDE you’re using, and its version

If you are seeing an error from Quarto, you can also provide additional
diagnostic information by defining the `QUARTO_PRINT_STACK` environment
variable.

For example on Unix:

    export QUARTO_PRINT_STACK=true
    quarto render document.qmd

or on Windows in a Powershell Terminal

    $ENV:QUARTO_PRINT_STACK="true"
    quarto render document.qmd

Proudly supported by [<img
src="https://www.rstudio.com/assets/img/posit-logo-fullcolor-TM.svg"
class="img-fluid" width="65" alt="Posit" />](https://posit.co)

-   <a href="./about.html" class="nav-link"></a>

    About

-   <a href="./docs/faq/index.html" class="nav-link"></a>

    FAQ

-   <a href="./license.html" class="nav-link"></a>

    License

-   <a href="./trademark.html" class="nav-link"></a>

    Trademark

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
