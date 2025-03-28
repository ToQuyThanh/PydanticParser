import pytest
from output_parser_template.llm_clients.gemini_calls import call_gemini_calendar_free_busy
from output_parser_template.models.calendar_api import CalendarFreeBusyResponse
from typing import List


def test_call_gemini_calendar_free_busy():
    """Check LLM call returns valid data"""
    prompt = "Get free busy for the next 7 days."
    
    response = call_gemini_calendar_free_busy(prompt)

    # Check response is a list of CalendarAPIFreeBusy objects
    assert isinstance(response, list)
    assert all(isinstance(item, CalendarFreeBusyResponse) for item in response)

    # Check some important fields in the result
    event = response[0]
    assert hasattr(event, "text")
    assert hasattr(event, "timeMin")
    assert hasattr(event, "timeMax")
    assert hasattr(event, "timeZone")
