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
-   <a href="#jupyter-cache" id="toc-jupyter-cache" class="nav-link"
    data-scroll-target="#jupyter-cache">Jupyter Cache</a>
-   <a href="#knitr-cache" id="toc-knitr-cache" class="nav-link"
    data-scroll-target="#knitr-cache">Knitr Cache</a>
-   <a href="#rendering" id="toc-rendering" class="nav-link"
    data-scroll-target="#rendering">Rendering</a>
-   <a href="#alternatives" id="toc-alternatives" class="nav-link"
    data-scroll-target="#alternatives">Alternatives</a>
    -   <a href="#disabling-execution" id="toc-disabling-execution"
        class="nav-link" data-scroll-target="#disabling-execution">Disabling
        Execution</a>
    -   <a href="#freezing-execution" id="toc-freezing-execution"
        class="nav-link" data-scroll-target="#freezing-execution">Freezing
        Execution</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/computations/caching.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Caching

## Overview

When rendering documents with embedded computations becomes
time-consuming, you may want to consider adding an execution cache,
which will store the results of cell executions so they aren’t
re-executed with every document render.

Quarto integrates with the [Jupyter
Cache](https://jupyter-cache.readthedocs.io/en/latest/) and [Knitr
Cache](https://bookdown.org/yihui/rmarkdown-cookbook/cache.html) to to
cache time consuming code chunks. These two caching facilities distinct
capabilities, and we’ll cover each in detail below.

## Jupyter Cache

[Jupyter Cache](https://jupyter-cache.readthedocs.io/en/latest/) enables
you to cache all of the cell outputs for a notebook. If any of the cells
in the notebook change then all of the cells will be re-executed.

To use Jupyter Cache you’ll want to first install the `jupyter-cache`
package:

<table class="table" style="width:71%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header header">
<th>Platform</th>
<th>Command</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td>Mac/Linux</td>
<td><div class="code-with-filename">
<div class="code-with-filename-file">
<pre><code>Terminal</code></pre>
</div>
<div id="cb1" class="sourceCode" data-filename="Terminal">
<div class="sourceCode" id="cb2"><pre
class="sourceCode bash code-with-copy"><code class="sourceCode bash"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="ex">python3</span> <span class="at">-m</span> pip install jupyter-cache</span></code></pre></div>
</div>
</div></td>
</tr>
<tr class="even even">
<td>Windows</td>
<td><div class="code-with-filename">
<div class="code-with-filename-file">
<pre><code>Terminal</code></pre>
</div>
<div id="cb2" class="sourceCode" data-filename="Terminal">
<div class="sourceCode" id="cb4"><pre
class="sourceCode powershell code-with-copy"><code class="sourceCode powershell"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>py <span class="op">-</span>m pip install jupyter<span class="op">-</span>cache</span></code></pre></div>
</div>
</div></td>
</tr>
<tr class="odd odd">
<td>Conda</td>
<td><div class="code-with-filename">
<div class="code-with-filename-file">
<pre><code>Terminal</code></pre>
</div>
<div id="cb3" class="sourceCode" data-filename="Terminal">
<div class="sourceCode" id="cb6"><pre
class="sourceCode bash code-with-copy"><code class="sourceCode bash"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a><span class="ex">conda</span> install jupyter-cache</span></code></pre></div>
</div>
</div></td>
</tr>
</tbody>
</table>

Julia Installation

Note that if you are using Julia along with the integrated Python
environment provided by `IJulia` then you should alternatively follow
the directions on [Installing Jupyter Cache for
Julia](../../docs/computations/julia.html#jupyter-cache).

To enable the cache for a document, add the `cache` option. For example:

    ---
    title: "My Document"
    format: html
    execute: 
      cache: true
    jupyter: python3
    ---

You can also specify caching at the project level. For example, within a
project file:

    project:
      type: website
      
    format:
      html:
        theme: united
        
    execute:
      cache: true

Note that changes within a document that aren’t within code cells
(e.g. markdown narrative) do not invalidate the document cache. This
makes caching a very convenient option when you are working exclusively
on the prose part of a document.

Jupyter Cache include a `jcache` command line utility that you can use
to analyze and manage the notebook cache. See the [Jupyter
Cache](https://jupyter-cache.readthedocs.io/en/latest/) documentation
for additional details.

## Knitr Cache

The Knitr Cache operates at the level of individual cells rather than
the entire document. While this can be very convenient, it also
introduced some special requirements around managing the dependencies
between cells.

You can enable the Knitr cache at the document or project level using
standard YAML options:

    ---
    title: "My Document"
    format: html
    execute: 
      cache: true
    ---

You can also enable caching on a per-cell basis (in this you would *not*
set the document level option):

    ```{r}
    #| cache: true

    summary(cars)
    ```

There are a variety of other cell-level options that affect Knitr
caching behavior. You can learn about them in the Knitr [cell
options](https://quarto.org/docs/reference/cells/cells-knitr.html#cache)
reference. Another excellent resource is Yihui Xie’s article on [cache
invalidation](https://yihui.org/en/2018/06/cache-invalidation/).

## Rendering

You can use \`quarto render\` command line options to control caching
behavior without changing the document’s code. Use options to force the
use of caching on all chunks, disable the use of caching on all chunks
(even if it’s specified in options), or to force a refresh of the cache
even if it has not been invalidated:

    Terminal

    # use a cache (even if the document options don't enable it)
    quarto render example.qmd --cache 

    # don't use a cache (even if the documentation options enable it)
    quarto render example.qmd --no-cache 

    # use a cache and force a refresh (even if the cells haven't changed)
    quarto render example.qmd --cache-refresh 

## Alternatives

If you are using caching to mitigate long render-times, there are some
alternatives you should consider alongside caching.

### Disabling Execution

If you are working exclusively with prose / markdown, you may want to
disable execution entirely. Do this by specifying the `enabled: false`
execute option For example:

    ---
    title: "My Document"
    format: html
    execute: 
      enabled: false
    ---

Note that if you are authoring using Jupyter `.ipynb` notebooks (as
opposed to plain-text `.qmd` files) then this is already the default
behavior: no execution occurs when you call `quarto render` (rather,
execution occurs as you work within the notebook).

### Freezing Execution

If you are working within a project and your main concern is the
cumulative impact of rendering many documents at once, consider using
the `freeze` option.

You can use the `freeze` option to denote that computational documents
should never be re-rendered during a global project render, or
alternatively only be re-rendered when their source file changes:

    execute:
      freeze: true  # never re-render during project render

    execute:
      freeze: auto  # re-render only when source changes

Note that `freeze` controls whether execution occurs during global
project renders. If you do an incremental render of either a single
document or a project sub-directory then code is always executed. For
example:

    Terminal

    # render single document (always executes code)
    quarto render document.qmd

    # render project subdirectory (always executes code)
    quarto render articles

Learn more about using `freeze` with projects in the article on
[managing project
execution](https://quarto.org/docs/projects/code-execution.html#freeze).

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
