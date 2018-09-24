{% extends "base.html" %}

{% block content %}

  <div class='jumbotron'>

    <h1>let's check your username</h1>

    {% if end_result %}
        <p>your username is correct!</p>
        {% else %}
          <ul>
            {% if not upper %}
              <li>your username miss uppercase</li>
            {% endif %}
            {% if not lower %}
              <li>your username miss lowercase</li>
            {% endif %}
            {% if not num_end %}
              <li>your username miss number at the end</li>
            {% endif %}
          </ul>
      {% endif %}

{% endblock %}
