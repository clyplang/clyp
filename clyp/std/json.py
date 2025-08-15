try:
    import orjson

    ORJSON_AVAILABLE = True
except ImportError:
    ORJSON_AVAILABLE = False

import json
from typing import Any, TextIO, List, Union


def dumps(obj: Any) -> str:
    """
    Serialize an object to a JSON-formatted string.

    Args:
        obj: The object to serialize.

    Returns:
        A JSON-formatted string.
    """
    if ORJSON_AVAILABLE:
        return orjson.dumps(obj).decode("utf-8")
    return json.dumps(obj)


def loads(s: str) -> Any:
    """
    Deserialize a JSON-formatted string to an object.

    Args:
        s: The JSON-formatted string to deserialize.

    Returns:
        The deserialized object.
    """
    if ORJSON_AVAILABLE:
        return orjson.loads(s)
    return json.loads(s)


def dump(obj: Any, fp: TextIO) -> None:
    """
    Serialize an object to a JSON-formatted stream.

    Args:
        obj: The object to serialize.
        fp: The file-like object to write the JSON data to.
    """
    json.dump(obj, fp)  # orjson does not support dumping directly to file-like objects


def load(fp: TextIO) -> Any:
    """
    Deserialize a JSON-formatted stream to an object.

    Args:
        fp: The file-like object to read the JSON data from.

    Returns:
        The deserialized object.
    """
    return json.load(fp)


def dump_jsonl(objs: List[Any], fp: TextIO) -> None:
    """
    Serialize a list of objects to a JSON Lines (jsonl) formatted stream.

    Args:
        objs: The list of objects to serialize.
        fp: The file-like object to write the JSONL data to.
    """
    for obj in objs:
        fp.write(dumps(obj) + "\n")


def load_jsonl(fp: TextIO) -> List[Any]:
    """
    Deserialize a JSON Lines (jsonl) formatted stream to a list of objects.

    Args:
        fp: The file-like object to read the JSONL data from.

    Returns:
        A list of deserialized objects.
    """
    return [loads(line) for line in fp if line.strip()]
