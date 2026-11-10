"""Schema comparison helpers."""

_COMPATIBLE = "compatible"
_RISKY = "risky"
_BREAKING = "breaking"


def compare(old, new):
    """Compare two field dictionaries and classify every change."""
    changes = {}
    for name, spec in new.items():
        previous = old.get(name)
        if previous is None:
            changes[name] = _COMPATIBLE
        elif previous.get("type") != spec.get("type"):
            changes[name] = _BREAKING
        elif previous.get("required") and not spec.get("required"):
            changes[name] = _RISKY
        else:
            changes[name] = _COMPATIBLE
    for name in old:
        if name not in new:
            changes[name] = _BREAKING
    return changes
