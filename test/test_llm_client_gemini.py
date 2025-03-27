import pytest
from output_parser_template.llm_clients.gemini_calls import call_gemini_summarization  # Thay your_module bằng tên file thực
from output_parser_template.models.summarization import SummarizationResponse  # Import model tương ứng

def test_call_gemini_summarization():
    # Prompt test
    prompt = "Test summary"

    # Call funcion
    result = call_gemini_summarization(prompt)

    # Validate result
    assert isinstance(result, list)  # Output must be a list
    assert len(result) > 0  # Output must be has a element at least
    assert isinstance(result[0], SummarizationResponse)  # Element must be SummarizationResponse
    assert hasattr(result[0], "summary")  # Element must have summary
    assert isinstance(result[0].summary, str)  # Summary is string
    assert len(result[0].summary) > 0  # Summary is not empty string
