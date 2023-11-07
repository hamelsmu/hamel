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

# Tarball Installation On Linux

<a href="_" id="download-url" class="btn btn-action btn-action-primary"
title="Download Quarto">_</a> <span id="download-text"
class="hidden download-text">Find your operating system in the table
below</span>

You can install Quarto for a single user on Linux by using the Quarto
tarball and following the below set of steps.

**1. Download the tarball**

    Terminal

    wget https://github.com/quarto-dev/quarto-cli/releases/download/v^version^/quarto-^version^-linux-amd64.tar.gz

**2. Extract Files**

Extract the contents of the tarball to the location where you typically
install software (e.g. `~/opt`). For example:

    Terminal

    mkdir ~/opt
    tar -C ~/opt -xvzf quarto-^version^-linux-amd64.tar.gz

**3. Create a Symlink**

Create a symlink to `bin/quarto` in a folder that is in your path. If
there is no such folder, you can create a folder such as `~/bin` and
place the symlink there. For example:

For example:

    Terminal

    mkdir ~/bin
    ln -s ~/opt/quarto-^version^/bin/quarto ~/bin/quarto

**4. Add Folder to Path**

Ensure that the folder where you created a symlink is in the path. For
example:

    Terminal

    ( echo ""; echo 'export PATH=$PATH:~/bin\n' ; echo "" ) >> ~/.profile
    source ~/.profile

**5. Check The Installation**

Use `quarto check` to confirm that the installation is successful:

    Terminal

    quarto check

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

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/download/tarball.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
