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

-   <a href="#getting-started" id="toc-getting-started"
    class="nav-link active" data-scroll-target="#getting-started">Getting
    Started</a>
-   <a href="#typst-format" id="toc-typst-format" class="nav-link"
    data-scroll-target="#typst-format">Typst Format</a>
-   <a href="#bibliography" id="toc-bibliography" class="nav-link"
    data-scroll-target="#bibliography">Bibliography</a>
-   <a href="#typst-blocks" id="toc-typst-blocks" class="nav-link"
    data-scroll-target="#typst-blocks">Typst Blocks</a>
-   <a href="#raw-blocks" id="toc-raw-blocks" class="nav-link"
    data-scroll-target="#raw-blocks">Raw Blocks</a>
-   <a href="#typst-file-.typ" id="toc-typst-file-.typ" class="nav-link"
    data-scroll-target="#typst-file-.typ">Typst File (<code>.typ</code>)</a>
-   <a href="#known-limitations" id="toc-known-limitations" class="nav-link"
    data-scroll-target="#known-limitations">Known Limitations</a>
-   <a href="#custom-formats" id="toc-custom-formats" class="nav-link"
    data-scroll-target="#custom-formats">Custom Formats</a>
    -   <a href="#template-partials" id="toc-template-partials" class="nav-link"
        data-scroll-target="#template-partials">Template Partials</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/prerelease/1.4/typst.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Typst Format

Pre-release Feature

This feature is new in the upcoming Quarto 1.4 release. To use the
feature now, you’ll need to
[download](https://quarto.org/docs/download/prerelease) and install the
Quarto pre-release.

Quarto v1.4 includes support for the `typst` output format.
[Typst](https://github.com/typst/typst) is a new open-source
markup-based typesetting system that is designed to be as powerful as
LaTeX while being much easier to learn and use. Typst creates beautiful
PDF output with blazing fast render times.

## Getting Started

To try out the `typst` format:

1.  Download and install the [latest
    pre-release](https://quarto.org/docs/download/prerelease) of Quarto
    1.4 (ensure you have installed Quarto v1.4.145 or higher).

2.  Create a document that uses `format: typst`. For example:

        ---
        title: "My document"
        format: typst
        ---

        Hello, typst!

Rendering or previewing this document will invoke the Typst CLI to
create a PDF from your markdown source file. Note that Quarto includes
version 0.8 of the Typst CLI so no separate installation of Typst is
required.

## Typst Format

When authoring a Typst document you’ll be using a Quarto format that is
in turn based on a Typst template, which defines its structure, layout,
and available options. The default Typst format and template that ships
with Quarto (`format: typst`) includes options for specifying title,
author, and abstract information along with basic layout and appearance
(numbering, margins, fonts, columns, etc.).

The following options are available for customizing Typst output:

<table class="table">
<colgroup>
<col style="width: 35%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header header">
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td><code>title</code></td>
<td>Main document title</td>
</tr>
<tr class="even even">
<td><code>author</code></td>
<td>One or more document authors.</td>
</tr>
<tr class="odd odd">
<td><code>date</code></td>
<td>Date of publication</td>
</tr>
<tr class="even even">
<td><code>abstract</code></td>
<td>Article abstract</td>
</tr>
<tr class="odd odd">
<td><code>toc</code></td>
<td>Include a table of contents.</td>
</tr>
<tr class="even even">
<td><code>number-sections</code></td>
<td>Apply numbering to sections and sub-sections</td>
</tr>
<tr class="odd odd">
<td><code>section-numbering</code></td>
<td>Schema to use for numbering sections, e.g. <code>1.1.a</code>.</td>
</tr>
<tr class="even even">
<td><code>margin</code></td>
<td>Margins: <code>x</code>, <code>y</code>, <code>top</code>, <code>bottom</code>, <code>left</code>, <code>right</code>.
Specified with units (e.g. <code>y: 1.25in</code> or
<code>x: 2cm</code>).</td>
</tr>
<tr class="odd odd">
<td><code>papersize</code></td>
<td>Paper size: <code>a4</code>, <code>us-letter</code>, etc. See the
docs on <a
href="https://typst.app/docs/reference/layout/page/#parameters–paper">paper
sizes</a> for all available sizes.</td>
</tr>
<tr class="even even">
<td><code>fontsize</code></td>
<td>Font size (e.g., <code>12pt</code>)</td>
</tr>
<tr class="odd odd">
<td><code>columns</code></td>
<td>Number of columns for body text.</td>
</tr>
<tr class="even even">
<td><code>include-in-header</code></td>
<td><code>.typ</code> file to include in header</td>
</tr>
<tr class="odd odd">
<td><code>include-before-body</code></td>
<td><code>.typ</code> file to include before body</td>
</tr>
<tr class="even even">
<td><code>include-after-body</code></td>
<td><code>.typ</code> file to include after the body</td>
</tr>
<tr class="odd odd">
<td><code>keep-typ</code></td>
<td>Keep the intermediate <code>.typ</code> file after render.</td>
</tr>
<tr class="even even">
<td><code>bibliography</code></td>
<td><code>.bib</code> file to use for citations processing</td>
</tr>
<tr class="odd odd">
<td><code>bibliographystyle</code></td>
<td>Style to use with Typst’s bibliography processing - See the doc
about <a
href="https://typst.app/docs/reference/meta/bibliography/#parameters–style">bibliography</a>
to see supported style.</td>
</tr>
<tr class="even even">
<td><code>citeproc</code></td>
<td>If <code>true</code>, Pandoc’s citeproc will be used for citation
processing instead of Typst’s own system (which is the default).</td>
</tr>
<tr class="odd odd">
<td><code>csl</code></td>
<td><code>.csl</code> file to use when Pandoc’s citeproc is used.</td>
</tr>
</tbody>
</table>

For example:

    ---
    title: "My Document"
    format:
      typst:
        toc: true
        section-numbering: 1.1.a
        columns: 2
    bibliography: refs.bib
    bibliographystyle: chicago-author-date
    ---

See the section below on [Custom Formats](#custom-formats) for details
on creating your own specialized formats for use with Typst.

## Bibliography

Typst comes with its [own citation processing system for
Bibliography](https://typst.app/docs/reference/meta/bibliography/) and
using `format: typst` defaults to it. If you prefer to use Pandoc’s
citation processing with a `.csl` file (e.g to use same `.csl` for a
HTML and PDF document), set `citeproc: true` explicitly in YAML header.

    ---
    title: Typst doc using citeproc
    format: typst
    citeproc: true
    bibliography: refs.bib
    csl: https://www.zotero.org/styles/apa-with-abstract
    ---

## Typst Blocks

If you want to change the appearance of blocks using native Typst
`#block()` calls, you can add the `.block` class to a Div and provide
whatever arguments are appropriate. For example:

    ::: {.block fill="luma(230)" inset="8pt" radius="4pt"}

    This is a block with gray background and slightly rounded corners.

    :::

This gets compiled to

    #block(fill:luma(230), inset=8pt, radius=4pt, 
    [This is a block with gray background and slightly rounded corners])

## Raw Blocks

If you want to use raw `typst` markup, use a raw `typst` block. For
example:

    ```{=typst} 
    #set par(justify: true)

    == Background 
    In the case of glaciers, fluid dynamics principles can be used to understand how the movement and behavior of the ice is influenced by factors such as temperature, pressure, and the presence of other fluids (such as water).
    ```

To learn more about `typst` markup, see the tutorial here:
<https://typst.app/docs/tutorial/>.

## Typst File (`.typ`)

The rendering process produces a native Typst file (`.typ)` which is
then compiled to PDF using the Typst CLI. This intermediate file is then
automatically removed. If you want to preserve the `.typ` file, use the
`keep-typ` option. For example:

    ---
    title: "My Document"
    format:
      typst:
        keep-typ: true
    ---

You can compile a `.typ` file to PDF directly using the
`quarto typst compile` command in a terminal. For example:

    Terminal

    $ quarto typst compile article.typ

The `quarto typst` command uses the version of Typst built in to Quarto
and support all Typst CLI actions and flags. For example, to determine
the version of Typst embedeed in Quarto:

    Terminal

    $ quarto typst --version

## Known Limitations

-   Callouts are not yet supported (they become block quotes with a bold
    heading)
-   Advanced page layout (panel layout, margin layout, etc.) does not
    work
-   Various other small things might not yet be implemented, please let
    us know if you see things that could use improvement!

## Custom Formats

You can create highly customized output with Typst by defining a new
format based on a custom Typst template. The Typst team has created
several useful [templates](https://github.com/typst/templates), a few
which which have been adapted for use with Quarto as custom formats.
These formats include:

<table class="table">
<colgroup>
<col style="width: 20%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header header">
<th>Format</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td><a
href="https://github.com/quarto-ext/typst-templates/tree/main/poster">Poster</a></td>
<td><code>quarto use template quarto-ext/typst-templates/poster</code></td>
</tr>
<tr class="even even">
<td><a
href="https://github.com/quarto-ext/typst-templates/tree/main/ieee">IEEE</a></td>
<td><code>quarto use template quarto-ext/typst-templates/ieee</code></td>
</tr>
<tr class="odd odd">
<td><a
href="https://github.com/quarto-ext/typst-templates/tree/main/ams">AMS</a></td>
<td><code>quarto use template quarto-ext/typst-templates/ams</code></td>
</tr>
<tr class="even even">
<td><a
href="https://github.com/quarto-ext/typst-templates/tree/main/letter">Letter</a></td>
<td><code>quarto use template quarto-ext/typst-templates/letter</code></td>
</tr>
<tr class="odd odd">
<td><a
href="https://github.com/quarto-ext/typst-templates/tree/main/fiction">Fiction</a></td>
<td><code>quarto use template quarto-ext/typst-templates/fiction</code></td>
</tr>
<tr class="even even">
<td><a
href="https://github.com/quarto-ext/typst-templates/tree/main/dept-news">Dept
News</a></td>
<td><code>quarto use template quarto-ext/typst-templates/dept-news</code></td>
</tr>
</tbody>
</table>

The source code for these formats is available at
<https://github.com/quarto-ext/typst-templates>.

To create a new custom Typst format (or package an existing Typst
template for use with Quarto) use the `quarto create` command to get
started:

    Terminal

    $ quarto create extension format

Then, choose `typst` as the base format and provide a name for the
extension (e.g. `letter`). A sample Typst format extension will be
created based on the code used in the default template that ships with
Quarto. It will include the following files which you can edit to
implement your custom format:

To implement the custom format, edit the following files:

<table class="table">
<colgroup>
<col style="width: 35%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header header">
<th>File</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td><code>_extension.yml</code></td>
<td>Basic extension metadata (name, author, description, etc.) and
format definition.</td>
</tr>
<tr class="even even">
<td><code>README.md</code></td>
<td>Documentation on how to install and use the format.</td>
</tr>
<tr class="odd odd">
<td><code>template.qmd</code></td>
<td>A starter document that demonstrates the basics of the format.</td>
</tr>
<tr class="even even">
<td><code>typst-template.typ</code></td>
<td>The core Typst template function (documentation on creating Typst
templates can be found here: <a
href="https://typst.app/docs/tutorial/making-a-template/"
class="uri">https://typst.app/docs/tutorial/making-a-template/</a>).</td>
</tr>
<tr class="odd odd">
<td><code>typst-show.typ</code></td>
<td>File that calls the template’s function (mapping Pandoc metadata to
function arguments).</td>
</tr>
</tbody>
</table>

Additional resources you might find useful when creating custom formats
include:

-   The official Typst tutorial on [Making a
    Template](https://typst.app/docs/tutorial/making-a-template/)

-   List of third party templates from the [Awesome
    Quarto](https://github.com/qjcg/awesome-typst#templates--libraries)
    repo.

### Template Partials

Note

This section covers advanced customization of Typst format output and
can be safely ignored unless you have found the method of defining
custom Typst formats described above too limited.

Above we describe a method of creating a Typst format based on
specifying two [template
partials](https://quarto.org/docs/journals/templates.html#template-partials)
(`typst-template.typ` and `typst-show.typ`). These partials customize
components of the default Typst Pandoc template, but leave some of the
core scaffolding including definitions required by Pandoc for its Typst
output as well as handling of bibliographies and footnotes (this means
that your own custom Typst formats do not need to explicitly handle
them).

If you would like to fully override the Pandoc template used for
rendering Typst, use the `template` option in your custom format (rather
than `template-partials`) and provide an alternate implementation of the
default template. For example, your `_extensions.yml` might look like
this:

    _extensions.yml

    ---
    title: Typst Custom Format
    author: Jane Smith
    version: "0.2.0"
    quarto-required: ">=1.4.11"
    contributes:
      formats:
        typst:
          template: template.typ
          template-partials:
            - typst-template.typ
            - typst-show.typ
    ---

Use the [source
code](https://github.com/quarto-dev/quarto-cli/blob/main/src/resources/formats/typst/pandoc/quarto/template.typ)
of the default template as a starting point for your `template.typ`.
Note that you can call all of the template partials provided by Quarto
(e.g. `biblio.typ()` or `notes.typ()` from within your custom template
implementation.

The [AMS](https://github.com/quarto-ext/typst-templates/tree/main/ams)
format provides an example of redefining the main template (in that
case, it is to prevent automatic bibliography processing by Quarto in
deference to the built-in handling of the Typst AMS template).

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
