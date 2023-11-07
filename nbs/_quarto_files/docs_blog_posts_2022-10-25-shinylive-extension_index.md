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

# Shinylive Extension

Embed Shinylive applications in Quarto documents

With Shinylive, you can embed Shiny for Python applications into Quarto
documents and run the entire application (including the Python runtime)
inside the user’s web browser.

Extensions

Features

Author

Winston Chang

Published

October 25, 2022

The new [Shinylive Quarto
extension](https://github.com/quarto-ext/shinylive) makes it easy to
embed Shiny for Python applications in your Quarto documents. This makes
it possible to add interactivity to your documents with just Python
code. For example, you can include an interactive Shiny application like
this, directly inside your Quarto document.

[<img src="shinylive-embedded-app.png"
class="preview-image img-fluid quarto-figure-center"
alt="Shinylive appplication embedded in a Quarto document." />](https://quarto-ext.github.io/shinylive/sine.html)

In case you’re not already familiar with Shiny, here’s some background:
[Shiny](https://shiny.rstudio.com/) is a framework for creating web
applications. Shiny was originally just for R, but we’ve recently
released an alpha version of [Shiny for
Python](https://shiny.rstudio.com/py/).

One of the exciting new features of Shiny for Python is a deployment
method called Shinylive: the application can be run entirely within the
browser, without needing a remote server running Python. Instead, Python
runs *in the web browser*, thanks to the magic of
[WebAssembly](https://webassembly.org/). In essence, but the server and
client sides of the Shiny application run in the browser.

The Shiny for Python [website](https://shiny.rstudio.com/py/) contains
many interactive, editable Shiny applications, and is built using this
extension.

Bear in mind that not all Shiny applications can be deployed with
Shinylive, in part because not all Python packages can run in
WebAssembly – but for those that can, this extension makes it possible
to deploy the Quarto document with the embedded application on any web
hosting service. To learn more about Shinylive, see [this
page](https://shiny.rstudio.com/py/docs/shinylive.html).

The new Shinylive Quarto extension makes it easy to embed Shiny for
Python applications in Quarto documents. This is a great way of adding
interactive components to your Quarto document. And, once again, you
don’t need a server running Python to share these Quarto documents –
just deploy the generated files as you would for any other Quarto
website.

Subscribe

<span style="font-size: 0.9em;">Enjoy this blog? Get notified of new
posts by email:</span>

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
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/blog/posts/2022-10-25-shinylive-extension/index.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
