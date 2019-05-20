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
</p>
{% endif %}

{% comment %}
  SPECIAL REQUIREMENTS

  Modify the block below if there are any special requirements.
{% endcomment %}
<p id="requirements">
  <strong>Requirements:</strong> Participants must bring a laptop with Chrome or Firefox installed.
  Tablets,  Chromebook, etc. are not supported.
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
    <h3>Thursday, June 13</h3>
    <table class="table table-striped">
      <tr> <td>9:00</td> <td>Workshop overview</td></tr>
      <tr> <td>9:10</td> <td><a href="{{site.swc_pages}}/shell-novice/01-intro/">Introduction to the unix shell</a></td></tr>
      <tr> <td>9:15</td> <td><a href="{{site.swc_pages}}/shell-novice/02-filedir">Navifating files and directories</a></td></tr>
      <tr> <td>9:50</td> <td><a href="{{site.swc_pages}}/shell-novice/03-create">Working with files and directories</a></td></tr>
      <tr> <td>10:30</td> <td>Coffee</td> </tr>
      <tr> <td>10:45</td> <td><a href="{{site.swc_pages}}/shell-novice/04-pipefilter">Pipes and filters</a></td></tr>
      <tr> <td>11:05</td> <td><a href="{{site.swc_pages}}/shell-novice/05-loop">Loops</a></td></tr>
      <tr> <td>11:45</td> <td>Best practices for programming at Regeneron</td></tr>
      <tr> <td>12:00</td> <td>Lunch</td></tr>
      <tr> <td>13:00</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/">Python Overview</a></td> </tr>
      <tr> <td>13:15</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/01-run-quit/">Running and Quitting</a></td> </tr>
      <tr> <td>13:35</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/02-variables/">Variables and Assignment</a></td> </tr>
      <tr> <td>13:55</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/03-types-conversion/">Data Types and Type Conversion</a></td> </tr>
      <tr> <td>14:30</td>  <td>Coffee</td> </tr>
      <tr> <td>14:45</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/04-built-in/">Built-in Functions and Help</a></td> </tr>
      <tr> <td>15:15</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/06-libraries/">Libraries</a></td> </tr>
      <tr> <td>16:05</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/07-reading-tabular/">Reading Tabular Data into DataFrames</a></td></tr>
      <tr> <td>16:30</td>  <td>Wrap-up</td> </tr>
    </table>
  </div>
  <div class="col-md-6">
    <h3>Friday, June 14</h3>
    <table class="table table-striped">
      <tr> <td>9:00</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/08-data-frames/">Pandas DataFrames</a></td> </tr>
      <tr> <td>9:45</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/09-plotting/">Plotting</a></td> </tr>
      <tr> <td>10:30</td>  <td>Coffee</td> </tr>
      <tr> <td>10:45</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/11-lists/">Lists</a></td> </tr>
      <tr> <td>11:15</td>  <td><a href="{{site.swc_pages}}/python-novice-gapminder/12-for-loops/">For Loops</a></td> </tr>
      <tr> <td>12:00</td> <td>Lunch</td></tr>
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

<div class="row">
  <div class="col-md-6">
    <h3 id="syllabus-shell">The Unix Shell</h3>
    <ul>
      <li>Files and directories</li>
      <li>History and tab completion</li>
      <li>Pipes and redirection</li>
      <li>Looping over files</li>
      <li>Creating and running shell scripts</li>
      <li>Finding things</li>
      <li><a href="{{site.swc_pages}}/shell-novice/reference">Reference...</a></li>
    </ul>
  </div>
  <div class="col-md-6">
    <h3 id="syllabus-python">Programming in Python</h3>
    <ul>
      <li>Using libraries</li>
      <li>Working with arrays</li>
      <li>Reading, transforming and plotting data</li>
      <li>Creating and using functions</li>
      <li>Loops and conditionals</li>
      <li><a href="{{site.swc_pages}}/python-novice-gapminder/reference">Reference...</a></li>
    </ul>
  </div>
</div>

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
<div id="python"> 
  <ul>
    <li>
      We will teach all sections of this workshop using the <a href="https://jupyter.org/">Jupyter notebook</a>,
      a programming environment that runs in a web browser. 
    </li>
    <li>
      The current versions of the Chrome, Safari and Firefox browsers are all
      <a href="https://jupyter-notebook.readthedocs.io/en/stable/notebook.html#browser-compatibility">supported</a>
    </li>
    <li>
      To access Jupyter notebook, point your browser to <a href="https://jupyterhub.regeneron.regn.com">jupyterhub.regeneron.regn.com</a> and log in with your Regeneron credentials
    </li>
  </ul>
</div> {% comment %} End of 'Python' section. {% endcomment %}
