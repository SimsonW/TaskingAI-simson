from enum import Enum
from typing import List
from pydantic import BaseModel, Field


__all__ = ["TextEmbeddingInputType", "TextEmbeddingOutput", "TextEmbeddingUsage"]


class TextEmbeddingInputType(str, Enum):
    DOCUMENT = "document"
    QUERY = "query"


class TextEmbeddingOutput(BaseModel):
    index: int = Field(..., description="The index of the embedding output.", examples=[0])
    embedding: List[float] = Field(..., description="The embedding vector.", examples=[[0.1, 0.2, 0.3, 0.4]])


class TextEmbeddingUsage(BaseModel):
    input_tokens: int = Field(
        ...,
        description="The number of tokens in the input.",
    )
