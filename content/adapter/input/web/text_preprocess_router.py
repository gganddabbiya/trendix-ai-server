from fastapi import APIRouter, Depends

from content.adapter.input.web.request.text_preprocess_request import TextPreprocessRequest
from content.application.usecase.text_preprocess_usecase import TextPreprocessUseCase
from content.domain.text_preprocessor import TextPreprocessor

router = APIRouter(prefix="/content/text")


def get_text_preprocess_usecase() -> TextPreprocessUseCase:
    # 실제 코드에서는 DI 컨테이너/팩토리에서 생성
    preprocessor = TextPreprocessor()
    usecase = TextPreprocessUseCase(text_preprocessor=preprocessor, out_port=None)
    return usecase


@router.post("/preprocess")
def preprocess_text(
    request: TextPreprocessRequest,
    usecase: TextPreprocessUseCase = Depends(get_text_preprocess_usecase),
):
    if request.text_type == "comment":
        cleaned = usecase.preprocess_comment(request.text)
    else:
        cleaned = usecase.preprocess_description(request.text)

    return {
        "content_id": request.content_id,
        "text_type": request.text_type,
        "cleaned_text": cleaned,
    }
