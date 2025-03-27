from pydantic import Field
from output_parser_template.models.base import LLMResponseBase

class SummarizationResponse(LLMResponseBase):
    """ Response class for summarization """
    
    summary: str = Field(..., title="Summary", description="The generated summary")
