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

# Quarto 1.3

Quarto 1.3 is officially released

Quarto 1.3 brings new features, improvements, and fixes.

Quarto 1.3

Author

Charlotte Wickham

Published

April 26, 2023

## On this page

-   <a href="#code-annotation" id="toc-code-annotation"
    class="nav-link active" data-scroll-target="#code-annotation">Code
    Annotation</a>
-   <a href="#multi-format-publishing" id="toc-multi-format-publishing"
    class="nav-link"
    data-scroll-target="#multi-format-publishing">Multi-format
    Publishing</a>
-   <a href="#jupyter-cell-embedding" id="toc-jupyter-cell-embedding"
    class="nav-link" data-scroll-target="#jupyter-cell-embedding">Jupyter
    Cell Embedding</a>
-   <a href="#confluence-publishing" id="toc-confluence-publishing"
    class="nav-link" data-scroll-target="#confluence-publishing">Confluence
    Publishing</a>
-   <a href="#other-highlights" id="toc-other-highlights" class="nav-link"
    data-scroll-target="#other-highlights">Other Highlights</a>
-   <a href="#acknowledgements" id="toc-acknowledgements" class="nav-link"
    data-scroll-target="#acknowledgements">Acknowledgements</a>

-   <a
    href="https://github.com/quarto-dev/quarto-web/edit/main/docs/blog/posts/2023-04-26-1.3-release/index.qmd"
    class="toc-action"><em></em>Edit this page</a>
-   <a href="https://github.com/quarto-dev/quarto-cli/issues/new/choose"
    class="toc-action"><em></em>Report an issue</a>

We are happy to announce that Quarto 1.3 has been released. You can grab
the current release from <https://quarto.org/docs/download/>.

If you are ever wondering which version of Quarto you are using, a quick
way to check on the command line is:

    Terminal

    quarto --version

We’ve previously blogged about some of the features of this release that
we were most excited about, but let’s highlight them again.

## Code Annotation

You can now add line-based annotations to your code blocks using special
code comments along with an ordered list. Code annotations work across
many formats, and are interactive in HTML-based formats.

<figure>
<img src="../2023-03-13-code-annotation/annotation.png"
class="img-fluid figure-img"
alt="Code Annotation in an HTML document" />
<figcaption aria-hidden="true">Code Annotation in an HTML
document</figcaption>
</figure>

To learn more, check out the [Code
Annotation](../../../../docs/authoring/code-annotation.html)
documentation.

## Multi-format Publishing

HTML pages (either standalone or in a website) now automatically include
links to other formats specified in the document front matter. For
example, the following document front matter:

    title: Sample Page
    author: Norah Jones
    date: last-modified
    toc: true
    format: 
      html: default
      ipynb: default

Results in an HTML page that includes a link to the additional notebook
format in the right margin below the table of contents:

<figure>
<img src="../../../output-formats/images/other-format.png"
class="border img-fluid figure-img"
alt="An HTML document with a link to another format" />
<figcaption aria-hidden="true">An HTML document with a link to another
format</figcaption>
</figure>

Find out more in the documentation on [Including Other
Formats](../../../../docs/output-formats/html-multi-format.html).

## Jupyter Cell Embedding

Easily include the output of an external Jupyter notebook in a Quarto
document with the `embed` shortcode. Provide the path to a Jupyter
Notebook and a cell identifier and the output will be included in your
document along with a link back to the source Notebook.

<figure>
<img src="../2023-03-17-jupyter-cell-embedding/embed.png"
class="img-fluid figure-img"
alt="A plot embedded in a document from a Jupyter Notebook" />
<figcaption aria-hidden="true">A plot embedded in a document from a
Jupyter Notebook</figcaption>
</figure>

Learn more about the embed shortcode in [Embedding Jupyter Notebook
Cells](../../../../docs/authoring/notebook-embed.html) in the docs.

## Confluence Publishing

[Atlassian Confluence](https://www.atlassian.com/software/confluence) is
a publishing platform for supporting team collaboration. Quarto now
provides support for publishing individual documents, as well as
projects composed of multiple documents, into [Confluence
Spaces](https://support.atlassian.com/confluence-cloud/docs/use-spaces-to-organize-your-work/).

<figure>
<img src="../../../publishing/images/confluence-project.png"
class="img-fluid figure-img" alt="A Quarto Project" />
<figcaption aria-hidden="true">A Quarto Project</figcaption>
</figure>

<figure>
<img src="../../../publishing/images/confluence-site.png"
class="img-fluid figure-img" alt="Published to Confluence" />
<figcaption aria-hidden="true">Published to Confluence</figcaption>
</figure>

To learn more, head to the documentation on [Confluence
Publishing](../../../../docs/publishing/confluence.html).

## Other Highlights

Some other notable highlights include:

-   [Article Grid
    Customization](../../../../docs/output-formats/page-layout.html#grid-customization)—Customize
    the widths of layout components in HTML documents

-   [Quarto Book AsciiDoc
    Support](../../../../docs/books/index.html)—Output Quarto books to
    AsciiDoc files

-   [Website Navigation
    Improvements](../../../../docs/prerelease/1.3/website-nav.html)—Include
    tools in your navbar, and provide better navigation for Quarto
    websites on mobile devices

-   [Mermaid Diagram
    Theming](../../../../docs/authoring/diagrams.html#mermaid-theming)—Use
    your document theme, or built-in Mermaid themes, for your Mermaid
    diagrams

-   [PDF: SVG and Remote
    Images](../../../../docs/prerelease/1.3/pdf.html)—Include SVG images
    and remote images in PDF documents

-   [`kbd`
    Shortcode](../../../../docs/authoring/markdown-basics.html#keyboard-shortcuts)—Show
    well-formatted keyboard shortcuts in Quarto documents.

You can find all the other changes in 1.3, in the [Release
Notes](https://quarto.org/docs/download/#download-section-news).

## Acknowledgements

We’d like to say a huge thank you to everyone who contributed to this
release by opening issues and pull requests:

[ABohynDOE](https://github.com/ABohynDOE),
[aborruso](https://github.com/aborruso),
[agerlach](https://github.com/agerlach),
[aimundo](https://github.com/aimundo),
[alperyilmaz](https://github.com/alperyilmaz),
[ameliaritger](https://github.com/ameliaritger),
[anaveenan](https://github.com/anaveenan),
[andrewheiss](https://github.com/andrewheiss),
[apreshill](https://github.com/apreshill),
[apsteinmetz](https://github.com/apsteinmetz),
[arnaudgallou](https://github.com/arnaudgallou),
[aronatkins](https://github.com/aronatkins),
[arronlacey](https://github.com/arronlacey),
[ArturKlauser](https://github.com/ArturKlauser),
[astrowonk](https://github.com/astrowonk),
[ats](https://github.com/ats),
[awehrfritz](https://github.com/awehrfritz),
[b-rodrigues](https://github.com/b-rodrigues),
[baptiste](https://github.com/baptiste),
[batpigandme](https://github.com/batpigandme),
[bayeslearner](https://github.com/bayeslearner),
[benabel](https://github.com/benabel),
[BertTijhuis](https://github.com/BertTijhuis),
[boshek](https://github.com/boshek),
[brunomioto](https://github.com/brunomioto),
[busemorose](https://github.com/busemorose),
[bvancil](https://github.com/bvancil),
[bwelman](https://github.com/bwelman),
[cboettig](https://github.com/cboettig),
[cgoo4](https://github.com/cgoo4),
[ChoCho66](https://github.com/ChoCho66),
[cicarrascog](https://github.com/cicarrascog),
[coatless](https://github.com/coatless),
[code86](https://github.com/code86),
[condwanaland](https://github.com/condwanaland),
[daniel-smit-haw](https://github.com/daniel-smit-haw),
[daranzolin](https://github.com/daranzolin),
[davidbudzynski](https://github.com/davidbudzynski),
[DavidD003](https://github.com/DavidD003),
[ddobrinskiy](https://github.com/ddobrinskiy),
[dgkf](https://github.com/dgkf),
[DhruvaSambrani](https://github.com/DhruvaSambrani),
[directknowledge](https://github.com/directknowledge),
[dkubek](https://github.com/dkubek),
[dmalan](https://github.com/dmalan),
[dmenne](https://github.com/dmenne),
[drcaprosser](https://github.com/drcaprosser),
[drscotthawley](https://github.com/drscotthawley),
[edoson](https://github.com/edoson),
[eeholmes](https://github.com/eeholmes),
[eitsupi](https://github.com/eitsupi),
[elgabbas](https://github.com/elgabbas),
[EllaKaye](https://github.com/EllaKaye),
[emmansh](https://github.com/emmansh),
[ericvmai](https://github.com/ericvmai),
[espinielli](https://github.com/espinielli),
[etiennebacher](https://github.com/etiennebacher),
[EvoArt](https://github.com/EvoArt), [fire](https://github.com/fire),
[fortunewalla](https://github.com/fortunewalla),
[freestatman](https://github.com/freestatman),
[fuhrmanator](https://github.com/fuhrmanator),
[fulem](https://github.com/fulem),
[g-simmons](https://github.com/g-simmons),
[gadenbuie](https://github.com/gadenbuie),
[GegznaV](https://github.com/GegznaV),
[ghost](https://github.com/ghost),
[giabaio](https://github.com/giabaio),
[githubpsyche](https://github.com/githubpsyche),
[GraceEMc](https://github.com/GraceEMc),
[gregswinehart](https://github.com/gregswinehart),
[GShotwell](https://github.com/GShotwell),
[guoruizhong](https://github.com/guoruizhong),
[harrelfe](https://github.com/harrelfe),
[hemonika](https://github.com/hemonika),
[henningsway](https://github.com/henningsway),
[iandol](https://github.com/iandol),
[ijlyttle](https://github.com/ijlyttle),
[iusgit](https://github.com/iusgit),
[ivanek](https://github.com/ivanek),
[jake-wittman](https://github.com/jake-wittman),
[jakobarendt](https://github.com/jakobarendt),
[jakub-jedrusiak](https://github.com/jakub-jedrusiak),
[javajon](https://github.com/javajon),
[jcmkk3](https://github.com/jcmkk3),
[jcolomb](https://github.com/jcolomb),
[jdutant](https://github.com/jdutant),
[JeffreyRacine](https://github.com/JeffreyRacine),
[jensschroer](https://github.com/jensschroer),
[jeremiahpslewis](https://github.com/jeremiahpslewis),
[jfbarthelemy](https://github.com/jfbarthelemy),
[jhelvy](https://github.com/jhelvy),
[Jiayou-Chao](https://github.com/Jiayou-Chao),
[jimjam-slam](https://github.com/jimjam-slam),
[jkylearmstrong](https://github.com/jkylearmstrong),
[jmbarbone](https://github.com/jmbarbone),
[jmbuhr](https://github.com/jmbuhr),
[jmcastagnetto](https://github.com/jmcastagnetto),
[joelvonrotz](https://github.com/joelvonrotz),
[JoFrhwld](https://github.com/JoFrhwld),
[johannes4998](https://github.com/johannes4998),
[jrcuesta](https://github.com/jrcuesta),
[jthomasmock](https://github.com/jthomasmock),
[juba](https://github.com/juba),
[justanothergithubber](https://github.com/justanothergithubber),
[KaiWaldrant](https://github.com/KaiWaldrant),
[kalenkovich](https://github.com/kalenkovich),
[kdheepak](https://github.com/kdheepak),
[kelly-sovacool](https://github.com/kelly-sovacool),
[KittJonathan](https://github.com/KittJonathan),
[kmasiello](https://github.com/kmasiello),
[knuesel](https://github.com/knuesel),
[koehlerson](https://github.com/koehlerson),
[koushikkhan](https://github.com/koushikkhan),
[lcnbr](https://github.com/lcnbr), [leovan](https://github.com/leovan),
[linogaliana](https://github.com/linogaliana),
[m-legrand](https://github.com/m-legrand),
[m4jing](https://github.com/m4jing),
[machow](https://github.com/machow),
[maelle](https://github.com/maelle),
[malcolmbarrett](https://github.com/malcolmbarrett),
[marierivers](https://github.com/marierivers),
[MattF-NSIDC](https://github.com/MattF-NSIDC),
[mattsams89](https://github.com/mattsams89),
[mattwarkentin](https://github.com/mattwarkentin),
[maxdrohde](https://github.com/maxdrohde),
[mccarthy-m-g](https://github.com/mccarthy-m-g),
[MHellmund](https://github.com/MHellmund),
[mikheyev](https://github.com/mikheyev),
[mine-cetinkaya-rundel](https://github.com/mine-cetinkaya-rundel),
[mksinicus](https://github.com/mksinicus),
[mrajeev08](https://github.com/mrajeev08),
[nanxstats](https://github.com/nanxstats),
[NeubertJonas](https://github.com/NeubertJonas),
[nikcleju](https://github.com/nikcleju),
[njbart](https://github.com/njbart),
[patrickvdb](https://github.com/patrickvdb),
[petrbouchal](https://github.com/petrbouchal),
[philip-khor](https://github.com/philip-khor),
[philwunderlich](https://github.com/philwunderlich),
[Pierre9344](https://github.com/Pierre9344),
[pitmonticone](https://github.com/pitmonticone),
[pmagwene](https://github.com/pmagwene),
[poldrack](https://github.com/poldrack),
[pommevilla](https://github.com/pommevilla),
[psychelzh](https://github.com/psychelzh),
[ratnanil](https://github.com/ratnanil),
[ravimakhija](https://github.com/ravimakhija),
[RaymondBalise](https://github.com/RaymondBalise),
[reuning](https://github.com/reuning),
[rexdouglass](https://github.com/rexdouglass),
[rgaiacs](https://github.com/rgaiacs),
[richardsprague](https://github.com/richardsprague),
[rjake](https://github.com/rjake),
[rleyvasal](https://github.com/rleyvasal),
[rmcd1024](https://github.com/rmcd1024),
[RobTour](https://github.com/RobTour),
[rsenft1](https://github.com/rsenft1),
[runlevel0](https://github.com/runlevel0),
[sagikazarmark](https://github.com/sagikazarmark),
[salim-b](https://github.com/salim-b),
[SamEdwardes](https://github.com/SamEdwardes),
[samperman](https://github.com/samperman),
[schochastics](https://github.com/schochastics),
[ScientiaFelis](https://github.com/ScientiaFelis),
[scottamain](https://github.com/scottamain),
[scottfranz](https://github.com/scottfranz),
[sebastian-c](https://github.com/sebastian-c),
[seeM](https://github.com/seeM),
[shafayetShafee](https://github.com/shafayetShafee),
[singuyenmai](https://github.com/singuyenmai),
[sje30](https://github.com/sje30),
[snhansen](https://github.com/snhansen),
[streepvaren](https://github.com/streepvaren),
[thedabs91](https://github.com/thedabs91),
[thomashallam](https://github.com/thomashallam),
[timothee-bacri](https://github.com/timothee-bacri),
[tomshafer](https://github.com/tomshafer),
[tomsutch](https://github.com/tomsutch),
[tomvaneyck](https://github.com/tomvaneyck),
[topepo](https://github.com/topepo),
[tverbeiren](https://github.com/tverbeiren),
[TylerHillery](https://github.com/TylerHillery),
[ucpresearch](https://github.com/ucpresearch),
[verbalins](https://github.com/verbalins),
[vfacta](https://github.com/vfacta),
[vlyubchich](https://github.com/vlyubchich),
[VMTdeJong](https://github.com/VMTdeJong),
[vpratz](https://github.com/vpratz),
[white-c](https://github.com/white-c),
[wklimowicz](https://github.com/wklimowicz),
[XiangyunHuang](https://github.com/XiangyunHuang),
[Xitian9](https://github.com/Xitian9), [xl0](https://github.com/xl0),
[xtimbeau](https://github.com/xtimbeau), [y9c](https://github.com/y9c),
[yevgenryeznik](https://github.com/yevgenryeznik),
[zachcp](https://github.com/zachcp), [zkwabm](https://github.com/zkwabm)

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

-   <a href="https://twitter.com/quarto_pub" class="nav-link"><em></em></a>
-   <a href="https://github.com/quarto-dev/quarto-cli"
    class="nav-link"><em></em></a>
-   <a href="https://quarto.org/docs/blog/index.xml"
    class="nav-link"><em></em></a>
