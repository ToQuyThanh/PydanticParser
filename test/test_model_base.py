import pytest
from output_parser_template.models.base import LLMResponseBase
from pydantic import ValidationError

def test_llm_response_valid():
    """Test create valid instance of LLMResponseBase"""
    data = {
        "text": "Hello, world!",
        "token_used": 10,
        "model": "gpt-4",
        "metadata": {"temperature": 0.7},
    }
    response = LLMResponseBase(**data)
    
    assert response.text == "Hello, world!"

def test_llm_response_invalid_type():
    """Test ValidationError"""
    with pytest.raises(ValidationError):
        LLMResponseBase(
            text=1
        )
