Introduction
============

A plone.app.theming theme skeleton, based on HTML5 Boilerplate, Twitter
Bootstrap, Modernizr, Retina.JS and Less Css, designed to be the starting point
for rapid theme development.


HTML 5 Boilerplate
==================

The main template that we are using is based on the index.html file from
HTML 5 Boilerplate, modified to meet our responsive and layout needs.


Twitter Bootstrap
=================

Twitter Boostrap was used as a starting point for styling and we ended up with
a fully customized version of it by stripping out parts that we don't use and
putting in extra styles that are needed by Plone. We packaged in the basic
bootstrap's styles as well, so they just need to be enabled in order to use the
stripped out parts.
The javascript plugins are also included.


Modernizr
=========

A customized version of Modernizr can be found in this package, and we strongly
advise to build you own custom version to include only the checks that are
really needed, as it slows down the page's load time.


Retina.JS
=========

Support for high resolution graphics is provided by Retina.JS. As the default
version of it checks all the images on the page if there are high resolution
versions of them available, this results in plenty of ajax requests. To keep the
request count low, we have modified this library to check only for images that
have the "retina" class attribute.


Less Css
========

We are using lesscss.org for development, which produces the final css that is
used by Plone. This means that less is only used in the development process,
and the less files are compiled before they are used by Plone. We are using
CodeKit for the compiling and it needs to be set up so the output of style.less
goes to our css folder.


Javascript
==========

HTML5Boilerplate suggests to have all Javascript plugins in plugins.js and all
user scripts in script.js. We have decided to go against it, and we are using
Plone's default javascript registry. The final result is the same, as Plone does
merge and minimize all the registered javascripts.

Javascript/script.js holds the javascript functions for the theme. Every
additional javascript should go into this file. If you need multiple files for
javascript, just create them in the javascript folder and include them in
Plone's JS registry (profiles/default/jsregistry.xml).



Plone.app.theming
=================

index.html is the main template that we use, so to have a custom layout, you'll
need to modify this file. The header tag holds the header of the site, the div
with id="visual-portal-wrapper" should hold the body region, and the footer tag
should hold the footer.

Some selectors in Plone rely on having the visual-portal-wrapper id present, so
we have just included an additional wrapper div within the main div.

The mobile version of the theme has a slightly different layout for the menu and
search, so we have included additional elements in our main layout and updated
the rules. The final generated html has the same structure, so there will be no
problems with the selectors used by Plone.

rules.xml is the rules file which includes the rules_base.xml, where we have set
up the copying of the css and javascripts to proper location within the
index.html, and it also includes rules that copy everything from Plone and put
it into proper place. Feel free to modify this to suite your needs. Boilerplate
encourages us to have the styles and javascript inclusions in specific places,
so please don't modify the rules that make this happen.

Within the less files, there are relative paths to some images, and Diazo will
append a previously set prefix on them, even though we actually don't want that.
One of the solutions would be to split the CSS files into two groups, the one
that need prefix applied, and ones that don't. Html 5 Boilerplate suggests to
have all the styles in one file, so we decided not to modify the structure, but
to include the missing images in our theme. This way we don't rely on other
products and we can easily update the images to suite our needs.


Structure of less files
-----------------------

The less folder holds all the css needed by Plone, so there is no need for
additional css. We have disabled all the default css that we don't need in
profiles/default/cssregistry.xml

We have three major devices that we are theming for: mobile, tablet and desktop.
All of them have a separate file that holds all the styles that are applied
only for the specific device. The styles that are in common to all are located
in appropriate files.

The starting point for this project was the Twitter Bootstrap, so we took the
needed styles from there, modified them to apply to Plone's markup and polished
them out for a final professional look.

For fast development, we need a quick way to change the default colors and
styling to reflect the design we are implementing, so we have modified the
files so they use variables that are set in one location. This is something that
we have seen before in form of base_properties.props, but this time we are doing
it right with less variables.

The theme specific styling that cannot be set in variables.less, should go to
custom.less. If you would like to have multiple custom files for your theme,
just create a new .less file and include it to style.less.

For styles that should be applied to mobile version only, we add them to
plone/moible.less. The same goes for plone/desktop.less and plone/tablet.less.

The media queries have been moved out from style.less to responsive.less to have
clear separation of the styles. Also this was done because of a bug that was
present in Internet Explorer 9. When the rich text editor is initialized, it
picks up all the css from portal css and puts it in the iframe that contains
the editor. This way the media queries were picked up too, and their presence in
multiple places on one page caused IE9 to flicker between mobile-tablet-desktop
mode. To prevent this, the css that holds the media queries have been moved
outside of portal css and it's included directly in index.html.


Javascript position within the page
-----------------------------------
The default behavior for 'script' tags are to be moved to the bottom of the
page. Some external widgets however require to have the 'script' tag in
specific location within the page. For this purpose we have created special
Diazo rules that will take care of the positioning.
To leave the tag in place, set the data-js-move attribute to 'js-dont-move':

    <script src="foo.js" data-js-move="js-dont-move"></script>

To move the tag to the head, set the data-js-move attribute to
'js-move-to-head':

    <script src="foo.js" data-js-move="js-move-to-head"></script>

To move the tag to the beginning of the body, set the data-js-move attribute
to 'js-move-to-beginning-of-body':

    <script src="foo.js" data-js-move="js-move-to-beginning-of-body"></script>

Exceptions
----------

Modernizer.js and Retina.js should be the only JS in the header, as it is hard
to have a rule that will put it there, we have put only these two js in the
index.html and it is not served from Plone’s js registry. In case if the site is
loaded without the Diazo theme, the modernizer.js and retina.js will be
provided by Plone.
Browsers that do not support media queries will display the site in desktop mode
only, as these are only desktop browsers.


Layout
======

The layout is constructed with responsive design in mind, and it can have from 1
to 3 columns.
Setting the width of the portal columns using the Deco grid will produce a fluid
width of the left and right columns. In some cases we need fixed with sidebars,
so special care has been been put into supporting this feature. In
variables.less the width can be set either to fixed number of pixels, or
percentages for variable widths:

    @sidebar-right-width: 300px; // or 25%
    @sidebar-left-width: 200px; // or 25%
    @sidebar-right-margin-left: 12px; // or 1.125%
    @sidebar-left-margin-right: 12px; // or 1.125%


Sidebar position
----------------
Some layouts require both of the sidebars to be on the right hand side.
In manifest.cfg there is a theme parameter set that is used to determine if the
sidebars should be on the right. This allows us to modify the layout without the
need to actually modify the templates:

    sidebarsright = python: False

True value is for moving the sidebars to the right, False for having one on the
left and one on the right.

This value can be updated in the control panel -> Diazo theme -> Advanced
settings too.


Sidebar behavior for tablet
---------------------------
As there is not enough room for both of the sidebars on a tablet, we need to
move one of them below the content. In manifest.cfg there is a theme parameter
set that is used to determine which column should be moved below the content.
To move the left column down set:

    tabletleftcolumndown = python: True

To move the right column down set:

    tabletleftcolumndown = python: False

This value can be updated in the control panel -> Diazo theme -> Advanced
settings too.


Deco Grid System
================

We are using the Deco Grid System that comes with Plone for the content column.
The size of the columns and gutters are set in percentages:
column width - 4%
margin left/right - 1.125%

Here are some recommended sizes (page width / column width / left/right margin):
Desktop: 1088px / 44px / 12px - (http://gridcalculator.dk/#/1088/16/24/12)
Tablet:   800px / 32px /  9px - (http://gridcalculator.dk/#/800/16/18/9)
Mobile:   480px / 20px /  5px - (http://gridcalculator.dk/#/480/16/10/5)



Best practices (Do's and Don'ts)
================================

Setting grid widths and positions in the stylesheets
----------------------------------------------------
The responsive design often forces us to have different widths and positions
for the same element on different screen sizes, and as we can't edit the markup,
we'll need to apply these changes in our stylesheets. Instead of giving it a
fixed width value, we can use the .grid-column-width() and .grid-position()
mixins. To set an element to be 6 columns wide and on position 3, just add this
to the appropriate css selector:

    .grid-column-width(6)
    .grid-position(3)

This mixin will calculate the appropriate width and margin for our element.


Centering a fixed width body
----------------------------
To be more precise, the title should be "Centering a fixed width container". The
main idea is to set a fixed width to the container that holds all the elements,
and center it. This way we can have a different background for the body and for
the container.

Responsive design suggests to have a fixed width layout only when the browser
window is wide enough, so we have included the bodyMaxWidth variable in
variables.less where you can set the desired width of the page.


Having multiple looks for the portlets
--------------------------------------
We recommend using hexagonit.portletstyle plugin for this so you will need to
set it up to be a dependency. Once it's set up, we can specify the portlet
styles and their css idendifiers by editing profiles/default/registry.xml. This
way on each install these styles will be available. These values show up in the
control panel so you can modify them on the fly, just remember to update the
registry.xml once done experimenting.


Using custom logo
-----------------
Most of the sites have a unique logo, so we are serving it from our theme and
not from Plone. Make sure to put the new logo in the images folder. The main
Diazo template already has the appropriate code for this, just the height and
width attribute needs to be update to match the size of the logo.

    <a href="#" accesskey="1" title="Site" id="portal-logo">
        <img width="305" height="32" title="Site" alt="Site" src="images/logo.png" />
    </a>


Show content only when the user is logged in
--------------------------------------------
For example we want to show portal-personaltools only for logged in users.
In rules.xml add:

    <before css:content="#portal-personaltools-wrapper"
            css:theme="#portal-logo"
            css:if-content="#portal-header .actionMenuHeader" />


Remove advanced search options from search box in the header
------------------------------------------------------------
This has become a default state, so if you wish to switch back to have the
advanced search options, find these lines in rules_base.xml and comment them
out:

    <drop css:content=".searchSection" />
    <drop css:content="#portal-advanced-search" />


Move breadcrumbs outside of the content column
----------------------------------------------
If you need to move a sub-element of an element that is copied by another rule,
then you just can't drop it and append it to another place, but you have to drop
it and use method="raw" to include it in the other location:

    <drop css:content="#portal-breadcrumbs"/>
    <replace css:content="#portal-breadcrumbs"
             css:theme="#portal-breadcrumbs"
             method="raw" />


Fix for IE7 hasLayout bug
-------------------------
Internet Explorer has a nice habit of not applying layout to some elements and
that manifests in an overall messed up look of the site. Usually adding some
css properties that are default values in browsers resolve this bug, so first
try setting them in global level, and if that messes up the look in other
browsers, only then apply it with the .ie7 parent class.
Read more about this bug and possible fixes on:
http://haslayout.net/haslayout


IE TinyMCE body background color bug
------------------------------------
If you are using the background gradient for the body tag, then IE will apply
the same gradient to the body tags within the iframes. To work around this bug,
set a new background gradient only for TinyMCE body that will go from white
to white:

    .mceContentBody {
        #gradient > .horizontal(#FFF, #FFF);
    }


Contain floats
--------------
Instead of having an additional element after the floats and applying clear:both
in your css, just apply the clearfix css class to your html element that
contains the floated elements.

If the content that needs to be cleared is copied with a diazo rule and we don't
have access to its html, then apply the .clearfix() mixin to it in the
appropriate less file.


Using custom fonts
------------------
@Font-Face is used for applying custom fonts. The preferred way is to have the
font files on your server and use that. The other way would be to use Google
Font API or FontSquirrel. Both are free and have big font collection that are
licensed for web.
With google, only a stylesheet is added to the page, which points to their
server and they will provide all the font files that are needed.
With FontSquirrel you download everything and serve it from your server.
In case if you do not find the proper font, and have a web license for that
font, FontSquirrel @Type-face Generator can be used to generate all the formats
needed by browsers, and it will provide some basic html and css codes as well.
Important: The font used must be licensed for web usage.

The font-face is defined in plone/type.less, and the font files should go into
themere_resources/fonts folder.


Using theme parameters
----------------------
Diazo lets us set variables for a theme within the manifest.cfg that will end
up in @@theming-controlpanel. To use these parameters, we need XSLT.

Display the value of the parameter as a content of an element:

    <xsl:value-of select="$tabletleftcolumndown"/>

Use the parameter for an if-statement:

    <rules if="$tabletleftcolumndown">
or:
    <xsl:if test="$tabletleftcolumndown">

Add the value of the parameter to a class attribute:

    <xsl:attribute name="class">$tabletleftcolumndown</xsl:attribute>


iOS image sizes
---------------
iOS has the possibility of creating an application from a website, so we need
icons and splash screens for it. These images need to be specific sizes in
order to be shown. If the size does not match, it will be ignored.
From iOS 5, media queries can be used for the link tags that set the icons and
splash. We are using these media queries only for the splash, as for the icons
we can use sizes attribute which is backward compatible.

Application icons:
iPhone4/5: 114 x 114
iPhone3:    57 x  57
iPad:       72 x  72

Splash screen:
iPhone4/5:       640 x  920
iPhone3:         320 x  460
iPad Landscape: 1024 x  748
iPad Portrait:   768 x 1004


Retina images
-------------
To use the full potential of the retina screens, we should provide images in
double the resolution. The filename of these images should be the same as the
original one's, just with a '@2x' postfix (image.png and image@2x.png). Also you
need to put a 'retina' class attribute to the image tag in order for it to be
switched for retina displays.
If the image is set by CSS, there is a neat less mixin that can be used for it:

    .at2x('../images/add_icon_gray.png', 13px, 13px);


Using CSS3 properties
---------------------
Not all browsers support CSS3 yet, so we need to keep it in mind when we are
developing a new theme. Create everything with CSS2 first, and only after
enhance it with CSS3 goodness. This way browsers that do not support CSS3 will
fall back to the CSS2, and still look pretty decent.



Create a new theme with ZopeSkel
================================
To create a new theme with this ZopeSkel template, run:

    ./bin/zopeskel diazo_theme my.theme

Where my.theme is the name of your package. Answer a few questions, or just hit
enter to get the default values. Move the new package to the src folder and edit
your buildout to include the newly created package. In the buildout section add:

    develop =
        src/my.theme

And in the instance section add:

    eggs =
        my.theme

Don't forget to run the buildout after these changes.


Package content
================

  * browser
  * docs
  * locales
  * profiles
  * theme_resources
    * css - holds the generated css that is actually used by plone
    * images - holds all the images used by the theme
    * javascript - holds all the javascripts used by the theme
    * less - holds all the less files that will produce the css
        * bootstrap - Twitter Bootstrap less files
        * plone - Plone theme specific less files
        * style.less - main less file that includes all the other files in the
        appropriate places.
        * responsive.less - styles that are for responsive design
        * mixins.less - commonly used less mixins
        * variables.less - less variables for quick styling
    * index.html - main template used by plone.app.theming
    * rules.xml - rules file used by plone.app.theming
    * rules_base.xml - Diazo rules that are common to all themes
    * manifest.cfg - settings page for plone.app.theming


Setting up CodeKit
==================

Add the less folder from theme_resources to CodeKit. Select less/style.less and
less/response.less and set it's CSS Output Path to point to theme_resources/css.
Usually the output folder is set like this, so you just need to make sure this
is the case.

After each update to the files, CodeKit will recompile style.less and
responsive.less automatically, so just reload your page (if zope is in debug
mode).


New theme roll-out checklist
============================
Follow these steps for each new theme:

  * Create a new theme with zopeskel
  * Create a new git repository for the new theme
  * Update your buildout to include the new theme and run it
  * Update manifest.cfg with tablet sidebar behavior rule
  * Update registry.xml with proper portlet style names (if using
    hexagonit.portletstyle)
  * Start the server and install the new theme
  * Update index.html and rules.xml to suite your layout
  * Change the variables.less variable values to match your needs
  * Modify common elements first, and only then move to device specific ones
  * Add needed images and javascripts
  * Create launch icons and splash screens for mobile phones
  * Update print styles
  * Cross browser testing
  * Minify css with Less.app or CodeKit
