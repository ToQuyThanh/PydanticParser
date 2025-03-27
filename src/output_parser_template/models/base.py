from pydantic import BaseModel, Field, ConfigDict
from typing import List, Dict, Any, Optional

class LLMResponseBase(BaseModel):
    """ Base class for LLM response """

    text: str = Field(..., title="Generated text", description="The generated text")

    model_config = ConfigDict(arbitrary_types_allowed=True)