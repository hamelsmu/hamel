<a href="./index.html" class="navbar-brand navbar-brand-logo"><img
src="./quarto.png" class="navbar-logo" alt="Quarto logo." /></a>

<span class="navbar-toggler-icon"></span>

-   <a href="./index.html" class="nav-link active" aria-current="page"><span
    class="menu-text">Overview</span></a>
-   <a href="./docs/get-started/index.html" class="nav-link"><span
    class="menu-text">Get Started</span></a>
-   <a href="./docs/guide/index.html" class="nav-link"><span
    class="menu-text">Guide</span></a>
-   <a href="./docs/extensions/index.html" class="nav-link"><span
    class="menu-text">Extensions</span></a>
-   <a href="./docs/reference/index.html" class="nav-link"><span
    class="menu-text">Reference</span></a>
-   <a href="./docs/gallery/index.html" class="nav-link"><span
    class="menu-text">Gallery</span></a>
-   <a href="./docs/blog/index.html" class="nav-link"><span
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
    -   <a href="./docs/faq/index.html" class="dropdown-item"><em></em> <span
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

# Welcome to Quarto<sup><span class="trademark">®</span></sup>

### An open-source scientific and technical publishing system

-   Author using [Jupyter](https://jupyter.org) notebooks or with plain
    text markdown in your favorite editor.
-   Create dynamic content with
    [Python](./docs/computations/python.html),
    [R](./docs/computations/r.html),
    [Julia](./docs/computations/julia.html), and
    [Observable](./docs/computations/ojs.html).
-   Publish reproducible, production quality articles, presentations,
    dashboards, websites, blogs, and books in HTML, PDF, MS Word, ePub,
    and more.
-   Share knowledge and insights organization-wide by publishing to
    [Posit
    Connect](https://quarto.org/docs/publishing/rstudio-connect.html),
    [Confluence](./docs/publishing/confluence.html), or other publishing
    systems.
-   Write using [Pandoc](https://pandoc.org) markdown, including
    equations, citations, crossrefs, figure panels, callouts, advanced
    layout, and more.

### Analyze. Share. Reproduce. You have a story to tell with data—tell it with Quarto.

<a href="docs/get-started/"
class="btn-action-primary btn-action btn btn-success btn-lg"
role="button">Get Started</a> <a href="docs/guide/" id="btn-guide"
class="btn-action btn btn-info btn-lg" role="button">Guide</a>

# Hello, Quarto

-   Python
-   R
-   Julia
-   Observable

Combine Jupyter notebooks with flexible options to produce production
quality output in a wide variety of formats. Author using traditional
notebook UIs or with a plain text markdown representation of notebooks.

<img src="images/demo-jupyter-plain.png" class="hello-output"
height="605"
alt="Example Jupyter notebook entitled Palmer Penguins with code cells, text, and a scatterplot." />

<img src="images/demo-jupyter-output.png" class="img-fluid"
alt="Output of example Jupyter notebook, Palmer Penguins, in HTML showing title, metadata, text, code, and scatterplot. At the top there is a dropdown option to show or hide the code." />

Quarto is a multi-language, next generation version of R Markdown from
Posit, with many new new features and capabilities. Like R Markdown,
Quarto uses [knitr](https://yihui.org/knitr/) to execute R code, and is
therefore able to render most existing Rmd files without modification.

    ---
    title: "ggplot2 demo"
    author: "Norah Jones"
    date: "5/22/2021"
    format: 
      html:
        fig-width: 8
        fig-height: 4
        code-fold: true
    ---

    ## Air Quality

    @fig-airquality further explores the impact of temperature on ozone level.

    ```{r}
    #| label: fig-airquality
    #| fig-cap: "Temperature and ozone level."
    #| warning: false

    library(ggplot2)
    ggplot(airquality, aes(Temp, Ozone)) + 
      geom_point() + 
      geom_smooth(method = "loess")
    ```

<img src="images/hello-knitr.png" class="hello-output img-fluid"
alt="Example output with title (ggplot2 demo), author (Norah Jones), and date (5/22/2021). Below is a header reading Air Quality followed by body text (Figure 1 further explores the impact of temperature on ozone level.) with a toggleable code field, and figure with caption Figure 1 Temperature and ozone level." />

Combine markdown and Julia code to create dynamic documents that are
fully reproducible. Quarto executes Julia code via the
[IJulia](https://github.com/JuliaLang/IJulia.jl) Jupyter kernel,
enabling you to author in plain text (as shown below) or render existing
Jupyter notebooks.

    ---
    title: "Plots Demo"
    author: "Norah Jones"
    date: "5/22/2021"
    format:
      html:
        code-fold: true
    jupyter: julia-1.8
    ---

    ## Parametric Plots

    Plot function pair (x(u), y(u)). 
    See @fig-parametric for an example.

    ```{julia}
    #| label: fig-parametric
    #| fig-cap: "Parametric Plots"

    using Plots

    plot(sin, 
         x->sin(2x), 
         0, 
         2π, 
         leg=false, 
         fill=(0,:lavender))
    ```

<img src="images/hello-julia.png" class="hello-output img-fluid"
alt="Example Plots Demo output with title, author, date published and main section on Parametric plots which contains text, a toggleable code field, and the output of the plot, with the caption Figure 1 Parametric Plots." />

Quarto includes native support for Observable JS, a set of JavaScript
enhancements created by Mike Bostock (the author of D3). Observable JS
uses a reactive execution model, and is especially well suited for
interactive data exploration and analysis.

    ---
    title: "observable plot"
    author: "Norah Jones"
    format: 
      html: 
        code-fold: true
    ---

    ## Seattle Precipitation by Day (2012 to 2016)

    ```{ojs}
    data = FileAttachment("seattle-weather.csv")
      .csv({typed: true})
      
    Plot.plot({
      width: 800, height: 500, padding: 0,
      color: { scheme: "blues", type: "sqrt"},
      y: { tickFormat: i => "JFMAMJJASOND"[i] },
      marks: [
        Plot.cell(data, Plot.group({fill: "mean"}, {
          x: d => new Date(d.date).getDate(),
          y: d => new Date(d.date).getMonth(),
          fill: "precipitation", 
          inset: 0.5
        }))
      ]
    })
    ```

<img src="images/hello-observable.png" class="img-fluid"
style="background-color: white; border: 1px solid #dee2e6; height: 625px;"
alt="Example output with title, author, and date. Below, the main section reads Seattle Precipitation by Day (2012 to 2016) with a toggleable section to show code and a heatmap of the precipitation by day." />

### Dynamic Documents

Generate dynamic output using Python, R, Julia, and Observable. Create
reproducible documents that can be regenerated when underlying
assumptions or data change.

[Learn more »](./docs/computations/python.html)

### Beautiful Publications

Publish high-quality articles, reports, presentations, websites, and
books in HTML, PDF, MS Word, ePub, and more. Use a single source
document to target multiple formats.

[Learn more »](./docs/output-formats/all-formats.html)

### Scientific Markdown

Pandoc markdown has excellent support for LaTeX equations and citations.
Quarto adds extensions for cross-references, figure panels, callouts,
advanced page layout, and more.

[Learn more »](./docs/authoring/markdown-basics.html)

### Authoring Tools

Use your favorite tools including VS Code, RStudio, Jupyter Lab, or any
text editor. Use the Quarto visual markdown editor for long-form
documents.

[Learn more »](./docs/tools/jupyter-lab.html)

### Interactivity

Engage readers by adding interactive data exploration to your documents
using Jupyter Widgets, htmlwidgets for R, Observable JS, and Shiny.

[Learn more »](docs/interactive/)

### Websites and Books

Publish collections of documents as a blog or full website. Create books
and manuscripts in both print formats (PDF and MS Word) and online
formats (HTML and ePub).

[Learn more »](docs/websites/)

<a href="docs/get-started/index.html"
class="btn-action-primary btn-action btn btn-success btn-lg"
role="button" style="margin-top: 1em;">Get Started</a>

Proudly supported by [<img
src="https://www.rstudio.com/assets/img/posit-logo-fullcolor-TM.svg"
class="img-fluid" width="65" alt="Posit" />](https://posit.co)

-   <a href="./about.html" class="nav-link"></a>

    About

-   <a href="./docs/faq/index.html" class="nav-link"></a>

    FAQ

-   <a href="./license.html" class="nav-link"></a>

    License

-   <a href="./trademark.html" class="nav-link"></a>

    Trademark

-   <a href="https://github.com/quarto-dev/quarto-web/edit/main/index.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
