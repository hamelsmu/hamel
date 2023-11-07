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

-   <a href="#goals" id="toc-goals" class="nav-link active"
    data-scroll-target="#goals">Goals</a>
-   <a href="#project" id="toc-project" class="nav-link"
    data-scroll-target="#project">Project</a>
-   <a href="#contribute" id="toc-contribute" class="nav-link"
    data-scroll-target="#contribute">Contribute</a>

-   <a href="https://github.com/quarto-dev/quarto-web/edit/main/about.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# About Quarto

Open source tools for scientific and technical publishing

## Goals

The overarching goal of Quarto is to make the process of creating and
collaborating on scientific and technical documents dramatically better.
We hope to do this in several dimensions:

-   Create a writing and publishing environment with great integrated
    tools for technical content. We want to make authoring with embedded
    code, equations, figures, complex diagrams, interactive widgets,
    citations, cross references, and the myriad other special
    requirements of scientific discourse straightforward and productive
    for everyone.

-   Help authors take full advantage of the web as a connected,
    interactive platform for communications, while still providing the
    ability to create excellent printed output from the same document
    source. Researchers shouldn’t need to choose between LaTeX, MS Word,
    and HTML but rather be able to author documents that target all of
    them at the same time.

-   Make reproducible research and publications the norm rather than the
    exception. Reproducibility requires that the code and data required
    to create a manuscript are an integrated part of it. However, this
    isn’t often straightforward in practice—Quarto aims to make it
    easier to adopt a reproducible workflow than not.

Quarto is open source software licensed under the [GNU GPL
v2](./license.html). We believe that it’s better for everyone if the
tools used for research and science are free and open. Reproducibility,
widespread sharing of knowledge and techniques, and the leveling of the
playing field by eliminating cost barriers are but a few of the shared
benefits of free software in science.

## Project

At the core of Quarto is [Pandoc](https://pandoc.org), a powerful and
flexible document processing tool. Quarto adds a number of facilities to
Pandoc aimed at scientific and technical publishing, including:

1.  Embedding code and output from Python, R, and JavaScript via
    integration with [Jupyter](https://jupyter.org/),
    [Knitr](https://yihui.org/knitr/), and
    [Observable](https://github.com/observablehq/).

2.  A variety of extensions to Pandoc markdown useful for technical
    writing including cross-references, sub-figures, layout panels,
    hoverable citations and footnotes, callouts, and more.

3.  A project system for rendering groups of documents at once, sharing
    options across documents, and producing aggregate output like
    [websites](./docs/websites/index.html) and
    [books](./docs/books/index.html).

Development of Quarto is sponsored by [Posit,
PBC](https://www.posit.co), where we previously created a similar system
([R Markdown](https://rmarkdown.rstudio.com/)) that shared the same
goals, but was targeted principally at users of the R language. The same
core team works on both Quarto and R Markdown:

-   J.J. Allaire ([@jjallaire](https://github.com/jjallaire/))
-   Christophe Dervieux ([@cderv](https://github.com/cderv))
-   Carlos Scheidegger ([@cscheid](https://github.com/cscheid))
-   Charles Teague ([@dragonstyle](https://github.com/dragonstyle))
-   Yihui Xie ([@yihui](https://github.com/yihui))

With Quarto, we are hoping to bring these tools to a much wider
audience.

Quarto is a registered trademark of Posit. Please see our [trademark
policy](./trademark.html) for guidelines on usage of the Quarto
trademark.

## Contribute

You can contribute to Quarto in many ways:

-   By opening issues to provide feedback and share ideas.
-   By submitting Pull Request (PR) to fix opened issues
-   By submitting Pull Request (PR) to suggest new features (it is
    considered good practice to open an issue for discussion before
    working on a pull request for a new feature).

Please be mindful of our [code of
conduct](https://github.com/quarto-dev/quarto-cli/blob/main/.github/CODE_OF_CONDUCT.md)
as you interact with other community members.

### Pull Requests

Pull requests are very welcome! Here’s how to contribute via PR:

1.  [Fork](https://github.com/quarto-dev/quarto-cli/fork) the
    repository, clone it locally, and make your changes in a new branch
    specific to the PR. For example:

        Terminal

        # clone your fork
        $ git clone https://github.com/<username>/quarto-cli

        # configure for your platform (./configure.sh or ./configure.cmd for windows)
        $ cd quarto-cli
        $ ./configure.sh

        # checkout a new branch
        $ git checkout -b feature/newthing

2.  For significant changes (e.g more than small bug fixes), ensure that
    you have signed the
    [individual](https://posit.co/wp-content/uploads/2023/04/2023-03-13_TC_Indiv_contrib_agreement.pdf)
    or
    [corporate](https://posit.co/wp-content/uploads/2023/04/2023-03-13_TC_Corp_contrib_agreement.pdf)
    contributor agreement as appropriate. You can send the signed copy
    to <jj@rstudio.com>.

3.  Submit the [pull
    request](https://help.github.com/articles/using-pull-requests). It
    is ok to submit as draft in your are still working on it but would
    like some feedback from us. It always good to share in the open that
    you are working on it.

We’ll try to be as responsive as possible in reviewing and accepting
pull requests.

Proudly supported by [<img
src="https://www.rstudio.com/assets/img/posit-logo-fullcolor-TM.svg"
class="img-fluid" width="65" alt="Posit" />](https://posit.co)

-   <a href="./about.html" class="nav-link active" aria-current="page"></a>

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
