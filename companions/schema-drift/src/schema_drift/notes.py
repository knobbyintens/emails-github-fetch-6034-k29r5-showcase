"""Human-readable migration notes."""


def note(name, change):
    """Return a one-line migration note for a classified change."""
    if change == "breaking":
        return f"`{name}` changes in a breaking way; coordinate a release."
    if change == "risky":
        return f"`{name}` becomes optional; downstream defaults must be reviewed."
    return f"`{name}` is a compatible change."
