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
-   <a href="#enabling-lightbox" id="toc-enabling-lightbox" class="nav-link"
    data-scroll-target="#enabling-lightbox">Enabling Lightbox</a>
    -   <a href="#applying-lightbox-to-specific-images"
        id="toc-applying-lightbox-to-specific-images" class="nav-link"
        data-scroll-target="#applying-lightbox-to-specific-images">Applying
        Lightbox to Specific Images</a>
-   <a href="#disabling-lightbox-treatment"
    id="toc-disabling-lightbox-treatment" class="nav-link"
    data-scroll-target="#disabling-lightbox-treatment">Disabling Lightbox
    Treatment</a>
    -   <a href="#disabling-lightbox-for-specific-images"
        id="toc-disabling-lightbox-for-specific-images" class="nav-link"
        data-scroll-target="#disabling-lightbox-for-specific-images">Disabling
        Lightbox for Specific Images</a>
-   <a href="#galleries" id="toc-galleries" class="nav-link"
    data-scroll-target="#galleries">Galleries</a>
-   <a href="#options" id="toc-options" class="nav-link"
    data-scroll-target="#options">Options</a>
-   <a href="#per-image-attributes" id="toc-per-image-attributes"
    class="nav-link" data-scroll-target="#per-image-attributes">Per Image
    Attributes</a>
-   <a href="#using-lightbox-with-computational-cells"
    id="toc-using-lightbox-with-computational-cells" class="nav-link"
    data-scroll-target="#using-lightbox-with-computational-cells">Using
    Lightbox with Computational Cells</a>
    -   <a href="#advanced-customization-in-computations"
        id="toc-advanced-customization-in-computations" class="nav-link"
        data-scroll-target="#advanced-customization-in-computations">Advanced
        Customization In Computations</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/prerelease/1.4/lightbox.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

# Lightbox Support

Pre-release Feature

This feature is new in the upcoming Quarto 1.4 release. To use the
feature now, you’ll need to
[download](https://quarto.org/docs/download/prerelease) and install the
Quarto pre-release.

## Overview

The new lightbox feature in Quarto uses the [GLightbox javascript
library](https://biati-digital.github.io/glightbox/) to add lightbox
styling and behavior to images in your HTML documents. For example, the
following document enables lightbox treatment for images in the
document:

    ---
    title: Simple Lightbox Example
    lightbox: true
    ---

    ![A Lovely Image](mv-1.jpg)

The viewer of the rendered HTML page for this document will be able to
click the image to zoom and see a larger version of the image (including
any caption).

## Enabling Lightbox

You can enable lightbox either for all images within a document, or for
only selected images within a document. To enable lightbox for all
images within a document, use the following yaml:

    ---
    lightbox: true
    ---

When lightbox is set to automatically select images, it will match any
image used as a figure or which appears as a block (by itself within a
paragraph). By default, images that appear inline with other content
will not receive lightbox treatment.

### Applying Lightbox to Specific Images

You can select specific images to receive the lightbox treatment by
applying the `lightbox` class on the images you’d like to receive the
treatment. In this case, there is no need to include `lightbox` in the
front matter, the use of the `lightbox` class will automatically enable
lightbox. For example:

    ---
    title: Simple Lightbox Example
    ---

    ![A Lovely Image](mv-1.jpg){.lightbox}

    ![Another Lovely Image](mv-2.jpg)

will result in the first image receiving a lightbox treatment, while the
second image will not.

## Disabling Lightbox Treatment

You can disable lightbox for the whole document using the following
yaml:

    ---
    lightbox: false
    ---

When lightbox is explicitly disabled, no images will receive the
lightbox treatment, even if the image is marked with a `lightbox` class
(as described above).

### Disabling Lightbox for Specific Images

If automatic lightboxing of images is enabled, you can select specific
images to not receive the treatment by marking them with a `no-lightbox`
class. For example:

    ---
    title: Simple Lightbox Example
    lightbox: auto
    ---

    ![A Lovely Image](mv-1.jpg)

    ![Another Lovely Image](mv-2.jpg){.no-lightbox}

In this example, the first image will receive the lightbox treatment,
while the second image will not.

## Galleries

In addition to simply providing a lightbox treatment for individual
images, you can also group images into a ‘gallery’. When the user
activates the lightbox, they will be able to page through the images in
the gallery without returning to the main document. To create galleries
of images, apply a `group` attribute (with a name) to the images that
you’d like to gather into a gallery. Images with the same group name
will be placed together in a gallery when given a lightbox treatment.

For example, the following three images will be treated as a gallery:

    ![A Lovely Image](mv-1.jpg){group="my-gallery"}

    ![Another Lovely Image](mv-2.jpg){group="my-gallery"}

    ![The Last Lovely Image](mv-3.jpg){group="my-gallery"}

## Options

Quarto supports a number of options to customize the ligthbox behavior
for a document. Options include:

<table class="table" style="width:99%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header header">
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td><code>match</code></td>
<td>Set this to <code>auto</code> if you’d like any image to be given
lightbox treatment. If you omit this, only images with the class
<code>lightbox</code> will be given the lightbox treatment.</td>
</tr>
<tr class="even even">
<td><code>effect</code></td>
<td>The effect that should be used when opening and closing the
lightbox. One of <code>fade</code>, <code>zoom</code>,
<code>none</code>. Defaults to <code>zoom</code>.</td>
</tr>
<tr class="odd odd">
<td><code>desc-position</code></td>
<td>The position of the title and description when displaying a
lightbox. One of <code>top</code>, <code>bottom</code>,
<code>left</code>, <code>right</code>. Defaults to
<code>bottom</code>.</td>
</tr>
<tr class="even even">
<td><code>loop</code></td>
<td>Whether galleries should ‘loop’ to first image in the gallery if the
user continues past the last image of the gallery. Boolean that defaults
to <code>true</code>.</td>
</tr>
<tr class="odd odd">
<td><code>css-class</code></td>
<td>A class name to apply to the lightbox to allow css targeting. This
will replace the lightbox class with your custom class name.</td>
</tr>
</tbody>
</table>

A complete example:

    ---
    title: Complete Lightbox Example
    filters:
      - lightbox
    lightbox:
      match: auto
      effect: fade
      desc-position: right
      loop: false
      css-class: "my-css-class"
    ---

## Per Image Attributes

The following options may be specified as attributes on individual
images to control the lightbox behavior:

<table class="table" style="width:99%;">
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header header">
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td><code>desc-position</code></td>
<td>The position of the title and description when displaying a
lightbox. One of <code>top</code>, <code>bottom</code>,
<code>left</code>, <code>right</code>. Defaults to
<code>bottom</code></td>
</tr>
</tbody>
</table>

## Using Lightbox with Computational Cells

The Quarto lightbox treatment will use figure information for
computational outputs. For example, the following plot will receive a
lightbox treatment and will include a properly prefixed caption when the
user zooms into the plot.

    ---
    lightbox: auto
    ---

    ```{r}
    #| label: fig-basic
    #| fig-cap: Simple demo R plot 
    plot(1:10, rnorm(10))
    ```

If your computational cell produces multiple subfigures, each of the
subfigures will receive the lightbox treatment and when zoom, the user
may page back and forth through the subfigures. For example, the
following will produce a ‘gallery’ lightbox view which includes both of
the subfigures, allowing the viewer to easily navigate between sub
figures:

    ```{r}
    #| label: fig-plots
    #| fig-cap: |
    #|   The below demonstrates placing more than one image in a gallery. Note
    #|   the usage of the `layout-ncol` which arranges the images on the page
    #|   side by date. Adding the `group` attribute to the markdown images places
    #|   the images in a gallery grouped together based upon the group name
    #|   provided.
    #| fig-subcap:
    #|   - "This is a caption for the first sub figure"
    #|   - "This is a caption for the second sub figure"
    #| layout-ncol: 2
    plot(ToothGrowth)
    plot(PlantGrowth)
    ```

### Advanced Customization In Computations

Options for lightbox can be passed using the code cell option `lightbox`
like the following:

    ```{r}
    #| fig-cap: Simple demo R plot 
    #| lightbox:
    #|   group: r-graph
    #|   description: This is 1 to 10 plot
    plot(1:10, rnorm(10))
    ```

It is possible to create several plots, and group them in a lightbox
gallery. Use list in YAML for options when you have several plots, on
per plot.

    ```{r}
    #| fig-cap: 
    #|   - Caption for first plot
    #|   - Caption for second plot
    #| lightbox: 
    #|   group: cars
    #|   description: 
    #|     - This is the decription for first graph
    #|     - This is the decription for second graph
    plot(mtcars)
    plot(cars)
    ```

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
