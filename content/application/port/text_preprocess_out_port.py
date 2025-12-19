from abc import ABC, abstractmethod


class TextPreprocessOutPort(ABC):
    """
    전처리된 텍스트를 AI 분석 파이프라인에 전달하는 출력 포트.
    (예: OpenAI, 내부 추천 엔진, 감성 분석 서비스 등)
    """

    @abstractmethod
    def send_to_ai_pipeline(self, cleaned_text: str, meta: dict | None = None) -> None:
        """
        cleaned_text: 전처리된 텍스트
        meta: 컨텐츠 ID, 사용자 ID 등 메타데이터
        """
        raise NotImplementedError
