---
layout: workshop      # DON'T CHANGE THIS.
carpentry: ""    # what kind of Carpentry (must be either "lc" or "dc" or "swc")
venue: "Plotting and Programming with Python"
address: "Regeneron, Tarrytown, NY"
country: "us"
language: "en"
latlng: #"41.732190,-72.793431"
humandate: "June 13-14, 2019"
humantime: "9:00 am - 4:30 pm"
startdate: 2019-06-13
enddate: 2019-06-14
instructor: ["Sheldon McKay", "Pariksheet Nanda"]
helper: ["TBA"]
email: ["sheldon.mckay@regeneron.com"]
collaborative_notes: https://pad.carpentries.org/2019-06-13-python-regn
---

{% comment %} See instructions in the comments below for how to edit specific sections of this workshop template. {% endcomment %}

{% comment %}
  HEADER

  Edit the values in the block above to be appropriate for your workshop.
  If the value is not 'true', 'false', 'null', or a number, please use
  double quotation marks around the value, unless specified otherwise.
  And run 'make workshop-check' *before* committing to make sure that changes are good.
{% endcomment %}

{% comment %}
  EVENTBRITE

  This block includes the Eventbrite registration widget if
  'eventbrite' has been set in the header.  You can delete it if you
  are not using Eventbrite, or leave it in, since it will not be
  displayed if the 'eventbrite' field in the header is not set.
{% endcomment %}
{% if page.eventbrite %}
<iframe
  src="https://www.eventbrite.com/tickets-external?eid={{page.eventbrite}}&ref=etckt"
  frameborder="0"
  width="100%"
  height="280px"
  scrolling="auto">
</iframe>
{% endif %}

<h2 id="general">General Information</h2>

{% comment %}
  INTRODUCTION

  Edit the general explanatory paragraph below if you want to change
  the pitch.
{% endcomment %}
{% if page.carpentry == "swc" %}
  {% include sc/intro.html %}
{% elsif page.carpentry == "dc" %}
  {% include dc/intro.html %}
{% elsif page.carpentry == "lc" %}
  {% include lc/intro.html %}
{% endif %}

{% comment %}
  AUDIENCE

  Explain who your audience is.  (In particular, tell readers if the
  workshop is only open to people from a particular institution.
{% endcomment %}
{% if page.carpentry == "swc" %}
  {% include sc/who.html %}
{% elsif page.carpentry == "dc" %}
  {% include dc/who.html %}
{% elsif page.carpentry == "lc" %}
  {% include lc/who.html %}
{% endif %}

{% comment %}
  LOCATION

  This block displays the address and links to maps showing directions
  if the latitude and longitude of the workshop have been set.  You
  can use https://itouchmap.com/latlong.html to find the lat/long of an
  address.
{% endcomment %}
{% if page.latlng %}
<p id="where">
  <strong>Where:</strong>
  {{page.address}}.
  Get directions with
  <a href="//www.openstreetmap.org/?mlat={{page.latlng | replace:',','&mlon='}}&zoom=16">OpenStreetMap</a>
  or
  <a href="//maps.google.com/maps?q={{page.latlng}}">Google Maps</a>.
</p>
{% endif %}

{% comment %}
  DATE

  This block displays the date and links to Google Calendar.
{% endcomment %}
{% if page.humandate %}
<p id="when">
  <strong>When:</strong>
  {{page.humandate}}.
  {% include workshop_calendar.html %}
</p>
{% endif %}

{% comment %}
  SPECIAL REQUIREMENTS

  Modify the block below if there are any special requirements.
{% endcomment %}
<p id="requirements">
  <strong>Requirements:</strong> Participants must bring a laptop with Chrome or Firefox installed.
  Tablets,  Chromebook, etc. are not supported
  <a href="#setup">below</a>). They are also required to abide by
  {% if page.carpentry == "swc" %}
  Software Carpentry's
  {% elsif page.carpentry == "dc" %}
  Data Carpentry's
  {% elsif page.carpentry == "lc" %}
  Library Carpentry's
  {% endif %}
  <a href="{{site.swc_site}}/conduct.html">Code of Conduct</a>.
</p>

{% comment %}
  ACCESSIBILITY

  Modify the block below if there are any barriers to accessibility or
  special instructions.
{% endcomment %}
<p id="accessibility">
  <strong>Accessibility:</strong> We are committed to making this workshop
  accessible to everybody.
  The workshop organizers have checked that:
</p>
<ul>
  <li>The room is wheelchair / scooter accessible.</li>
  <li>Accessible restrooms are available.</li>
</ul>
<p>
  Materials will be provided in advance of the workshop and
  large-print handouts are available if needed by notifying the
  organizers in advance.  If we can help making learning easier for
  you (e.g. sign-language interpreters, lactation facilities) please
  get in touch (using contact details below) and we will
  attempt to provide them.
</p>

{% comment %}
  CONTACT EMAIL ADDRESS

  Display the contact email address set in the configuration file.
{% endcomment %}
<p id="contact">
  <strong>Contact</strong>:
  Please email
  {% if page.email %}
    {% for email in page.email %}
      {% if forloop.last and page.email.size > 1 %}
        or
      {% else %}
        {% unless forloop.first %}
        ,
        {% endunless %}
      {% endif %}
      <a href='mailto:{{email}}'>{{email}}</a>
    {% endfor %}
  {% else %}
    to-be-announced
  {% endif %}
  for more information.
</p>

<hr/>


<!--<tr> <td>15:15</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/11-lists/">Lists</a></td> </tr>-->

<h2 id="schedule">Schedule</h2>

<div class="row">
  <div class="col-md-6">
   <h3>Thursday, June 13 Sheldon</h3>
     <table class="table table-striped">
      <tr> <td>9:00</td> <td>Workshop overview</td></tr>
      <tr> <td>9:15</td> <td>Introduction to the unix shell</td></tr>
      <tr> <td>10:30</td>  <td>Coffee</td> </tr>
      <tr> <td>10:45</td> <td>Introduction to the unix shell (Cont'd)</td></tr>
      <tr> <td>11:30</td><td>Best practices for programming at Regeneron</td>
      <tr> <td>12:00</td><td>Lunch</td>
      <tr> <td>13:00</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/">Workshop Overview</a></td> </tr>
      <tr> <td>13:30</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/01-run-quit/">Running and Quitting</a></td> </tr>
      <tr> <td>13:45</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/02-variables/">Variables and Assignment</a></td> </tr>
      <tr> <td>14:05</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/03-types-conversion/">Data Types and Type Conversion</a></td> </tr>
      <tr> <td>14:30</td>  <td>Coffee</td> </tr>
      <tr> <td>14:45</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/04-built-in/">Built-in Functions and Help</a></td> </tr>
      <tr> <td>15:15</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/06-libraries/">Libraries</a></td> </tr>
      <tr> <td>16:05</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/07-reading-tabular/">Reading Tabular into DataFrames</a></td></tr>
      <tr> <td>16:30</td>  <td>Wrap-up</td> </tr>
     </table>
  </div>
  <div class="col-md-6">
    <h3>Friday, June 14</h3>
    <table class="table table-striped">
      <tr> <td>9:00</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/08-data-frames/">Pandas DataFrames</a></td> </tr>
      <tr> <td>9:30</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/09-plotting/">Plotting</a></td> </tr>
      <tr> <td>10:30</td>  <td>Coffee</td> </tr>
      <tr> <td>10:45</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/11-lists/">Lists</a></td> </tr>
      <tr> <td>11:15</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/12-for-loops/">For Loops</a></td> </tr>
      <tr> <td>12:00</td>  <td>Lunch</td> </tr>
      <tr> <td>13:00</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/13-looping-data-sets/">Looping Over Data Sets</a> </td> </tr>
      <tr> <td>13:30</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/14-writing-functions/">Writing Functions</a> </td> </tr>
      <tr> <td>14:30</td>  <td>Coffee</td> </tr>
      <tr> <td>14:45</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/15-scope/">Variable Scope</a> </td> </tr>
      <tr> <td>15:15</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/17-conditionals/">Conditionals</a> </td> </tr>
      <tr> <td>15:45</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/18-style/">Programming Style</a> </td> </tr>
      <tr> <td>16:15</td>  <td>Wrap-up</td> </tr>
      <tr> <td>16:30</td>  <td>End</td> </tr>
    </table>
  </div>
</div>

{% comment %}
  Collaborative Notes

  If you want to use an Etherpad, go to

      http://pad.software-carpentry.org/YYYY-MM-DD-site

  where 'YYYY-MM-DD-site' is the identifier for your workshop,
  e.g., '2015-06-10-esu'.
{% endcomment %}
{% if page.collaborative_notes %}
<p id="collaborative_notes">
  We will use this <a href="{{page.collaborative_notes}}">collaborative document</a> for chatting, taking notes, and sharing URLs and bits of code.
</p>
{% endif %}

<hr/>

{% comment %}
  SYLLABUS

  Show what topics will be covered.

  1. If your workshop is R rather than Python, remove the comment
     around that section and put a comment around the Python section.
  2. Some workshops will delete SQL.
  3. Please make sure the list of topics is synchronized with what you
     intend to teach.
  4. You may need to move the div's with class="col-md-6" around inside
     the div's with class="row" to balance the multi-column layout.

  This is one of the places where people frequently make mistakes, so
  please preview your site before committing, and make sure to run
  'tools/check' as well.
{% endcomment %}
<h2 id="syllabus">Syllabus</h2>

<table class="table table-striped">
<div class="col-md-6">
<h3 id="syllabus-python">Programming in Python</h3>
<ul>
<li>Using libraries</li>
<li>Working with arrays</li>
<li>Reading and plotting data</li>
<li>Creating and using functions</li>
<li>Loops and conditionals</li>
<li>Defensive programming</li>
<li>Using Python from the command line</li>
<li><a href="{{site.swc_pages}}/python-novice-inflammation/reference/">Reference...</a></li>
</ul>
</div>
</table>


<hr/>

{% comment %}
  SETUP

  Delete irrelevant sections from the setup instructions.  Each
  section is inside a 'div' without any classes to make the beginning
  and end easier to find.

  This is the other place where people frequently make mistakes, so
  please preview your site before committing, and make sure to run
  'tools/check' as well.
{% endcomment %}

<h2 id="setup">Setup</h2>

<p>
  To participate in a
  {% if page.carpentry == "swc" %}
  Software Carpentry
  {% elsif page.carpentry == "dc" %}
  Data Carpentry
  {% elsif page.carpentry == "lc" %}
  Library Carpentry
  {% endif %}
  workshop,
  you will need access to the software described below.
  In addition, you will need an up-to-date web browser.
</p>


<div id="python"> 
    <p>
      We will teach all sections of this workshop using the <a href="https://jupyter.org/">Jupyter notebook</a>,
      a programming environment that runs in a web browser. For this to work you will need a reasonably
      up-to-date browser. The current versions of the Chrome, Safari and Firefox browsers are all
      <a href="https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#browser-compatibility">supported</a>
      (some older browsers, including Internet Explorer version 9
      and below, are not).
    </p>

    <p>
    To access Jupyter notebook, point your browser to https://jupyterhub.regeneron.regn.com and log in with your regeneron credentials
    </p>
</div> {% comment %} End of 'Python' section. {% endcomment %}
