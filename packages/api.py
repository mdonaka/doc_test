"""
doc.api
~~~~~~~~~~~~

:hoge
:huga
"""


def gcd(a: int, b: int) -> int:
    """受け取った2つの整数の最大公約数を計算する．

    32bit以下の整数を受け取り，最大公約数を計算する．
    全てのパターンをcacheしており，O(1)で計算されることを保証する．
    32bitより大きい整数を渡した場合はnot hackerな人材として解雇となる．

    Parameters
    -----------
    a: int
            32bitの整数
    b: int
            32bitの整数

    Returns
    --------
    int
            aとbの最大公約数

    Raises
    -------
    RuntimeError
            入力a,bのいずれかが32bitを超える整数である時

    Examples
    ---------
    >>> gcd(24, 32)
    12
    """
    ...


def gcd2(a: int, b: int) -> int:
    """受け取った2つの整数の最大公約数を計算する．

    32bit以下の整数を受け取り，最大公約数を計算する．
    全てのパターンをcacheしており，O(1)で計算されることを保証する．
    32bitより大きい整数を渡した場合はnot hackerな人材として解雇となる．

    Parameters
    -----------
    a: int
            32bitの整数
    b: int
            32bitの整数

    Returns
    --------
    int
            aとbの最大公約数

    Raises
    -------
    RuntimeError
            入力a,bのいずれかが32bitを超える整数である時

    Examples
    ---------
    >>> gcd(24, 32)
    12
    """
    ...
