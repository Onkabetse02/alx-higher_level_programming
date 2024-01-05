#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevents the creation of new instance except instance attribute
    is called first_name.
    """

    __slots__ = ["first_name"]
