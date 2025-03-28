from output_parser_template.llm_clients.gemini_calls import call_gemini_calendar_free_busy
from output_parser_template.models.calendar_api import CalendarFreeBusyResponse
from typing import List

prompt = "Get free busy for the next 7 days"

responses : List[CalendarFreeBusyResponse] = call_gemini_calendar_free_busy(prompt)

for response in responses:
    print(response)