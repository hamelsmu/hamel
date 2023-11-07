<a href="../../../index.html"
class="navbar-brand navbar-brand-logo"><img src="../../../quarto.png"
class="navbar-logo" alt="Quarto logo." /></a>

<span class="navbar-toggler-icon"></span>

-   <a href="../../../index.html" class="nav-link"><span
    class="menu-text">Overview</span></a>
-   <a href="../../../docs/get-started/index.html" class="nav-link active"
    aria-current="page"><span class="menu-text">Get Started</span></a>
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

1.  Tutorial: Hello, Quarto

<span class="flex-grow-1" role="button" bs-toggle="collapse"
bs-target=".quarto-sidebar-collapse-item" aria-controls="quarto-sidebar"
aria-expanded="false" aria-label="Toggle sidebar navigation"
onclick="if (window.quartoToggleHeadroom) { window.quartoToggleHeadroom(); }"></span>

-   <a href="../../../docs/get-started/index.html"
    class="sidebar-item-text sidebar-link"><span class="menu-text">Get
    Started</span></a>

-   <a href="../../../docs/get-started/hello/"
    class="sidebar-item-text sidebar-link"><span class="menu-text">Tutorial:
    Hello, Quarto</span></a>

-   <a href="../../../docs/get-started/computations/"
    class="sidebar-item-text sidebar-link"><span class="menu-text">Tutorial:
    Computations</span></a>

-   <a href="../../../docs/get-started/authoring/"
    class="sidebar-item-text sidebar-link"><span class="menu-text">Tutorial:
    Authoring</span></a>

## On this page

-   <a href="#overview" id="toc-overview" class="nav-link active"
    data-scroll-target="#overview">Overview</a>
-   <a href="#rendering" id="toc-rendering" class="nav-link"
    data-scroll-target="#rendering">Rendering</a>
-   <a href="#authoring" id="toc-authoring" class="nav-link"
    data-scroll-target="#authoring">Authoring</a>
    -   <a href="#yaml-header" id="toc-yaml-header" class="nav-link"
        data-scroll-target="#yaml-header">YAML header</a>
    -   <a href="#code-chunks" id="toc-code-chunks" class="nav-link"
        data-scroll-target="#code-chunks">Code chunks</a>
    -   <a href="#markdown-text" id="toc-markdown-text" class="nav-link"
        data-scroll-target="#markdown-text">Markdown text</a>
-   <a href="#how-it-works" id="toc-how-it-works" class="nav-link"
    data-scroll-target="#how-it-works">How it works</a>
-   <a href="#next-up" id="toc-next-up" class="nav-link"
    data-scroll-target="#next-up">Next Up</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/get-started/hello/rstudio.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Tutorial: Hello, Quarto

-   <a href="vscode.html" class="nav-link"><img
    src="../images/vscode-logo.png" />VS Code</a>
-   <a href="jupyter.html" class="nav-link"><img
    src="../images/jupyter-logo.png" />Jupyter</a>
-   <a href="rstudio.html" class="nav-link"><img
    src="../images/rstudio-logo.png" />RStudio</a>
-   <a href="neovim.html" class="nav-link"><img
    src="../images/neovim-logo.svg" />Neovim</a>
-   <a href="text-editor.html" class="nav-link"><img
    src="../images/text-editor-logo.png" id="text-editor-logo" />Editor</a>

## Overview

Quarto is a multi-language,
[next-generation](../../../docs/faq/rmarkdown.html) version of R
Markdown from Posit and includes dozens of new features and capabilities
while at the same being able to render most existing Rmd files without
modification.

In this tutorial, we’ll show you how to use RStudio with Quarto. You’ll
edit code and markdown in RStudio just as you would with any
computational document (e.g., R Markdown) and preview the rendered
document in the Viewer tab as you work.

The following is a Quarto document with the extension `.qmd` (on the
left), along with its rendered version as HTML (on the right). You could
also choose to render it into other formats like PDF, MS Word, etc.

<img src="images/rstudio-hello.png"
class="border column-page-right img-fluid quarto-figure-center"
alt="RStudio with a Quarto document titled &quot;Penguins, meet Quarto!&quot; open on the left side and the rendered version of the document on the right side." />

This is the basic model for Quarto publishing—take a source document and
render it to a variety of output formats.

If you would like a video introduction to Quarto before you dive into
the tutorial, watch the [Get Started with
Quarto](https://youtu.be/_f3latmOhew) where you can see a preview of
authoring a Quarto document with executable code chunks, rendering to
multiple formats, including revealjs presentations, creating a website,
and publishing on QuartoPub.

# An error occurred.

<a href="https://www.youtube.com/watch?v=_f3latmOhew"
target="_blank">Try watching this video on www.youtube.com</a>, or
enable JavaScript if it is disabled in your browser.

If you would like to follow along with this tutorial in your own
environment, follow the steps outlined below.

1.  Download and install the latest release of RStudio (v2023.06):

    [Download RStudio
    v2023.06](https://posit.co/download/rstudio-desktop/)

2.  Be sure that you have installed the `tidyverse` and `palmerpenguins`
    packages:

        install.packages("tidyverse")
        install.packages("palmerpenguins")

3.  Download the Quarto document (`.qmd`) below, open it in RStudio, and
    click on <span
    class="kbd"><img src="images/rstudio-render-button.png" width="25" height="20" /></span>
    Render.

    <a href="rstudio/_hello.qmd" download="hello.qmd">Download hello.qmd</a>

## Rendering

Use the <span
class="kbd"><img src="images/rstudio-render-button.png" width="25" height="20" /></span>
**Render** button in the RStudio IDE to render the file and preview the
output with a single click or keyboard shortcut (⇧⌘K).

<img src="images/rstudio-render.png"
class="border img-fluid quarto-figure-center"
alt="Top of the text editor in RStudio with the Render button highlighted with a purple box." />

If you prefer to automatically render whenever you save, you can check
the Render on Save option on the editor toolbar. The preview will update
whenever you re-render the document. Side-by-side preview works for both
HTML and PDF outputs.

<img src="images/rstudio-render-on-save.png"
class="border img-fluid quarto-figure-center"
alt="Top of the text editor in RStudio with the Render on Save checkbox checked and highlighted with a purple box." />

Note that documents can also be rendered from the R console via the
**quarto** package:

    install.packages("quarto")
    quarto::quarto_render("hello.qmd")

When rendering, Quarto generates a new file that contains selected text,
code, and results from the .qmd file. The new file can be an
[HTML](https://quarto.org/docs/output-formats/all-formats.html),
[PDF](https://quarto.org/docs/output-formats/pdf-basics.html), [MS
Word](https://quarto.org/docs/output-formats/ms-word.html) document,
[presentation](https://quarto.org/docs/presentations/),
[website](https://quarto.org/docs/websites/),
[book](https://quarto.org/docs/books/), [interactive
document](https://quarto.org/docs/interactive/), or [other
format](https://quarto.org/docs/output-formats/all-formats.html).

## Authoring

In the image below, we can see the same document in the two modes of the
RStudio editor: visual (on the left) and source (on the right).
RStudio’s [visual editor](../../../docs/visual-editor/) offers an
[WYSIWYM](https://en.wikipedia.org/wiki/WYSIWYM) authoring experience
for markdown. For formatting (e.g., bolding text), you can use the
toolbar, a keyboard shortcut (⌘B), or the markdown construct
(`**bold**`). The plain text source code underlying the document is
written for you, and you can view/edit it at any point by switching to
source mode for editing. You can toggle back and forth between these two
modes by clicking on **Source** and **Visual** in the editor toolbar (or
using the keyboard shortcut ⌘⇧ F4).

<img src="images/rstudio-source-visual.png"
class="column-page-right img-fluid quarto-figure-center"
alt="On the left: Document in the visual editor. On the right: Same document in the source editor. The visual/source editor toggle is highlighted in both documents marking their current state. The document shown is the &quot;Hello Quarto&quot; document from a previous image on the page." />

Next, let’s turn our attention to the contents of our Quarto document.
The file contains three types of content: a YAML header, code chunks,
and markdown text.

### YAML header

An (optional) YAML header demarcated by three dashes (`---`) on either
end.

    ---
    title: "Hello, Quarto"
    format: html
    editor: visual
    ---

When rendered, the `title`, `"Hello, Quarto"`, will appear at the top of
the rendered document with a larger font size than the rest of the
document. The other two YAML fields denote that the output should be in
`html` `format` and the document should open in the `visual` `editor` by
default.

The basic syntax of YAML uses key-value pairs in the format
`key: value`. Other YAML fields commonly found in headers of documents
include metadata like `author`, `subtitle`, `date` as well as
customization options like `theme`, `fontcolor`, `fig-width`, etc. You
can find out about all available YAML fields for HTML documents
[here](../../../docs/reference/formats/html.html). The available YAML
fields vary based on document format, e.g., see
[here](../../../docs/reference/formats/pdf.html) for YAML fields for PDF
documents and [here](../../../docs/reference/formats/docx.html) for MS
Word.

### Code chunks

R code chunks identified with `{r}` with (optional) chunk options, in
YAML style, identified by `#|` at the beginning of the line.

    ```{r}
    #| label: load-packages
    #| include: false

    library(tidyverse)
    library(palmerpenguins)
    ```

In this case, the `label` of the code chunk is `load-packages`, and we
set `include` to `false` to indicate that we don’t want the chunk itself
or any of its outputs in the rendered documents.

In addition to rendering the complete document to view the results of
code chunks, you can also run each code chunk interactively in the
RStudio editor by clicking the <img
src="https://d33wubrfki0l68.cloudfront.net/18153fb9953057ee5cff086122bd26f9cee8fe93/3aba9/images/notebook-run-chunk.png"
class="img-fluid" /> icon or keyboard shortcut (⇧⌘⏎). RStudio executes
the code and displays the results either inline within your file or in
the Console, depending on your preference.

<img src="images/rstudio-inline-output.png"
class="img-fluid quarto-figure-center"
alt="In the background, the code chunk labeled plot-penguins from hello.qmd. The chunk is partially covered by its output, a scatterplot showing the relationship between bill length and flipper length of penguins, colors by species. The button for running the code chunk is highlighted, and an arrow extends to the plot, showing that clicking the button results in the plot being generated." />

### Markdown text

Text with formatting, including section headers, hyperlinks, an embedded
image, and an inline code chunk.

<img src="images/rstudio-text.png"
class="border img-fluid quarto-figure-center"
alt="Text portion of the of the linked example document titled &quot;Penguins, meet Quarto!&quot;, with an annotation that reads &quot;Text&quot;." />

Quarto uses markdown syntax for text. If using the visual editor, you
won’t need to learn much markdown syntax for authoring your document, as
you can use the menus and shortcuts to add a header, bold text, insert a
table, etc. If using the source editor, you can achieve these with
markdown expressions like `##`, `**bold**`, etc.

## How it works

When you render a Quarto document, first
[knitr](http://yihui.name/knitr/) executes all of the code chunks and
creates a new markdown (.md) document, which includes the code and its
output. The markdown file generated is then processed by
[pandoc](http://pandoc.org/), which creates the finished format. The
Render button encapsulates these actions and executes them in the right
order for you.

<img src="images/rstudio-qmd-how-it-works.png"
class="border img-fluid quarto-figure-center"
alt="Workflow diagram starting with a qmd file, then knitr, then md, then pandoc, then PDF, MS Word, or HTML." />

## Next Up

You now know the basics of creating and authoring Quarto documents. The
following tutorials explore Quarto in more depth:

-   [Tutorial: Computations](../computations/) — Learn how to tailor the
    behavior and output of executable code blocks.

-   [Tutorial: Authoring](../authoring/) — Learn more about output
    formats and technical writing features like citations, crossrefs,
    and advanced layout.

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
