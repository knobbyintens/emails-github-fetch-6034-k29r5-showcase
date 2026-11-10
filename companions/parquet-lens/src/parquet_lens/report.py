"""Report rendering."""

import json


def render(columns):
    """Render a profiling result as a compact JSON document."""
    return json.dumps({"columns": columns}, indent=2, sort_keys=True)
