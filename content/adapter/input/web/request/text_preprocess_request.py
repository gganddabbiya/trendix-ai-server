from pydantic import BaseModel


class TextPreprocessRequest(BaseModel):
    content_id: str
    text_type: str  # "comment" or "description"
    text: str
