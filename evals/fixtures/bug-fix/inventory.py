#!/usr/bin/env python3
"""Inventory pagination fixture with a deliberate off-by-one bug."""


def paginate(items, page, size):
    if page < 1 or size < 1:
        raise ValueError("page and size must be positive")
    start = page * size
    return items[start:start + size]


def page_count(items, size):
    if size < 1:
        raise ValueError("size must be positive")
    return (len(items) + size - 1) // size
