from abc import ABC, abstractmethod
from typing import Protocol


class TextPreprocessInPort(Protocol):
    """
    댓글/설명 텍스트 전처리를 요청하는 입력 포트.
    웹/배치/기타 어댑터에서 이 인터페이스만 의존.
    """

    def preprocess_comment(self, raw_comment: str) -> str:
        ...

    def preprocess_description(self, raw_description: str) -> str:
        ...
