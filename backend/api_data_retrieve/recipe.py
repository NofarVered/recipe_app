from pydantic import BaseModel
from typing import Union, List


class Recipe(BaseModel):
    title: Union[str, None] = None
    thumbnail: Union[str, None] = None
    href: Union[str, None] = None
    ingredients: Union[List[str], None] = None
