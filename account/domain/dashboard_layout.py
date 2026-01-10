from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class DashboardLayout:
    """계정별 대시보드 레이아웃 도메인 모델"""
    account_id: int
    widgets: Any  # JSON 데이터 (프론트엔드 위젯 목록)
    layouts: Any  # JSON 데이터 (react-grid-layout 레이아웃)
    id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
