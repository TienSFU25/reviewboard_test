This is in test_template.py
{% set summary = review_request.summary %}
{% set description = review_request.description %}
{% set testing_done = review_request.testing_done %}

{% if not description.startswith(summary) %}
{{summary}}


{% endif %}
{{description}}


{% if testing_done%}
Testing Done:
{{testing_done}}


{% endif %}
{% if review_request.bugs_closed%}
Bugs closed:
{{review_request.bugs_closed|join(', ')}}


{% endif %}
Reviewed at
{{review_request.absolute_url}}
