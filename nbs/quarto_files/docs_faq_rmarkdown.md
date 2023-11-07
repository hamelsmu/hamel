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

# FAQ for R Markdown Users

Answers to R Markdown users’ most frequently asked questions about
Quarto.

## On this page

-   <a href="#what-can-i-use-quarto-for"
    id="toc-what-can-i-use-quarto-for">What can I use Quarto for?</a>
-   <a
    href="#quarto-sounds-similar-to-r-markdown.-what-is-the-difference-and-why-create-a-new-project"
    id="toc-quarto-sounds-similar-to-r-markdown.-what-is-the-difference-and-why-create-a-new-project">Quarto
    sounds similar to R Markdown. What is the difference and why create a
    new project?</a>
-   <a
    href="#is-r-markdown-going-away-will-my-r-markdown-documents-continue-to-work"
    id="toc-is-r-markdown-going-away-will-my-r-markdown-documents-continue-to-work">Is
    R Markdown going away? Will my R Markdown documents continue to
    work?</a>
-   <a href="#should-i-switch-from-r-markdown-to-quarto"
    id="toc-should-i-switch-from-r-markdown-to-quarto">Should I switch from
    R Markdown to Quarto?</a>
-   <a href="#i-use-x-bookdown-blogdown-etc..-what-is-the-quarto-equivalent"
    id="toc-i-use-x-bookdown-blogdown-etc..-what-is-the-quarto-equivalent">I
    use X (bookdown, blogdown, etc.). What is the Quarto equivalent?</a>
-   <a
    href="#can-you-create-custom-formats-for-quarto-like-you-can-for-r-markdown"
    id="toc-can-you-create-custom-formats-for-quarto-like-you-can-for-r-markdown">Can
    you create custom formats for Quarto like you can for R Markdown?</a>
-   <a
    href="#when-would-be-a-good-time-to-start-new-projects-in-quarto-rather-than-r-markdown"
    id="toc-when-would-be-a-good-time-to-start-new-projects-in-quarto-rather-than-r-markdown">When
    would be a good time to start new projects in Quarto rather than R
    Markdown?</a>
-   <a href="#does-the-rstudio-ide-support-quarto"
    id="toc-does-the-rstudio-ide-support-quarto">Does the RStudio IDE
    support Quarto?</a>
-   <a href="#does-posit-connect-support-quarto"
    id="toc-does-posit-connect-support-quarto">Does Posit Connect support
    Quarto?</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/faq/rmarkdown.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

### What can I use Quarto for?

Quarto® is an open-source scientific and technical publishing system
built on Pandoc. You can weave together narrative text and code to
produce elegantly formatted output as documents, web pages, blog posts,
books and more. 

### Quarto sounds similar to R Markdown. What is the difference and why create a new project?

At its core, Quarto works the same way as R Markdown: 

<img
src="../../docs/get-started/hello/images/rstudio-qmd-how-it-works.png"
class="preview-image img-fluid"
alt="How Quarto works: qmd to knitr to md to pandoc to multiple formats including pdf, HTML and Microsoft Word" />

The goal of Quarto is to make the process of creating and collaborating
on scientific and technical documents dramatically better. Quarto
combines the functionality of R Markdown, bookdown, distill, xaringian,
etc into a single consistent system with “batteries included” that
reflects everything we’ve learned from R Markdown over the past 10
years.

The number of languages and runtimes used for scientific discourse is
very broad (and the Jupyter ecosystem in particular is extraordinarily
popular). Quarto is at its core multi-language and multi-engine
(supporting Knitr, Jupyter, and Observable today and potentially other
engines tomorrow).

On the other hand, R Markdown is fundamentally tied to R which severely
limits the number of practitioners it can benefit. Quarto is Posit’s
attempt to bring R Markdown to everyone! Unlike R Markdown, Quarto
doesn’t have a dependency or requirement for R. Quarto was developed to
be multilingual, beginning with R, Python, Javascript, and Julia, with
the idea that it will work even for languages that don’t yet exist.

While it is a “new” system, it should also be noted that it is highly
compatible with existing content: you can render most R Markdown
documents and Jupyter notebooks unmodified with Quarto. The concept is
to make a major, long term investment in reproducible research, while
keeping it compatible with existing formats and adaptable to the various
environments users work in.

### Is R Markdown going away? Will my R Markdown documents continue to work?

R Markdown is not going away! R Markdown is used extensively and
continues to work well. It will continue to be actively supported. We’re
not leaving R Markdown, we’re expanding our scope. Over the years there
have been many feature requests, and rather than implementing them all
in R Markdown, for certain features we may refer you to Quarto.
Everything that is currently in R Markdown will continue to work and be
supported. There are no plans for deprecation.

Read more about this in Yihui Xie’s blog post [With Quarto Coming, is R
Markdown Going Away?
No.](https://yihui.org/en/2022/04/quarto-r-markdown/)

### Should I switch from R Markdown to Quarto?

If you like using R Markdown, there’s no need to switch! R Markdown will
continue to be supported and work as it always has been. You’re welcome
to try Quarto if you like, but there’s no need to switch. Some new
features may only exist in Quarto, so if you want to use those, then
that’s where you would give those a try.  

We should emphasize that switching is not imperative. While we don’t
plan on major feature initiatives in R Markdown and related packages, we
are going to continue to maintain them (smaller improvements and bug
fixes) for a long time to come. Furthermore, since Rmd files can in most
cases be rendered without modification by Quarto, you can continue using
R Markdown and the switching cost will still be minimal whenever you
decide to do it. 

### I use X (bookdown, blogdown, etc.). What is the Quarto equivalent?

Here are the Quarto equivalents for various packages and features of the
R Markdown ecosystem (in some cases Quarto equivalents are not yet
available but will be later this year):

<table class="table">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header header">
<th>Feature</th>
<th>R Markdown</th>
<th>Quarto</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td>Basic Formats</td>
<td><ul>
<li><a
href="https://pkgs.rstudio.com/rmarkdown/reference/html_document.html">html_document</a></li>
<li><a
href="https://pkgs.rstudio.com/rmarkdown/reference/pdf_document.html">pdf_document</a></li>
<li><a
href="https://pkgs.rstudio.com/rmarkdown/reference/word_document.html">word_document</a></li>
</ul></td>
<td><ul>
<li><a
href="https://quarto.org/docs/output-formats/html-basics.html">html</a></li>
<li><a
href="https://quarto.org/docs/output-formats/pdf-basics.html">pdf</a></li>
<li><a
href="https://quarto.org/docs/output-formats/ms-word.html">docx</a></li>
</ul></td>
</tr>
<tr class="even even">
<td>Beamer</td>
<td><ul>
<li><a
href="https://pkgs.rstudio.com/rmarkdown/reference/beamer_presentation.html">beamer_presentation</a></li>
</ul></td>
<td><ul>
<li><a
href="https://quarto.org/docs/presentations/beamer.html">beamer</a></li>
</ul></td>
</tr>
<tr class="odd odd">
<td>PowerPoint</td>
<td><ul>
<li><a
href="https://pkgs.rstudio.com/rmarkdown/reference/powerpoint_presentation.html">powerpoint_presentation</a></li>
</ul></td>
<td><ul>
<li><a
href="https://quarto.org/docs/presentations/powerpoint.html">pptx</a></li>
</ul></td>
</tr>
<tr class="even even">
<td>HTML Slides</td>
<td><ul>
<li><a
href="https://bookdown.org/yihui/rmarkdown/xaringan.html">xaringan</a></li>
<li><a
href="https://bookdown.org/yihui/rmarkdown/ioslides-presentation.html">ioslides</a></li>
<li><a
href="https://bookdown.org/yihui/rmarkdown/revealjs.html">revealjs</a></li>
</ul></td>
<td><ul>
<li><a
href="https://quarto.org/docs/presentations/revealjs/">revealjs</a></li>
</ul></td>
</tr>
<tr class="odd odd">
<td>Advanced Layout</td>
<td><ul>
<li><a
href="https://bookdown.org/yihui/rmarkdown/tufte-handouts.html">tufte</a></li>
<li><a
href="https://rstudio.github.io/distill/figures.html">distill</a></li>
</ul></td>
<td><ul>
<li><a
href="https://quarto.org/docs/authoring/article-layout.html">Quarto
Article Layout</a></li>
</ul></td>
</tr>
<tr class="even even">
<td>Cross References</td>
<td><ul>
<li><a
href="https://bookdown.org/yihui/bookdown/a-single-document.html">html_document2</a></li>
<li><a
href="https://bookdown.org/yihui/bookdown/a-single-document.html">pdf_document2</a></li>
<li><a
href="https://bookdown.org/yihui/bookdown/a-single-document.html">word_document2</a></li>
</ul></td>
<td><ul>
<li><a
href="https://quarto.org/docs/authoring/cross-references.html">Quarto
Crossrefs</a></li>
</ul></td>
</tr>
<tr class="odd odd">
<td>Websites &amp; Blogs</td>
<td><ul>
<li><a href="https://pkgs.rstudio.com/blogdown/">blogdown</a></li>
<li><a href="https://pkgs.rstudio.com/distill/">distill</a></li>
</ul></td>
<td><ul>
<li><a href="https://quarto.org/docs/websites/">Quarto Websites</a></li>
<li><a href="https://quarto.org/docs/websites/website-blog.html">Quarto
Blogs</a></li>
</ul></td>
</tr>
<tr class="even even">
<td>Books</td>
<td><ul>
<li><a href="https://pkgs.rstudio.com/bookdown/">bookdown</a></li>
</ul></td>
<td><ul>
<li><a href="https://quarto.org/docs/books/">Quarto Books</a></li>
</ul></td>
</tr>
<tr class="odd odd">
<td>Interactivity</td>
<td><a
href="https://bookdown.org/yihui/rmarkdown/shiny-documents.html">Shiny
Documents</a></td>
<td><a href="https://quarto.org/docs/interactive/shiny/">Quarto
Interactive Documents</a></td>
</tr>
<tr class="even even">
<td>Journal Articles</td>
<td><a href="https://pkgs.rstudio.com/rticles/">rticles</a></td>
<td><a href="https://quarto.org/docs/journals/">Quarto Journal
Articles</a></td>
</tr>
<tr class="odd odd">
<td>Paged HTML</td>
<td><a href="https://github.com/rstudio/pagedown">pagedown</a></td>
<td>Planned</td>
</tr>
<tr class="even even">
<td>Dashboards</td>
<td><a
href="https://pkgs.rstudio.com/flexdashboard/">flexdashboard</a></td>
<td>Planned</td>
</tr>
<tr class="odd odd">
<td>Interactive Tutorials</td>
<td><a href="https://pkgs.rstudio.com/learnr/">learnr</a></td>
<td>No equivalent planned</td>
</tr>
</tbody>
</table>

### Can you create custom formats for Quarto like you can for R Markdown?

Quarto offers an [Extension](https://quarto.org/docs/extensions/)
mechanism to add features to a format using
[Shortcodes](https://quarto.org/docs/extensions/#using-shortcodes) or
[Filters](https://quarto.org/docs/extensions/#using-filters) but also
create [custom
formats](https://quarto.org/docs/extensions/formats.html). A major
difference with custom output format in R Markdown is that Quarto
Extension does not use R but Lua, for example if you need to add some
logic behind custom metadata fields. See [Developing with
Lua](https://quarto.org/docs/extensions/lua.html) to get started if you
need use it your extension. Some of the features from R Markdown custom
formats like customizing knitting behavior can also now be done in YAML
with [execution
options](https://quarto.org/docs/computations/execution-options.html#knitr-options).

As example of custom formats for Quarto, [Journal
Articles](https://quarto.org/docs/journals/) for Quarto are port of some
custom output format inside the **rticles** R package. Extensions lives
in [Quarto Journals](https://github.com/quarto-journals/) Github
organization, and you can find information on how to [customize
templates](https://quarto.org/docs/journals/templates.html) and [manage
Authors](https://quarto.org/docs/journals/authors.html) for you format.

If you are an advanced developer of R Markdown custom format, the
Extension mechanism may still have limitation (like pre and post
processor). The Extension feature in Quarto will be improved over time -
do not hesitate to share with us your use case or wished in our
[Discussion
Board](https://github.com/quarto-dev/quarto-cli/discussions).

### When would be a good time to start new projects in Quarto rather than R Markdown?

Quarto v1.0 was [announced at
rstudio::conf(2022)](https://www.rstudio.com/blog/announcing-quarto-a-new-scientific-and-technical-publishing-system/).
This is the first stable release which is already an excellent
foundation for starting new projects with Quarto or migrating existing R
Markdown projects ([if you are so
inclined](https://quarto.org/docs/faq/rmarkdown.html#is-r-markdown-going-away-will-my-r-markdown-documents-continue-to-work)).
If you start using Quarto, please do stay updated with [latest release
and changes](https://quarto.org/docs/download/) as development is very
active.

### Does the RStudio IDE support Quarto?

Yes! You need to use RStudio v2022.07 or a later version, which includes
support for [editing and preview of Quarto
documents](https://quarto.org/docs/tools/rstudio.html).

You can download the latest release (v2023.06) of RStudio v2023.06 from
<https://posit.co/download/rstudio-desktop/>.

### Does Posit Connect support Quarto?

Yes! You can publish Quarto content to Posit Connect v2021.08.0 or
later. Quarto has to be enabled as documented in the Posit Connect
[admin
guide](https://docs.rstudio.com/connect/admin/appendix/configuration/#Quarto).
Connect’s user
[documentation](https://docs.rstudio.com/connect/user/quarto/) refers to
[Quarto.org
docs](https://quarto.org/docs/websites/publishing-websites.html#rstudio-connect)
on how to publish from the RStudio IDE. To publish Python-based Quarto
content, you can use the [rsconnect-python
CLI](https://docs.rstudio.com/rsconnect-python/) from various locations,
including VSCode, JupyterLab or the terminal.

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
