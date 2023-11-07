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

-   <a href="#support-for-crossreferenceable-elements-in-filters"
    id="toc-support-for-crossreferenceable-elements-in-filters"
    class="nav-link active"
    data-scroll-target="#support-for-crossreferenceable-elements-in-filters">Support
    for crossreferenceable elements in filters</a>
    -   <a href="#the-floatreftarget-ast-node"
        id="toc-the-floatreftarget-ast-node" class="nav-link"
        data-scroll-target="#the-floatreftarget-ast-node">The
        <code>FloatRefTarget</code> AST node</a>
-   <a href="#custom-formats-and-custom-renderers"
    id="toc-custom-formats-and-custom-renderers" class="nav-link"
    data-scroll-target="#custom-formats-and-custom-renderers">Custom formats
    and Custom renderers</a>
-   <a href="#relative-paths-in-require-calls"
    id="toc-relative-paths-in-require-calls" class="nav-link"
    data-scroll-target="#relative-paths-in-require-calls">Relative paths in
    <code>require()</code> calls</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/prerelease/1.4/lua_changes.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Lua filter changes

Pre-release Feature

This feature is new in the upcoming Quarto 1.4 release. To use the
feature now, you’ll need to
[download](https://quarto.org/docs/download/prerelease) and install the
Quarto pre-release.

Quarto v1.4 includes the following new features for Lua filters:

## Support for crossreferenceable elements in filters

Quarto v1.4 brings significant changes to the handling of figures,
tables, listings, etc. These changes simplify the writing of Lua filters
that targets those elements, but will generally require changes in
existing.

### The `FloatRefTarget` AST node

In v1.4, crossreferenceable elements all have a single generic type,
`FloatRefTarget`. This element can be constructed explicitly in a Lua
filter. It can also be used as the element to be processed in a Lua
filter directly.

    -- A filter targeting FloatRefTarget nodes
    return {
      FloatRefTarget = function(float)
        if float.caption_long then
          float.caption_long.content:insert(pandoc.Str("[This will appear at the beginning of every caption]"))
          return float
        end
      end
    }

`FloatRefTarget` nodes have the following fields:

-   `type`: The type of element: `Figure`, `Table`, `Listing`, etc.
    Quarto v1.4 supports custom node types that can be declared at the
    document or project level.
-   `content`: The content of the Figure, Table, etc. Quarto v1.4
    accepts any content in any `FloatRefTarget` type (so if your tables
    are better displayed as an image, you can use that.).
-   `caption_long`: The caption that appears in the main body of the
    document
-   `caption_short`: The caption that appears in the element collations
    (such as a list of tables, list of figures, etc.)
-   `identifier`, `attributes`, `classes`: these are analogous to `Attr`
    fields in Pandoc AST elements like spans and divs. `identifier`, in
    addition, needs to be the string that is used in a crossref
    (`fig-cars`, `tbl-votes`, `lst-query`, and so on).
-   `parent_id`: if a `FloatRefTarget` is a subfloat of a parent
    multiple-element float, then `parent_id` will hold the identifier of
    the parent float.

## Custom formats and Custom renderers

Quarto v1.4 adds support for extensible renderers of quarto AST nodes
such as `FloatRefTarget`, `Callout`. In order to declare a custom
renderer, add the following to a Lua filter:

    local predicate = function(float)
      -- return true if this renderer should be used;
      -- typically, this will return true if the custom format is active.
    end
    local renderer = function(float)
      -- returns a plain Pandoc representation of the rendered figure.
    end
    quarto._quarto.ast.add_renderer(
      "FloatRefTarget", 
      predicate, 
      renderer)

## Relative paths in `require()` calls

In larger, more complex filters, it becomes useful to structure your Lua
code in modules. Quarto v1.4 supports the use of relative paths in
`require()` calls so that small modules can be easily created and
reused.

For example:

    filter.lua

    local utility = require('./utils')
    function Pandoc(doc)
      -- process 
    end

Using relative paths this way in quarto makes it harder for multiple
filters to accidentally create conflicting module names (as would
eventually happen when using the standard Lua `require('utils')`
syntax). It’s possible to refer to subdirectories and parent directories
as well:

    filter2.lua

    local parsing = require('./utils/parsing')
    function Pandoc(doc)
      -- process 
    end

    utils/parsing.lua

    local utils = require("../utils")
    -- ...

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
