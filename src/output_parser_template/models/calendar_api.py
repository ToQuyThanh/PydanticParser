from pydantic import BaseModel, Field
from output_parser_template.models.base import LLMResponseBase
from typing import Optional


class Time(BaseModel):
    dateTime: str = Field(description="Time value ISO 8601 datetime format")
    timeZone: str = Field(description="Time zone value e.g: America/Los_Angeles")

class CalendarAPIResponse(LLMResponseBase):
    """ Response class for summarization """
    
    summary: str = Field(..., title="Summary", description="The generated summary to use as a title of calendar")
    description: Optional[str] = Field(description='A short description of event as list to track')
    startTime: Time = Field(description='Time start')
    endTime: Time = Field(description='Time end')

