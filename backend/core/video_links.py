# 视频链接管理模块
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse


class VideoLinksManager:
    def __init__(self, storage_path: str | Path | None = None) -> None:
        self.storage_path = Path(storage_path) if storage_path else Path("inputs/video_links.json")
        self.video_links: list[str] = []
        self.load_links()

    def _normalize(self, link: str) -> str:
        return link.strip()

    def is_valid_link(self, link: str) -> bool:
        parsed = urlparse(link)
        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)

    def load_links(self) -> None:
        if not self.storage_path.exists():
            return
        try:
            data = json.loads(self.storage_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return
        if not isinstance(data, list):
            return
        cleaned_links = []
        for item in data:
            if not isinstance(item, str):
                continue
            normalized = self._normalize(item)
            if normalized and self.is_valid_link(normalized):
                cleaned_links.append(normalized)
        self.video_links = cleaned_links

    def save_links(self) -> None:
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self.storage_path.write_text(
            json.dumps(self.video_links, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def add_link(self, link: str) -> bool:
        normalized = self._normalize(link)
        if not normalized or not self.is_valid_link(normalized):
            return False
        if normalized not in self.video_links:
            self.video_links.append(normalized)
            self.save_links()
            return True  # 添加成功
        return False  # 链接已经存在

    def remove_link(self, link: str) -> bool:
        normalized = self._normalize(link)
        if normalized in self.video_links:
            self.video_links.remove(normalized)
            self.save_links()
            return True  # 删除成功
        return False  # 链接不存在

    def list_links(self) -> list[str]:
        return list(self.video_links)  # 返回所有链接
