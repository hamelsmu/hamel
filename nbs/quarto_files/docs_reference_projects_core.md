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

-   <a href="#preview" id="toc-preview" class="nav-link active"
    data-scroll-target="#preview">Preview</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/reference/projects/core.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Project Options

This article documents options that define the type, render targets, and
output of a project.

See the [Project Basics](../../../docs/projects/quarto-projects.html)
article for additional documentation on using projects.

Project options are specified under the `project` key. For example:

    ---
    project:
      type: website
      output-dir: _site
    ---

<table class="table">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd odd">
<td style="text-align: left;"><code>title</code></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even even">
<td style="text-align: left;"><code>type</code></td>
<td style="text-align: left;"><p>Project type (<code>default</code>,
<code>website</code>, or <code>book</code>)</p></td>
</tr>
<tr class="odd odd">
<td style="text-align: left;"><code>render</code></td>
<td style="text-align: left;"><p>Files to render (defaults to all
files)</p></td>
</tr>
<tr class="even even">
<td style="text-align: left;"><code>execute-dir</code></td>
<td style="text-align: left;"><p>Control the working directory for
computations.</p>
<ul>
<li><code>file</code>: Use the directory of the file that is currently
executing.</li>
<li><code>project</code>: Use the root directory of the project.</li>
</ul></td>
</tr>
<tr class="odd odd">
<td style="text-align: left;"><code>output-dir</code></td>
<td style="text-align: left;"><p>Output directory</p></td>
</tr>
<tr class="even even">
<td style="text-align: left;"><code>lib-dir</code></td>
<td style="text-align: left;"><p>HTML library (JS/CSS/etc.)
directory</p></td>
</tr>
<tr class="odd odd">
<td style="text-align: left;"><code>resources</code></td>
<td style="text-align: left;"><p>Additional file resources to be copied
to output directory</p></td>
</tr>
<tr class="even even">
<td style="text-align: left;"><code>preview</code></td>
<td style="text-align: left;"><p>Options for <code>quarto preview</code>
(see <a href="#preview">Preview</a>)</p></td>
</tr>
<tr class="odd odd">
<td style="text-align: left;"><code>pre-render</code></td>
<td style="text-align: left;"><p>Scripts to run as a pre-render
step</p></td>
</tr>
<tr class="even even">
<td style="text-align: left;"><code>post-render</code></td>
<td style="text-align: left;"><p>Scripts to run as a post-render
step</p></td>
</tr>
</tbody>
</table>

### Preview

Specify options that control the behavior of `quarto preview` within the
`preview` key. For example:

    ---
    project:
      type: website
      output-dir: _site
      preview:
        port: 4200
        browser: false
    ---

Available `preview` options include:

<table class="table">
<tbody>
<tr class="odd odd">
<td style="text-align: left;"><code>port</code></td>
<td style="text-align: left;"><p>Port to listen on (defaults to random
value between 3000 and 8000)</p></td>
</tr>
<tr class="even even">
<td style="text-align: left;"><code>host</code></td>
<td style="text-align: left;"><p>Hostname to bind to (defaults to
127.0.0.1)</p></td>
</tr>
<tr class="odd odd">
<td style="text-align: left;"><code>serve</code></td>
<td style="text-align: left;"><p>Options for external preview server
(see <a href="#serve">Serve</a>)</p></td>
</tr>
<tr class="even even">
<td style="text-align: left;"><code>browser</code></td>
<td style="text-align: left;"><p>Open a web browser to view the preview
(defaults to true)</p></td>
</tr>
<tr class="odd odd">
<td style="text-align: left;"><code>watch-inputs</code></td>
<td style="text-align: left;"><p>Re-render input files when they change
(defaults to true)</p></td>
</tr>
<tr class="even even">
<td style="text-align: left;"><code>navigate</code></td>
<td style="text-align: left;"><p>Navigate the browser automatically when
outputs are updated (defaults to true)</p></td>
</tr>
<tr class="odd odd">
<td style="text-align: left;"><code>timeout</code></td>
<td style="text-align: left;"><p>Time (in seconds) after which to exit
if there are no active clients</p></td>
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
