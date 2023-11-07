<a href="../../../index.html"
class="navbar-brand navbar-brand-logo"><img src="../../../quarto.png"
class="navbar-logo" alt="Quarto logo." /></a>

<span class="navbar-toggler-icon"></span>

-   <a href="../../../index.html" class="nav-link"><span
    class="menu-text">Overview</span></a>
-   <a href="../../../docs/get-started/index.html" class="nav-link"><span
    class="menu-text">Get Started</span></a>
-   <a href="../../../docs/guide/index.html" class="nav-link"><span
    class="menu-text">Guide</span></a>
-   <a href="../../../docs/extensions/index.html" class="nav-link"><span
    class="menu-text">Extensions</span></a>
-   <a href="../../../docs/reference/index.html" class="nav-link"><span
    class="menu-text">Reference</span></a>
-   <a href="../../../docs/gallery/index.html" class="nav-link"><span
    class="menu-text">Gallery</span></a>
-   <a href="../../../docs/blog/index.html" class="nav-link"><span
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
    -   <a href="../../../docs/faq/index.html" class="dropdown-item"><em></em>
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
-   <a href="#usage-in-notebooks" id="toc-usage-in-notebooks"
    class="nav-link" data-scroll-target="#usage-in-notebooks">Usage in
    Notebooks</a>
-   <a href="#markdown-output" id="toc-markdown-output" class="nav-link"
    data-scroll-target="#markdown-output">Markdown Output</a>
-   <a href="#escaping" id="toc-escaping" class="nav-link"
    data-scroll-target="#escaping">Escaping</a>
-   <a href="#engine-binding" id="toc-engine-binding" class="nav-link"
    data-scroll-target="#engine-binding">Engine Binding</a>
-   <a href="#syntax-compatibility" id="toc-syntax-compatibility"
    class="nav-link" data-scroll-target="#syntax-compatibility">Syntax
    Compatibility</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/prerelease/1.4/inline.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Inline Execution for Jupyter

Pre-release Feature

This feature is new in the upcoming Quarto 1.4 release. To use the
feature now, you’ll need to
[download](https://quarto.org/docs/download/prerelease) and install the
Quarto pre-release.

## Overview

Quarto v1.4 includes support for executing inline expressions when using
Jupyter kernels. Inline expressions are similar to code blocks, except
that they use a single tick (`` ` ``) rather than triple tick
(```` ``` ````) and can appear anywhere. For example, the following
code:

    ```{python}
    x = 5
    ```

    The answer is `{python} x`

Will create this markdown output:

    The answer is 5.

This syntax works for any Jupyter kernel—so for Julia you would write an
inline expression as `` `{julia} x` ``).

Caution

One important consideration with inline expressions is that they should
be confined to simple values that you have pre-computed within normal
code cells (rather than function calls that do non-trivial work). This
is because the protocol used for inline expressions is not compatible
with some Python libraries (especially those that use multi-threading or
multi-processing).

## Usage in Notebooks

Inline expressions are always evaulated when rendering and previewing
`.qmd` files. However, for notebooks you need to execute the notebook
with Quarto in order to evaluate inline expressions (i.e. they won’t be
evaluated within the JupyterLab, VS Code, or PyCharm notebook editor).

You can work in your favorite notebook front-end without Quarto
execution, then once you are ready to publish execute the notebook
during rendering as follows:

    Terminal

    $ quarto render notebook.ipynb --execute

You can also turn on execution within the YAML options of a notebook.
For example:

    ---
    title: "My Notebooks"
    execute:
      enabled: true
    ---

## Markdown Output

Note that by default, the output of inline expressions is treated as
ordinary text (i.e. markdown within it is not rendered). Any markdown
like syntax within the output of inline expressions will be
automatically escaped. For example, the following inline expression:

`` `{python} '**not bold**'` ``

Will produce the following markdown:

`\*\*not bold\*\*`

If you want to explicitly create markdown output, use the `Markdown()`
function from `IPython.display`. For example, the following inline
expression will result in bolded text:

    ```{python}
    from IPython.display import Markdown
    ```

    `{python} Markdown('**bold**')`

Note that for the Knitr engine, you use the `I()` function to designate
that inline output has markdown to render. For example:

    `{r} I('**bold**')`

## Escaping

If you are writing documentation about inline expressions (as we are in
this article!) then you may need to escape the syntax so that it doesn’t
execute. You can do that in one of two ways:

1.  Use a double-brace around the expression. For example:
    `` `{{python}} x` ``

2.  Enclose the expression in an extra backtick. For example:
    ``` ``{python} x`` ```

Each of the expressions above will render (unexpected) as
`` `{python} x` `` within the output document.

## Engine Binding

If you use inline expressions in a document that does not have any other
executable code blocks then you should explicitly set the `engine`
document option to ensure that your expressions are evaluated (automatic
engine binding works for blocks but not inlines). For example:

    ---
    title: "My Document"
    engine: jupyter
    ---

    `{python} "hello"`

## Syntax Compatibility

The Knitr and Observable engines each have their own syntax for inline
expressions. To make it easier to learn and use expressions across
engines, there is also a mapping from the Jupyter-compatible syntax to
the native synaxes of Knitr and Observable. For example:

<table class="table">
<thead>
<tr class="header header">
<th>Engine</th>
<th>Example</th>
<th>Converted</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td>Knitr</td>
<td><code>`{r} x`</code></td>
<td><code>`r x`</code></td>
</tr>
<tr class="even even">
<td>Observable</td>
<td><code>`{ojs} x`</code></td>
<td><code>${x}</code></td>
</tr>
</tbody>
</table>

So you can use either the standard Quarto inline expression syntax or
the native syntax with these engines.

Note that native Knitr inline syntax has a different default behavior
for handling of markdown content. Specificially, it treats all inline
output as *containing markdown* (whereas Quarto assumes that it
doesn’t). So a strict equivalency between the Knitr and Quarto syntax
would be:

<table class="table">
<thead>
<tr class="header header">
<th>Knitr</th>
<th>Quarto</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td><code>`r "**bold**"`</code></td>
<td><code>`{r} I("**bold**")`</code></td>
</tr>
</tbody>
</table>

Proudly supported by [<img
src="https://www.rstudio.com/assets/img/posit-logo-fullcolor-TM.svg"
class="img-fluid" width="65" alt="Posit" />](https://posit.co)

-   <a href="../../../about.html" class="nav-link"></a>

    About

-   <a href="../../../docs/faq/index.html" class="nav-link"></a>

    FAQ

-   <a href="../../../license.html" class="nav-link"></a>

    License

-   <a href="../../../trademark.html" class="nav-link"></a>

    Trademark

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
