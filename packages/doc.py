"""
doc.api
~~~~~~~~~~~~

:hoge
:huga
"""


def Parameters(x: int, y: float):
    """Short Summary

    Parameters
    ----------
    x: int
        説明
    y: float
        説明
    """


def Returns() -> int:
    """Short Summary

    Returns
    -------
    int
        説明
    """
    ...


def Raises():
    """Short Summary

    Raises
    -------
    RuntimeError
        説明
    """
    ...


def SeeAlso():
    """Short Summary

    See Also
    --------
    hoge: 説明
    """
    ...


def Notes():
    """Short Summary

    Notes
    -----
    説明
    """
    ...


def Examples():
    """Short Summary

    Examples
    --------
    >>> Examples()
    None
    """
    ...


class Attributes:
    """Short Summary

    Attributes
    ----------
    x:int
        説明
    y: float
        説明
    """
    ...


class Methods:
    """Short Summary

    Methods
    -------
    f(n: int) -> None
        説明
    g(s: str = "default") -> int
        説明
    """


def link_internal():
    """
    Short Summary

    .. _label_name:


    Notes
    -----
    :ref:`label_name`
    """
    ...


def link_external():
    """Short Summary

    直接指定は `google <https://www.google.com/>`_．
    間接指定は `google2`_

    .. _google2: https://www.google.com/
    """
    ...
