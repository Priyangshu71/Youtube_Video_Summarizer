import re
from typing import List
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.document_loaders.base import BaseLoader
from langchain.schema import Document


class YouTubeTranscriptLoader(BaseLoader):
    def __init__(self, youtube_url: str):
        self.youtube_url = youtube_url
        self.video_id = self._extract_video_id(youtube_url)

    def _extract_video_id(self, url: str) -> str:
        pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
        match = re.search(pattern, url)
        if not match:
            raise ValueError("Invalid YouTube URL")
        return match.group(1)

    def load(self) -> List[Document]:
        transcript = YouTubeTranscriptApi.get_transcript(self.video_id)
        full_text = " ".join(chunk["text"] for chunk in transcript)

        return [
            Document(
                page_content=full_text,
                metadata={
                    "source": self.youtube_url,
                    "video_id": self.video_id,
                    "type": "youtube_transcript"
                }
            )
        ]
