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

-   <a href="#basics" id="toc-basics" class="nav-link active"
    data-scroll-target="#basics">Basics</a>
    -   <a href="#check-the-version-of-quarto-and-its-dependencies"
        id="toc-check-the-version-of-quarto-and-its-dependencies"
        class="nav-link"
        data-scroll-target="#check-the-version-of-quarto-and-its-dependencies">Check
        the version of quarto and its dependencies</a>
    -   <a href="#get-a-stack-trace" id="toc-get-a-stack-trace" class="nav-link"
        data-scroll-target="#get-a-stack-trace">Get a stack trace</a>
    -   <a href="#verbose-mode" id="toc-verbose-mode" class="nav-link"
        data-scroll-target="#verbose-mode">Verbose mode</a>
    -   <a href="#log-files" id="toc-log-files" class="nav-link"
        data-scroll-target="#log-files">Inspect log files</a>
    -   <a href="#out-of-memory-issues" id="toc-out-of-memory-issues"
        class="nav-link"
        data-scroll-target="#out-of-memory-issues">Out-of-memory issues</a>
    -   <a href="#installer-issues" id="toc-installer-issues" class="nav-link"
        data-scroll-target="#installer-issues">Installer issues</a>
    -   <a href="#pdflatex-issues" id="toc-pdflatex-issues" class="nav-link"
        data-scroll-target="#pdflatex-issues">PDF/LaTeX issues</a>
-   <a href="#environment-libraries-and-dependencies"
    id="toc-environment-libraries-and-dependencies" class="nav-link"
    data-scroll-target="#environment-libraries-and-dependencies">Environment,
    Libraries, and Dependencies</a>
    -   <a href="#knitr" id="toc-knitr" class="nav-link"
        data-scroll-target="#knitr">knitr</a>
-   <a href="#advanced" id="toc-advanced" class="nav-link"
    data-scroll-target="#advanced">Advanced</a>
    -   <a href="#debugging-jupyter-engine-issues"
        id="toc-debugging-jupyter-engine-issues" class="nav-link"
        data-scroll-target="#debugging-jupyter-engine-issues">Debugging Jupyter
        engine issues</a>
    -   <a href="#debugging-lua-filters" id="toc-debugging-lua-filters"
        class="nav-link" data-scroll-target="#debugging-lua-filters">Debugging
        Lua filters</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/troubleshooting/index.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Troubleshooting

This page documents a number of strategies you can employ in case you
run into problems with Quarto. As always, we welcome feedback and bug
reports on the [Quarto issue
tracker](https://github.com/quarto-dev/quarto-cli/issues), but this page
might help you get up and running quickly.

## Basics

### Check the version of quarto and its dependencies

You can check the version of Quarto and its dependencies by running
`quarto check`. Here’s an example of the output it generates:

    [✓] Checking versions of quarto binary dependencies...
          Pandoc version 2.19.2: OK
          Dart Sass version 1.32.8: OK
    [✓] Checking versions of quarto dependencies......OK
    [✓] Checking Quarto installation......OK
          Version: 1.2.313
          Path: /Users/cscheid/repos/github/quarto-dev/quarto-cli/package/dist/bin

    [✓] Checking basic markdown render....OK

    [✓] Checking Python 3 installation....OK
          Version: 3.10.9
          Path: /Users/cscheid/virtualenvs/homebrew-python3/bin/python3
          Jupyter: 5.1.3
          Kernels: python3, julia-1.6, julia-1.8

    [✓] Checking Jupyter engine render....OK

    [✓] Checking R installation...........OK
          Version: 4.2.2
          Path: /Library/Frameworks/R.framework/Resources
          LibPaths:
            - /Users/cscheid/repos/github/quarto-dev/quarto-web/renv/library/R-4.2/aarch64-apple-darwin20
            - /private/var/folders/nm/m64n9_z9307305n0xtzpp54m0000gn/T/RtmpXmQfZA/renv-system-library
          rmarkdown: 2.14

    [✓] Checking Knitr engine render......OK

### Get a stack trace

Setting `QUARTO_PRINT_STACK=true` in your environment will cause Quarto
to print a stack trace when an error occurs.

-   <span id="tabset-1-1-tab" class="nav-link active" bs-toggle="tab"
    bs-target="#tabset-1-1" role="tab" aria-controls="tabset-1-1"
    aria-selected="true">Windows</span>
-   <span id="tabset-1-2-tab" class="nav-link" bs-toggle="tab"
    bs-target="#tabset-1-2" role="tab" aria-controls="tabset-1-2"
    aria-selected="false">Unix</span>

On PowerShell:

    $env:QUARTO_PRINT_STACK = "true"

On bash-like shells:

    export QUARTO_PRINT_STACK=true

### Verbose mode

Quarto will print more information about its internal state if you set
`QUARTO_LOG_LEVEL=DEBUG` in your environment.

### Inspect log files

Quarto creates log files that can help you diagnose problems. These are
stored in different locations depending on your operating system:

-   <span id="tabset-2-1-tab" class="nav-link active" bs-toggle="tab"
    bs-target="#tabset-2-1" role="tab" aria-controls="tabset-2-1"
    aria-selected="true">Windows</span>
-   <span id="tabset-2-2-tab" class="nav-link" bs-toggle="tab"
    bs-target="#tabset-2-2" role="tab" aria-controls="tabset-2-2"
    aria-selected="false">macOS</span>
-   <span id="tabset-2-3-tab" class="nav-link" bs-toggle="tab"
    bs-target="#tabset-2-3" role="tab" aria-controls="tabset-2-3"
    aria-selected="false">Linux</span>

`%LOCALAPPDATA%\quarto\logs`

`${HOME}/Library/Application Support/quarto/logs`

If `$XDG_DATA_HOME` is set, `${XDG_DATA_HOME}/.local/share/quarto/logs`,
otherwise `${HOME}/.local/share/quarto/logs`

### Out-of-memory issues

When building a large project or website, you might run into memory
limits. In that case, consider the following environment variable.

In this example, we’re setting the maximum amount of memory to be
allocated by Deno to be 8GB. Adjust this to your computer’s limits.

-   <span id="tabset-3-1-tab" class="nav-link active" bs-toggle="tab"
    bs-target="#tabset-3-1" role="tab" aria-controls="tabset-3-1"
    aria-selected="true">Windows</span>
-   <span id="tabset-3-2-tab" class="nav-link" bs-toggle="tab"
    bs-target="#tabset-3-2" role="tab" aria-controls="tabset-3-2"
    aria-selected="false">Unix</span>

On PowerShell:

    $env:QUARTO_DENO_EXTRA_OPTIONS = "--v8-flags=--max-old-space-size=8192"

On bash-like shells:

    export QUARTO_DENO_EXTRA_OPTIONS=--v8-flags=--max-old-space-size=8192

### Installer issues

-   <span id="tabset-4-1-tab" class="nav-link active" bs-toggle="tab"
    bs-target="#tabset-4-1" role="tab" aria-controls="tabset-4-1"
    aria-selected="true">macOS</span>

In macOS, installers write their output to `/var/log/install.log`.
Inspecting this file might offer hints to what went wrong.

Warning

If you’re going to ask for help on public forums, be aware that *every*
macOS installer writes to the same file `/var/log/install.log`. You
should make sure you’re not accidentally disclosing installation
information you would rather not.

### PDF/LaTeX issues

If quarto finds an existing installation of `texlive` in your system, it
will use that. If you’re seeing issues with rendering to PDF, make sure
you have an up-to-date installation of `texlive`. Alternatively, you can
have quarto use its own version, by calling `quarto install tinytex`.

## Environment, Libraries, and Dependencies

One common source of tricky problems is the presence of multiple
installations of R and Python in a system. Quarto will attempt to find
an R or Python installation, and sometimes your shell environment is
pointing to a different one.

### knitr

If you suspect that quarto is finding the wrong version of an R
installation, you can obtain information about the R installation that
Quarto sees by running the following .qmd file:

    ---
    engine: knitr
    ---

    ```{r}
    sessionInfo()
    Sys.getenv()
    .libPaths()

    # If the sessioninfo package is available, 
    # it provides output that is easier to read,
    # and can write its results to a file
    sessioninfo:::session_info(to_file = "quarto-session-info-output.txt")
    ```

You can then also run those commands from your R environment, and
compare the output. If `sessioninfo` is available, then you can ask for
a difference between the outputs more directly:

    sessioninfo:::session_diff(new = "quarto-session-info-output.txt")

## Advanced

### Debugging Jupyter engine issues

To enable Jupyter debugging, add the following to your YAML front
matter:

    execute:
      debug: true

Quarto creates a log of the execution of jupyter notebooks in its [log
directory](#log-files) under `jupyter-kernel.log`.

If Jupyter execution is hanging instead of failing, you can force
immediate flushing of the log by setting
`QUARTO_JUPYTER_FLUSH_LOGS=true` in your environment before running
quarto.

### Debugging Lua filters

#### Useful Lua helper functions

Quarto includes a number of useful Lua helper functions that can be used
to debug Lua filters. These are available in the `quarto` module, and
can be used as follows:

    quarto.log.output(obj) -- prints a potentially complex object to the console

#### Filter tracing

Setting `QUARTO_TRACE_FILTERS=<FILENAME>.json` in your environment will
cause Quarto to produce a trace of the Lua filters it runs, and write it
to disk. This will be a file written to same the directory of the
rendered file. We include an interactive Quarto document that can be
used to visualize this trace, which you can find in the `quarto-cli`
repository at
[`tools/trace-viewer/trace-viewer.qmd`](https://github.com/quarto-dev/quarto-cli/tree/main/tools/trace-viewer/trace-viewer.qmd).
Run `quarto preview trace-viewer.qmd`, and you will be shown two text
fields, “Trace 1” and “Trace 2”. Drag and drop the JSON file onto either
of the fields and you will be shown the trace. If you wish to compare
two traces, drag them onto the two fields.

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
