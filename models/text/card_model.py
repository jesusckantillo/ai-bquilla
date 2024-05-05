from pydantic import BaseModel

from typing import List

class TextCard(BaseModel):
    translations: str =""
    pronuntations: str = ""
    examples: List[str] = []