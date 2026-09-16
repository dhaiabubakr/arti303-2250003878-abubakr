"""Utilities for cleaning student names."""

def clean_name(raw):

    """Clean a name by collapsing whitespace and title-casing it."""

    return " ".join(raw.split()).title()
