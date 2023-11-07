# Quarto Presentations

Create beautiful interactive slide decks with Reveal.js

## Hello, There

This presentation will show you examples of what you can do with Quarto
and [Reveal.js](https://revealjs.com), including:

-   Presenting code and LaTeX equations
-   Including computations in slide output
-   Image, video, and iframe backgrounds
-   Fancy transitions and animations
-   Printing to PDF

…and much more

## Pretty Code

-   Over 20 syntax highlighting themes available
-   Default theme optimized for accessibility

    # Define a server for the Shiny app
    function(input, output) {
      
      # Fill in the spot we created for a plot
      output$phonePlot <- renderPlot({
        # Render a barplot
      })
    }

Learn more: [Syntax
Highlighting](https://quarto.org/docs/output-formats/html-code.html#highlighting)

## Code Animations

-   Over 20 syntax highlighting themes available
-   Default theme optimized for accessibility

    # Define a server for the Shiny app
    function(input, output) {
      
      # Fill in the spot we created for a plot
      output$phonePlot <- renderPlot({
        # Render a barplot
        barplot(WorldPhones[,input$region]*1000, 
                main=input$region,
                ylab="Number of Telephones",
                xlab="Year")
      })
    }

Learn more: [Code
Animations](https://quarto.org/docs/presentations/revealjs/advanced.html#code-animations)

## Line Highlighting

-   Highlight specific lines for emphasis
-   Incrementally highlight additional lines

    import numpy as np
    import matplotlib.pyplot as plt

    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi * r
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r)
    ax.set_rticks([0.5, 1, 1.5, 2])
    ax.grid(True)
    plt.show()

Learn more: [Line
Highlighting](https://quarto.org/docs/presentations/revealjs/#line-highlighting)

## Executable Code

    library(ggplot2)
    ggplot(mtcars, aes(hp, mpg, color = am)) +
      geom_point() +  geom_smooth(formula = y ~ x, method = "loess")

Learn more: [Executable
Code](https://quarto.org/docs/presentations/revealjs/#executable-code)

## LaTeX Equations

[MathJax](https://www.mathjax.org/) rendering of equations to HTML

    \begin{gather*}
    a_1=b_1+c_1\\
    a_2=b_2+c_2-d_2+e_2
    \end{gather*}

    \begin{align}
    a_{11}& =b_{11}&
      a_{12}& =b_{12}\\
    a_{21}& =b_{21}&
      a_{22}& =b_{22}+c_{22}
    \end{align}

<span class="math display">\\\[\begin{gather\*} a\_1=b\_1+c\_1\\\\
a\_2=b\_2+c\_2-d\_2+e\_2 \end{gather\*}\\\]</span> <span
class="math display">\\\[\begin{align} a\_{11}& =b\_{11}& a\_{12}&
=b\_{12}\\\\ a\_{21}& =b\_{21}& a\_{22}& =b\_{22}+c\_{22}
\end{align}\\\]</span>

Learn more: [LaTeX
Equations](https://quarto.org/docs/authoring/markdown-basics.html#equations)

## Column Layout

Arrange content into columns of varying widths:

#### Motor Trend Car Road Tests

The data was extracted from the 1974 Motor Trend US magazine, and
comprises fuel consumption and 10 aspects of automobile design and
performance for 32 automobiles.

<table>
<thead>
<tr class="header header">
<th style="text-align: left;"></th>
<th style="text-align: right;">mpg</th>
<th style="text-align: right;">cyl</th>
<th style="text-align: right;">disp</th>
<th style="text-align: right;">hp</th>
<th style="text-align: right;">wt</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td style="text-align: left;">Mazda RX4</td>
<td style="text-align: right;">21.0</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">160</td>
<td style="text-align: right;">110</td>
<td style="text-align: right;">2.620</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Mazda RX4 Wag</td>
<td style="text-align: right;">21.0</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">160</td>
<td style="text-align: right;">110</td>
<td style="text-align: right;">2.875</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Datsun 710</td>
<td style="text-align: right;">22.8</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">108</td>
<td style="text-align: right;">93</td>
<td style="text-align: right;">2.320</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Hornet 4 Drive</td>
<td style="text-align: right;">21.4</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">258</td>
<td style="text-align: right;">110</td>
<td style="text-align: right;">3.215</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Hornet Sportabout</td>
<td style="text-align: right;">18.7</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">360</td>
<td style="text-align: right;">175</td>
<td style="text-align: right;">3.440</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Valiant</td>
<td style="text-align: right;">18.1</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">225</td>
<td style="text-align: right;">105</td>
<td style="text-align: right;">3.460</td>
</tr>
</tbody>
</table>

Learn more: [Multiple
Columns](https://quarto.org/docs/presentations/revealjs/#multiple-columns)

## Incremental Lists

Lists can optionally be displayed incrementally:

-   First item
-   Second item
-   Third item

  
Insert pauses to make other types of content display incrementally.

Learn more: [Incremental
Lists](https://quarto.org/docs/presentations/revealjs/#incremental-lists)

## Fragments

Incremental text display and animation with fragments:

  

Fade in

Slide up while fading in

Slide left while fading in

Fade in then semi out

Strike

Highlight red

Learn more:
[Fragments](https://quarto.org/docs/presentations/revealjs/advanced.html#fragments)

## Slide Backgrounds

Set the `background` attribute on a slide to change the background color
(all CSS color formats are supported).

Different background transitions are available via the
`background-transition` option.

Learn more: [Slide
Backgrounds](https://quarto.org/docs/presentations/revealjs/#color-backgrounds)

## Media Backgrounds

You can also use the following as a slide background:

-   An image: `background-image`

-   A video: `background-video`

-   An iframe: `background-iframe`

Learn more: [Media
Backgrounds](https://quarto.org/docs/presentations/revealjs/#image-backgrounds)

## Absolute Position

Position images or other elements at precise locations

Learn more: [Absolute
Position](https://quarto.org/docs/presentations/revealjs/advanced.html#absolute-position)

## Auto-Animate

Automatically animate matching elements across slides with Auto-Animate.

Learn more:
[Auto-Animate](https://quarto.org/docs/presentations/revealjs/advanced.html#auto-animate)

## Auto-Animate

Automatically animate matching elements across slides with Auto-Animate.

Learn more:
[Auto-Animate](https://quarto.org/docs/presentations/revealjs/advanced.html#auto-animate)

## Slide Transitions

The next few slides will transition using the `slide` transition

<table style="width:99%;">
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header header">
<th>Transition</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td><code>none</code></td>
<td>No transition (default, switch instantly)</td>
</tr>
<tr class="even even">
<td><code>fade</code></td>
<td>Cross fade</td>
</tr>
<tr class="odd odd">
<td><code>slide</code></td>
<td>Slide horizontally</td>
</tr>
<tr class="even even">
<td><code>convex</code></td>
<td>Slide at a convex angle</td>
</tr>
<tr class="odd odd">
<td><code>concave</code></td>
<td>Slide at a concave angle</td>
</tr>
<tr class="even even">
<td><code>zoom</code></td>
<td>Scale the incoming slide so it grows in from the center of the
screen.</td>
</tr>
</tbody>
</table>

Learn more: [Slide
Transitions](https://quarto.org/docs/presentations/revealjs/advanced.html#slide-transitions)

## Tabsets

-   <a href="#tabset-1-1" data-tabby-default="">Plot</a>
-   [Data](#tabset-1-2)

<table style="width:100%;">
<colgroup>
<col style="width: 27%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header header">
<th style="text-align: left;"></th>
<th style="text-align: right;">mpg</th>
<th style="text-align: right;">cyl</th>
<th style="text-align: right;">disp</th>
<th style="text-align: right;">hp</th>
<th style="text-align: right;">drat</th>
<th style="text-align: right;">wt</th>
<th style="text-align: right;">qsec</th>
<th style="text-align: right;">vs</th>
<th style="text-align: right;">am</th>
<th style="text-align: right;">gear</th>
<th style="text-align: right;">carb</th>
</tr>
</thead>
<tbody>
<tr class="odd odd">
<td style="text-align: left;">Mazda RX4</td>
<td style="text-align: right;">21.0</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">160.0</td>
<td style="text-align: right;">110</td>
<td style="text-align: right;">3.90</td>
<td style="text-align: right;">2.620</td>
<td style="text-align: right;">16.46</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">4</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Mazda RX4 Wag</td>
<td style="text-align: right;">21.0</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">160.0</td>
<td style="text-align: right;">110</td>
<td style="text-align: right;">3.90</td>
<td style="text-align: right;">2.875</td>
<td style="text-align: right;">17.02</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">4</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Datsun 710</td>
<td style="text-align: right;">22.8</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">108.0</td>
<td style="text-align: right;">93</td>
<td style="text-align: right;">3.85</td>
<td style="text-align: right;">2.320</td>
<td style="text-align: right;">18.61</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Hornet 4 Drive</td>
<td style="text-align: right;">21.4</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">258.0</td>
<td style="text-align: right;">110</td>
<td style="text-align: right;">3.08</td>
<td style="text-align: right;">3.215</td>
<td style="text-align: right;">19.44</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">1</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Hornet Sportabout</td>
<td style="text-align: right;">18.7</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">360.0</td>
<td style="text-align: right;">175</td>
<td style="text-align: right;">3.15</td>
<td style="text-align: right;">3.440</td>
<td style="text-align: right;">17.02</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">2</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Valiant</td>
<td style="text-align: right;">18.1</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">225.0</td>
<td style="text-align: right;">105</td>
<td style="text-align: right;">2.76</td>
<td style="text-align: right;">3.460</td>
<td style="text-align: right;">20.22</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">1</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Duster 360</td>
<td style="text-align: right;">14.3</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">360.0</td>
<td style="text-align: right;">245</td>
<td style="text-align: right;">3.21</td>
<td style="text-align: right;">3.570</td>
<td style="text-align: right;">15.84</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">4</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Merc 240D</td>
<td style="text-align: right;">24.4</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">146.7</td>
<td style="text-align: right;">62</td>
<td style="text-align: right;">3.69</td>
<td style="text-align: right;">3.190</td>
<td style="text-align: right;">20.00</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">2</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Merc 230</td>
<td style="text-align: right;">22.8</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">140.8</td>
<td style="text-align: right;">95</td>
<td style="text-align: right;">3.92</td>
<td style="text-align: right;">3.150</td>
<td style="text-align: right;">22.90</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">2</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Merc 280</td>
<td style="text-align: right;">19.2</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">167.6</td>
<td style="text-align: right;">123</td>
<td style="text-align: right;">3.92</td>
<td style="text-align: right;">3.440</td>
<td style="text-align: right;">18.30</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">4</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Merc 280C</td>
<td style="text-align: right;">17.8</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">167.6</td>
<td style="text-align: right;">123</td>
<td style="text-align: right;">3.92</td>
<td style="text-align: right;">3.440</td>
<td style="text-align: right;">18.90</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">4</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Merc 450SE</td>
<td style="text-align: right;">16.4</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">275.8</td>
<td style="text-align: right;">180</td>
<td style="text-align: right;">3.07</td>
<td style="text-align: right;">4.070</td>
<td style="text-align: right;">17.40</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">3</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Merc 450SL</td>
<td style="text-align: right;">17.3</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">275.8</td>
<td style="text-align: right;">180</td>
<td style="text-align: right;">3.07</td>
<td style="text-align: right;">3.730</td>
<td style="text-align: right;">17.60</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">3</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Merc 450SLC</td>
<td style="text-align: right;">15.2</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">275.8</td>
<td style="text-align: right;">180</td>
<td style="text-align: right;">3.07</td>
<td style="text-align: right;">3.780</td>
<td style="text-align: right;">18.00</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">3</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Cadillac Fleetwood</td>
<td style="text-align: right;">10.4</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">472.0</td>
<td style="text-align: right;">205</td>
<td style="text-align: right;">2.93</td>
<td style="text-align: right;">5.250</td>
<td style="text-align: right;">17.98</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">4</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Lincoln Continental</td>
<td style="text-align: right;">10.4</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">460.0</td>
<td style="text-align: right;">215</td>
<td style="text-align: right;">3.00</td>
<td style="text-align: right;">5.424</td>
<td style="text-align: right;">17.82</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">4</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Chrysler Imperial</td>
<td style="text-align: right;">14.7</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">440.0</td>
<td style="text-align: right;">230</td>
<td style="text-align: right;">3.23</td>
<td style="text-align: right;">5.345</td>
<td style="text-align: right;">17.42</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">4</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Fiat 128</td>
<td style="text-align: right;">32.4</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">78.7</td>
<td style="text-align: right;">66</td>
<td style="text-align: right;">4.08</td>
<td style="text-align: right;">2.200</td>
<td style="text-align: right;">19.47</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Honda Civic</td>
<td style="text-align: right;">30.4</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">75.7</td>
<td style="text-align: right;">52</td>
<td style="text-align: right;">4.93</td>
<td style="text-align: right;">1.615</td>
<td style="text-align: right;">18.52</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">2</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Toyota Corolla</td>
<td style="text-align: right;">33.9</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">71.1</td>
<td style="text-align: right;">65</td>
<td style="text-align: right;">4.22</td>
<td style="text-align: right;">1.835</td>
<td style="text-align: right;">19.90</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Toyota Corona</td>
<td style="text-align: right;">21.5</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">120.1</td>
<td style="text-align: right;">97</td>
<td style="text-align: right;">3.70</td>
<td style="text-align: right;">2.465</td>
<td style="text-align: right;">20.01</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">1</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Dodge Challenger</td>
<td style="text-align: right;">15.5</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">318.0</td>
<td style="text-align: right;">150</td>
<td style="text-align: right;">2.76</td>
<td style="text-align: right;">3.520</td>
<td style="text-align: right;">16.87</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">2</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">AMC Javelin</td>
<td style="text-align: right;">15.2</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">304.0</td>
<td style="text-align: right;">150</td>
<td style="text-align: right;">3.15</td>
<td style="text-align: right;">3.435</td>
<td style="text-align: right;">17.30</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">2</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Camaro Z28</td>
<td style="text-align: right;">13.3</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">350.0</td>
<td style="text-align: right;">245</td>
<td style="text-align: right;">3.73</td>
<td style="text-align: right;">3.840</td>
<td style="text-align: right;">15.41</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">4</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Pontiac Firebird</td>
<td style="text-align: right;">19.2</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">400.0</td>
<td style="text-align: right;">175</td>
<td style="text-align: right;">3.08</td>
<td style="text-align: right;">3.845</td>
<td style="text-align: right;">17.05</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">3</td>
<td style="text-align: right;">2</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Fiat X1-9</td>
<td style="text-align: right;">27.3</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">79.0</td>
<td style="text-align: right;">66</td>
<td style="text-align: right;">4.08</td>
<td style="text-align: right;">1.935</td>
<td style="text-align: right;">18.90</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Porsche 914-2</td>
<td style="text-align: right;">26.0</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">120.3</td>
<td style="text-align: right;">91</td>
<td style="text-align: right;">4.43</td>
<td style="text-align: right;">2.140</td>
<td style="text-align: right;">16.70</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">5</td>
<td style="text-align: right;">2</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Lotus Europa</td>
<td style="text-align: right;">30.4</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">95.1</td>
<td style="text-align: right;">113</td>
<td style="text-align: right;">3.77</td>
<td style="text-align: right;">1.513</td>
<td style="text-align: right;">16.90</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">5</td>
<td style="text-align: right;">2</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Ford Pantera L</td>
<td style="text-align: right;">15.8</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">351.0</td>
<td style="text-align: right;">264</td>
<td style="text-align: right;">4.22</td>
<td style="text-align: right;">3.170</td>
<td style="text-align: right;">14.50</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">5</td>
<td style="text-align: right;">4</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Ferrari Dino</td>
<td style="text-align: right;">19.7</td>
<td style="text-align: right;">6</td>
<td style="text-align: right;">145.0</td>
<td style="text-align: right;">175</td>
<td style="text-align: right;">3.62</td>
<td style="text-align: right;">2.770</td>
<td style="text-align: right;">15.50</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">5</td>
<td style="text-align: right;">6</td>
</tr>
<tr class="odd odd">
<td style="text-align: left;">Maserati Bora</td>
<td style="text-align: right;">15.0</td>
<td style="text-align: right;">8</td>
<td style="text-align: right;">301.0</td>
<td style="text-align: right;">335</td>
<td style="text-align: right;">3.54</td>
<td style="text-align: right;">3.570</td>
<td style="text-align: right;">14.60</td>
<td style="text-align: right;">0</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">5</td>
<td style="text-align: right;">8</td>
</tr>
<tr class="even even">
<td style="text-align: left;">Volvo 142E</td>
<td style="text-align: right;">21.4</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">121.0</td>
<td style="text-align: right;">109</td>
<td style="text-align: right;">4.11</td>
<td style="text-align: right;">2.780</td>
<td style="text-align: right;">18.60</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">2</td>
</tr>
</tbody>
</table>

Learn more:
[Tabsets](https://quarto.org/docs/presentations/revealjs/#tabsets)

## Interactive Slides

Include Jupyter widgets and htmlwidgets in your presentations

Learn more: [Jupyter
widgets](https://quarto.org/docs/interactive/widgets/jupyter.html),
[htmlwidgets](https://quarto.org/docs/interactive/widgets/htmlwidgets.html)

## Interactive Slides

Turn presentations into applications with Observable and Shiny. Use
component layout to position inputs and outputs.

    viewof talentWeight = Inputs.range([-2, 2], { value: 0.7, step: 0.01, label: "talent weight" })
    viewof looksWeight = Inputs.range([-2, 2], { value: 0.7, step: 0.01, label: "looks weight" })
    viewof minimum = Inputs.range([-2, 2], { value: 1, step: 0.01, label: "min fame" })

    import { plotActors } from './actors.js';
    plotActors(actors, talentWeight, looksWeight, minimum)

Learn more: [Observable](https://quarto.org/docs/interactive/ojs/),
[Shiny](https://quarto.org/docs/interactive/shiny/), [Component
Layout](https://quarto.org/docs/interactive/layout.html)

## Preview Links

Navigate to hyperlinks without disrupting the flow of your presentation.

Use the `preview-links` option to open links in an iframe on top of your
slides. Try clicking the link below for a demonstration:

<a href="https://matplotlib.org/" data-preview-link="true"
style="text-align: center">Matplotlib: Visualization with Python</a>

Learn more: [Preview
Links](https://quarto.org/docs/presentations/revealjs/presenting.html#preview-links)

## Themes

10 Built-in Themes (or [create your
own](https://quarto.org/docs/presentations/revealjs/themes.html#creating-themes))

Learn more:
[Themes](https://quarto.org/docs/presentations/revealjs/themes.html)

## Easy Navigation

Quickly jump to other parts of your presentation

Toggle the slide menu with the menu button (bottom left of slide) to go
to other slides and access presentation tools.

You can also press `m` to toggle the menu open and closed.

Learn more:
[Navigation](https://quarto.org/docs/presentations/revealjs/presenting.html#navigation-menu)

## Chalkboard

Free form drawing and slide annotations

Use the chalkboard button at the bottom left of the slide to toggle the
chalkboard.

Use the notes canvas button at the bottom left of the slide to toggle
drawing on top of the current slide.

You can also press `b` to toggle the chalkboard or `c` to toggle the
notes canvas.

Learn more:
[Chalkboard](https://quarto.org/docs/presentations/revealjs/presenting.html#chalkboard)

## Point of View

Press `o` to toggle overview mode:

Hold down the `Alt` key (or `Ctrl` in Linux) and click on any element to
zoom towards it—try it now on this slide.

Learn more: [Overview
Mode](https://quarto.org/docs/presentations/revealjs/presenting.html#overview-mode),
[Slide
Zoom](https://quarto.org/docs/presentations/revealjs/presenting.html#slide-zoom)

## Speaker View

Press `s` (or use the presentation menu) to open speaker view

Learn more: [Speaker
View](https://quarto.org/docs/presentations/revealjs/presenting.html#speaker-view)

## Authoring Tools

Live side-by-side preview for any notebook or text editor including
Jupyter and VS Code

Learn more: [Jupyter](https://quarto.org/docs/tools/jupyter-lab.html),
[VS Code](https://quarto.org/docs/tools/vscode.html), [Text
Editors](https://quarto.org/docs/tools/text-editors.html)

## Authoring Tools

RStudio includes an integrated presentation preview pane

Learn more: [RStudio](https://quarto.org/docs/tools/rstudio.html)

## And More…

-   [Touch](https://quarto.org/docs/presentations/revealjs/advanced.html#touch-navigation)
    optimized (presentations look great on mobile, swipe to navigate
    slides)
-   [Footer &
    Logo](https://quarto.org/docs/presentations/revealjs/#footer-logo)
    (optionally specify custom footer per-slide)
-   [Auto-Slide](https://quarto.org/docs/presentations/revealjs/presenting.html#auto-slide)
    (step through slides automatically, without any user input)
-   [Multiplex](https://quarto.org/docs/presentations/revealjs/presenting.html#multiplex)
    (allows your audience to follow the slides of the presentation you
    are controlling on their own phone, tablet or laptop).

Learn more: [Quarto
Presentations](https://quarto.org/docs/presentations/revealjs/)

<img src="images/quarto.png" class="slide-logo r-stretch" />

<https://quarto.org>
