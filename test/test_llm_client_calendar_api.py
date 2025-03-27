import pytest
from output_parser_template.llm_clients.gemini_calls import call_gemini_calendar_api
from output_parser_template.models.calendar_api import CalendarAPIResponse

def test_call_gemini_calendar_api():
    """Check LLM call returns valid data"""
    prompt = "Create a Google Calendar event for a team meeting on March 30, 2025, at 10 AM."
    
    response = call_gemini_calendar_api(prompt)

    # Check response is a list of CalendarAPIResponse objects
    assert isinstance(response, list)
    assert all(isinstance(item, CalendarAPIResponse) for item in response)

    # Check some important fields in the result
    event = response[0]
    assert hasattr(event, "summary")
    assert hasattr(event, "description")
    assert hasattr(event, "startTime")
    assert hasattr(event, "endTime")

