import pytest
from output_parser_template.models.base import LLMResponseBase
from pydantic import ValidationError

def test_llm_response_valid():
    """Test tạo instance hợp lệ của LLMResponseBase"""
    data = {
        "text": "Hello, world!",
        "token_used": 10,
        "model": "gpt-4",
        "metadata": {"temperature": 0.7},
    }
    response = LLMResponseBase(**data)
    
    assert response.text == "Hello, world!"
    assert response.token_used == 10
    assert response.model == "gpt-4"
    assert response.metadata == {"temperature": 0.7}

def test_llm_response_default_values():
    """Test giá trị mặc định khi thiếu field"""
    data = {"text": "Test text"}
    response = LLMResponseBase(**data)

    assert response.text == "Test text"
    assert response.token_used == 1000
    assert response.model == "unknown"
    assert response.metadata == {}

def test_llm_response_invalid_type():
    """Test lỗi ValidationError khi truyền sai kiểu dữ liệu"""
    with pytest.raises(ValidationError):
        LLMResponseBase(
            text="Invalid Test",
            token_used="not a number",
            model="gpt-4",
            metadata={}
        )
