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

# Palmer Penguins

    import pandas as pd
    import altair as alt
    import seaborn as sns
    from matplotlib import pyplot as plt

Data from [Palmer Penguins R
package](https://allisonhorst.github.io/palmerpenguins/)

    penguins = pd.read_csv("https://pos.it/palmer-penguins-github-csv")

    penguins.groupby("species").size().reset_index(name = "count")

<table class="dataframe table table-sm table-striped small"
data-quarto-postprocess="true" data-border="1">
<thead>
<tr class="header header">
<th data-quarto-table-cell-role="th"></th>
<th data-quarto-table-cell-role="th">species</th>
<th data-quarto-table-cell-role="th">count</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td data-quarto-table-cell-role="th">0</td>
<td>Adelie</td>
<td>152</td>
</tr>
<tr class="even even">
<td data-quarto-table-cell-role="th">1</td>
<td>Chinstrap</td>
<td>68</td>
</tr>
<tr class="odd odd">
<td data-quarto-table-cell-role="th">2</td>
<td>Gentoo</td>
<td>124</td>
</tr>
</tbody>
</table>

    colors = ["#FF8C00", "#A020F0", "#008B8B"]
    sns.set_palette(colors, n_colors = 3)

    penguins["bill_ratio"] = (
       penguins["bill_length_mm"] / penguins["bill_depth_mm"] 
    )
    sns.displot(penguins, 
                x = "bill_ratio", 
                hue = "species", 
                kind = "kde", fill = True, aspect = 2, height = 3)
    plt.show()

<img src="penguins_files/figure-html/cell-6-output-1.png"
class="img-fluid" alt="A density plot of bill ratio by species." />

    sns.displot(penguins, 
                x = "bill_depth_mm", 
                hue = "species", 
                kind = "kde", fill = True, 
                aspect = 2, height = 3)
    plt.show()
    sns.displot(penguins, 
                x = "bill_length_mm", 
                hue = "species", 
                kind = "kde", fill = True, 
                aspect = 2, height = 3)
    plt.show()

<figure>
<img src="penguins_files/figure-html/fig-bill-marginal-output-1.png"
class="img-fluid figure-img" data-ref-parent="fig-bill-marginal"
alt="(a) Gentoo penguins tend to have thinner bills," />
<figcaption aria-hidden="true">(a) Gentoo penguins tend to have thinner
bills,</figcaption>
</figure>

<figure>
<img src="penguins_files/figure-html/fig-bill-marginal-output-2.png"
class="img-fluid figure-img" data-ref-parent="fig-bill-marginal"
alt="(b) and Adelie penguins tend to have shorter bills." />
<figcaption aria-hidden="true">(b) and Adelie penguins tend to have
shorter bills.</figcaption>
</figure>

Figure 1: Marginal distributions of bill dimensions

    scale = alt.Scale(domain = ['Adelie', 'Chinstrap', 'Gentoo'],
                      range = colors)

    alt.Chart(penguins).mark_circle(size=60).encode(
        alt.X('bill_length_mm',
            scale=alt.Scale(zero=False)
        ),
        alt.Y('bill_depth_mm',
            scale=alt.Scale(zero=False)
        ),
        color = alt.Color('species', scale = scale),
        tooltip=['species', 'sex', 'island']
    )

Figure 2: A scatterplot of bill dimensions for penguins, made with
Altair.

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
    href="https://github.dev/quarto-dev/quarto-web/blob/main/docs/blog/posts/2023-03-17-jupyter-cell-embedding/penguins.ipynb"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
