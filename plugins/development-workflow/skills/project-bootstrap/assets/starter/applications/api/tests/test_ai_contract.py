import pytest
from pydantic import ValidationError

from notes.ai import validate_summary


def test_model_output_contract():
    assert (
        validate_summary('{"summary":"Synthetic note","tags":["idea"]}').summary == "Synthetic note"
    )
    with pytest.raises(ValidationError):
        validate_summary('{"summary":"","tags":[]}')
    with pytest.raises(ValidationError):
        validate_summary("not JSON")
