import os
from dotenv import load_dotenv
from google import genai
from output_parser_template.models.summarization import SummarizationResponse
from output_parser_template.models.calendar_api import CalendarAPIResponse

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_KEY")

def call_gemini_summarization(prompt: str):
    """Call Gemini API to summarize text parse output"""
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'response_schema': list[SummarizationResponse],
        },
    )

    # Use instantiated objects
    return response.parsed # List of SummarizationResponse objects: List[SummarizationResponse]

def call_gemini_calendar_api(prompt:str):
    """Call Gemini API to create google api event denifition and parse output"""
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
        config={
            'response_mime_type': 'application/json',
            'response_schema': list[CalendarAPIResponse],
        },
    )

    # Use instantiated objects
    return response.parsed # List of CalendarAPIResponse objects: List[CalendarAPIResponse]