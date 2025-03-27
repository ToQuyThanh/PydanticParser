import pytest
from output_parser_template.models.summarization import SummarizationResponse
from pydantic import ValidationError

def test_llm_response_valid():
    """Test create valid instance of LLMResponseBase"""
    data = {
        "text": "Hello, world!",
        "summary": "Hello, world!",
    }
    response = SummarizationResponse(**data)
    
    assert response.text == "Hello, world!"
    assert response.summary == "Hello, world!"

def test_llm_response_invalid_type():
    """Test ValidationError"""
    with pytest.raises(ValidationError):
        SummarizationResponse(
            text=1,
            summary=1
        )
