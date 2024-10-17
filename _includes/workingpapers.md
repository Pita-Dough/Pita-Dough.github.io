<h2 id="workingpapers" style="margin: 2px 0px -15px;">Working Papers</h2>

<div class="publications">
<ol class="bibliography">

{% for link in site.data.workingpapers.main %}

<li>
  <!---
<div class="pub-row">
  <div class="col-sm-3 abbr" style="position: relative;padding-right: 15px;padding-left: 15px;">
    {% if link.image %} 
    <img src="{{ link.image }}" class="teaser img-fluid z-depth-1" style="width=100;height=40%">
    {% endif %}
    {% if link.conference_short %} 
    <abbr class="badge">{{ link.conference_short }}</abbr>
    {% endif %}
  </div>
  -->
  <div class="col-sm-9" style="position: relative;padding-right: 0px;padding-left: 0px;">
      <div class="title"><a>{{ link.title }}</a></div>
      <div class="author">{{ link.authors }}</div>
      <div class="periodical"><em>{{ link.conference }}</em>
      </div>
    <div class="links">
      {% if link.abstract %} 
      <a >
      <button class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;border:1px solid #2086c9;color:#2086c9;background-color:#fffaf2;cursor:pointer" id="toggleButton{{ forloop.index }}" >
      Abstract <i class='fas fa-chevron-down' style='font-size:12px;color:#2086c9;background-color:#fffaf2;'></i>
      </button> 
      </a>
      {% endif %}
      {% if link.pdf %} 
      <a href="{{ link.pdf }}" style="cursor:pointer"><button  class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;border:1px solid #2086c9;cursor:pointer;color:#2086c9;background-color:#fffaf2;">PDF</button></a>
      {% endif %}
      {% if link.arXiv %} 
      <a href="{{ link.arXiv }}" style="cursor:pointer"><button  class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;border:1px solid #2086c9;cursor:pointer;color:#2086c9;background-color:#fffaf2;">arXiv</button></a>
      {% endif %}
      {% if link.code %} 
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Code</a>
      {% endif %}
      {% if link.mathematica %} 
      <a href="{{ link.mathematica }}" style="cursor:pointer"><button  class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;border:1px solid #2086c9;cursor:pointer;color:#2086c9;background-color:#fffaf2;">Mathematica Notebook</button></a>
      {% endif %}
      {% if link.page %} 
      <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Project Page</a>
      {% endif %}
      {% if link.bibtex %} 
      <a href="{{ link.bibtex }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">BibTex</a>
      {% endif %}
      {% if link.notes %} 
      <strong> <i style="color:#e74d3c">{{ link.notes }}</i></strong>
      {% endif %}
      {% if link.others %} 
      {{ link.others }}
      {% endif %}
    </div>
    <div class="collapsible" id="toggleBlock{{ forloop.index }}" align="justify"><p>{{ link.abstract }}</p></div>
    <!---
  </div>
    -->
</div>
</li>
{% endfor %}

</ol>
</div>
