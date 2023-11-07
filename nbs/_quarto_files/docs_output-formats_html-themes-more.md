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

-   <a href="#bootswatch-sass-theme-files"
    id="toc-bootswatch-sass-theme-files" class="nav-link active"
    data-scroll-target="#bootswatch-sass-theme-files">Bootswatch Sass Theme
    Files</a>
-   <a href="#bootstrap-bootswatch-layering"
    id="toc-bootstrap-bootswatch-layering" class="nav-link"
    data-scroll-target="#bootstrap-bootswatch-layering">Bootstrap /
    Bootswatch Layering</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/output-formats/html-themes-more.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# More About Quarto Themes

As a part of Quarto, we’ve developed a simple single file format that
describes declarations, variables, and rules that should be layered into
Scss files when compiling them into css. The basic structure of a theme
file is:

-   A single text file that contains valid Scss

-   Special comments are used to denote regions of functions, defaults,
    mixins, and rules (region decorators).

-   At least one of these region decorators must be present in order for
    the theme file to be valid.

-   More than one of each type of region decorator are permitted. If
    more than one of any type is present, all regions of a given type
    will be merged into a single block of that type in the order in
    which they are encountered in the file.

-   When compiling, the sections will be layered according to type,
    functions first, then variables, then mixins, then rules.

-   The directory that contains your theme file will be added to the
    load path, allowing `@use` or `@import` statements to be resolved
    using the same directory that contains the theme file.

Here is an example file:

    /*-- scss:functions --*/
    @function colorToRGB ($color) {
      @return "rgb(" + red($color) + ", " + green($color) + ", " + blue($color)+ ")";
    }

    /*-- scss:defaults --*/
    $h2-font-size:          1.6rem !default;
    $headings-font-weight:  500 !default;
    $body-color:            $gray-700 !default;

    /*-- scss:rules --*/
    h1, h2, h3, h4, h5, h6 {
      text-shadow: -1px -1px 0 rgba(0, 0, 0, .3);
    }

## Bootswatch Sass Theme Files

We’ve merged Bootswatch themes for Bootstrap 5 into this single file
theme format in our repo here:

<https://github.com/quarto-dev/quarto-cli/tree/main/src/resources/formats/html/bootstrap/themes>

From time to time, as the Bootswatch themes are updated, we will update
these merged theme files.

## Bootstrap / Bootswatch Layering

When using the Quarto HTML format, we allow the user to specify theme
information in the document front matter (or project YAML). The theme
information consists of a list of one or more of

-   A valid built in Bootswatch theme name

-   A theme file (valid as described above).

For example the following would use the cosmo Bootswatch theme and
provide customization using the custom.scss file:

    theme:
      - cosmo
      - custom.scss

When compiling the CSS for a Quarto website or HTML page, we merge any
user provided theme file(s) or Bootswatch themes with the Bootstrap Scss
in the following layers:

    Uses
        Bootstrap
        Theme(s)       /*-- scss:uses --*/
        
    Functions
        Bootstrap
        Theme(s)       /*-- scss:functions --*/

    Variables
        Themes(s)      /*-- scss:defaults --*/
        Bootstrap
        
    Mixins                 
        Bootstrap
        Theme(s)       /* -- scss:mixins --*/

    Rules
        Bootstrap
        Theme(s)       /*-- scss:rules --*/

We order the themes according to the order that they are specified in
the YAML, maintaining the order for declarations and rules and reversing
the order for variables (allowing the files specified later in the list
to provide defaults variable values to the files specified earlier in
the list). Layering of the example themes above would be as follows:

    Uses
        Bootstrap
        cosmo           /*-- scss:uses --*/
        custom.scss     /*-- scss:uses --*/

    Functions
        Bootstrap
        cosmo           /*-- scss:functions --*/
        custom.scss     /*-- scss:functions --*/

    Variables
        custom.scss     /*-- scss:defaults --*/
        cosmo           /*-- scss:defaults --*/
        Bootstrap

    Mixins
        Bootstrap
        cosmo            /* -- scss:mixins --*/
        custom.scss      /* -- scss:mixins --*/

    Rules
        Bootstrap
        cosmo           /*-- scss:rules --*/
        custom.scss     /*-- scss:rules --*/

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
