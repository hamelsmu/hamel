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

1.  [Highlights](../../../../docs/prerelease/1.3/index.html)
2.  [Quarto AST](../../../../docs/prerelease/1.3/ast.html)
3.  [Conditional
    Blocks](../../../../docs/prerelease/1.3/custom-ast-nodes/conditional-block.html)

<span class="flex-grow-1" role="button" bs-toggle="collapse"
bs-target=".quarto-sidebar-collapse-item" aria-controls="quarto-sidebar"
aria-expanded="false" aria-label="Toggle sidebar navigation"
onclick="if (window.quartoToggleHeadroom) { window.quartoToggleHeadroom(); }"></span>

-   <a href="../../../../docs/prerelease/1.3/index.html"
    class="sidebar-item-text sidebar-link"><span
    class="menu-text">Highlights</span></a> <span
    class="sidebar-item-toggle text-start" bs-toggle="collapse"
    bs-target="#quarto-sidebar-section-1" aria-expanded="true"
    aria-label="Toggle section"></span>

    -   <a href="../../../../docs/publishing/confluence.html"
        class="sidebar-item-text sidebar-link"><span
        class="menu-text">Confluence Publishing</span></a>

    -   <a href="../../../../docs/output-formats/html-multi-format.html"
        class="sidebar-item-text sidebar-link"><span
        class="menu-text">Multi-Format</span></a>

    -   <a href="../../../../docs/authoring/notebook-embed.html"
        class="sidebar-item-text sidebar-link"><span class="menu-text">Cell
        Embedding</span></a>

    -   <a
        href="../../../../docs/output-formats/page-layout.html#grid-customization"
        class="sidebar-item-text sidebar-link"><span class="menu-text">Grid
        Customization</span></a>

    -   <a href="../../../../docs/authoring/code-annotation.html"
        class="sidebar-item-text sidebar-link"><span class="menu-text">Code
        Annotation</span></a>

    -   <a href="../../../../docs/prerelease/1.3/ast.html"
        class="sidebar-item-text sidebar-link"><span class="menu-text">Quarto
        AST</span></a> <span class="sidebar-item-toggle text-start"
        bs-toggle="collapse" bs-target="#quarto-sidebar-section-2"
        aria-expanded="true" aria-label="Toggle section"></span>

        -   <a href="../../../../docs/prerelease/1.3/custom-ast-nodes/callout.html"
            class="sidebar-item-text sidebar-link"><span
            class="menu-text">Callouts</span></a>

        -   <a href="../../../../docs/prerelease/1.3/custom-ast-nodes/tabset.html"
            class="sidebar-item-text sidebar-link"><span
            class="menu-text">Tabsets</span></a>

        -   <a
            href="../../../../docs/prerelease/1.3/custom-ast-nodes/conditional-block.html"
            class="sidebar-item-text sidebar-link active"><span
            class="menu-text">Conditional Blocks</span></a>

    -   <a href="../../../../docs/authoring/diagrams.html#mermaid-theming"
        class="sidebar-item-text sidebar-link"><span class="menu-text">Mermaid
        Theming</span></a>

    -   <a href="../../../../docs/prerelease/1.3/pdf.html"
        class="sidebar-item-text sidebar-link"><span class="menu-text">PDF
        Images</span></a>

    -   <a
        href="../../../../docs/authoring/markdown-basics.html#keyboard-shortcuts"
        class="sidebar-item-text sidebar-link"><span
        class="menu-text"><code>kbd</code> Shortcode</span></a>

1.  [Highlights](../../../../docs/prerelease/1.3/index.html)
2.  [Quarto AST](../../../../docs/prerelease/1.3/ast.html)
3.  [Conditional
    Blocks](../../../../docs/prerelease/1.3/custom-ast-nodes/conditional-block.html)

# Quarto Conditional Blocks Custom Node API

Published

November 7, 2023

In Quarto 1.3, conditional blocks are represented as a custom AST node.
You can create conditional block AST nodes in Lua filters with the
`quarto.ConditionalBlock` constructor. The constructor takes a single
parameter, a table with entries `node`, `behavior`, and `condition`, as
described below. In Lua filters, conditional blocks are represented as a
table with the following fields:

-   `node`: the div containing the content
-   `behavior`: either `content-visible` or `content-hidden`
-   `condition`: a list of 2-element lists, such as
    `{ { "unless-format", "html" } }` (optional in the constructor,
    default value `{}`). The first element of each sublist must be one
    of `when-format`, `unless-format`, `when-profile`, and
    `unless-profile`. The second element is the relevant format or
    profile.

<a href="../../../../docs/prerelease/1.3/custom-ast-nodes/tabset.html"
class="pagination-link aria-label=" data-tabsets"=""><em></em> <span
class="nav-page-text">Tabsets</span></a>

<a href="../../../../docs/authoring/diagrams.html#mermaid-theming"
class="pagination-link" aria-label="Mermaid Theming"><span
class="nav-page-text">Mermaid Theming</span> <em></em></a>

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
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/prerelease/1.3/custom-ast-nodes/conditional-block.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
