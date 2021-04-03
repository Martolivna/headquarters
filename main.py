def json_dumps(imp: dict) -> str:
    assert isinstance(imp, dict)
    return _json_dumps(imp)


def _dumps_list(values):
    dumped_values = [
        _json_dumps(i)
        for i in values
    ]
    s = '[' + ', '.join(dumped_values) + ']'
    return s


def _dumps_dict(values):
    dumped_values = [
        f'"{k}": {_json_dumps(v)}'
        for k, v in values.items()
    ]
    s = '{' + ', '.join(dumped_values) + '}'
    return s


def _json_dumps(value):
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, int):
        return str(value)
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, list):
        return _dumps_list(value)
    if isinstance(value, dict):
        return _dumps_dict(value)
    return 'Unk type'






