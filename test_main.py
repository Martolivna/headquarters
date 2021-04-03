import pytest

from main import json_dumps


def test_json_dumps():
    assert json_dumps({"asd": "qwe"}) == '{"asd": "qwe"}'
