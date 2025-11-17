from typing import TypedDict, Union

class MediaFile(TypedDict):
    id: int
    name: str
    media_type: str
    data: Union[bytes, str]  # bytes for images/videos, str for text

class MediaInput(TypedDict):
    name: str
    media_type: str
    data: Union[bytes, str]  # bytes for images/videos, str for text

class MediaOutput(TypedDict):
    id: int
    name: str
    media_type: str
    data: Union[bytes, str]  # bytes for images/videos, str for text