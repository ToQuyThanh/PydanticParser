import os
from dotenv import load_dotenv
from google import genai
from output_parser_template.models.summarization import SummarizationResponse

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_KEY")

def call_gemini_summarization(prompt: str):
    """Gọi Gemini API để tóm tắt và parse output"""
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