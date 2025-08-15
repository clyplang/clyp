import random as rand
from typing import Any


def random():
    """
    Generate a random float between 0.0 and 1.0.

    Returns:
        float: A random float between 0.0 and 1.0.
    """
    return rand.random()


def seed(seed: int) -> None:
    """
    Seed the random number generator.

    Args:
        seed (int): The seed value.
    """
    rand.seed(seed)


def randint(a: int, b: int) -> int:
    """
    Generate a random integer between a and b, inclusive.

    Args:
        a (int): The lower bound.
        b (int): The upper bound.

    Returns:
        int: A random integer between a and b, inclusive.
    """
    return rand.randint(a, b)


def choice(seq: list[Any]) -> Any:
    """
    Choose a random element from a non-empty sequence.

    Args:
        seq (Sequence[Any]): The sequence to choose from.

    Returns:
        Any: A random element from the sequence.
    """
    return rand.choice(seq)


def shuffle(seq: list[Any]) -> None:
    """
    Shuffle the elements of a list in place.

    Args:
        seq (list[Any]): The list to shuffle.
    """
    rand.shuffle(seq)


def uniform(a: float, b: float) -> float:
    """
    Generate a random float between a and b.

    Args:
        a (float): The lower bound.
        b (float): The upper bound.

    Returns:
        float: A random float between a and b.
    """
    return rand.uniform(a, b)


def randfloat(a: float, b: float) -> float:
    """
    Generate a random float between a and b (inclusive).

    Args:
        a (float): The lower bound.
        b (float): The upper bound.

    Returns:
        float: A random float between a and b (inclusive).
    """
    return rand.uniform(a, b)


def sample(seq: list[Any], k: int) -> list[Any]:
    """
    Return a k length list of unique elements chosen from the sequence.

    Args:
        seq (list[Any]): The sequence to choose from.
        k (int): The number of elements to choose.

    Returns:
        list[Any]: A list of k unique elements from the sequence.
    """
    return rand.sample(seq, k)


__all__ = [
    "random",
    "seed",
    "randint",
    "choice",
    "shuffle",
    "uniform",
    "randfloat",
    "sample",
]
