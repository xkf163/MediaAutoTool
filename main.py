#!/usr/bin/env python3
"""MediaAutoTool CLI entry point."""

from __future__ import annotations

import argparse

from backend.core.video_links import VideoLinksManager


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="MediaAutoTool 视频链接管理工具")
    parser.add_argument(
        "--storage",
        default="inputs/video_links.json",
        help="保存视频链接的文件路径",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="列出所有视频链接")

    add_parser = subparsers.add_parser("add", help="添加视频链接")
    add_parser.add_argument("link", help="要添加的视频链接")

    remove_parser = subparsers.add_parser("remove", help="删除视频链接")
    remove_parser.add_argument("link", help="要删除的视频链接")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    manager = VideoLinksManager(storage_path=args.storage)

    if args.command == "list":
        for link in manager.list_links():
            print(link)
        return

    if args.command == "add":
        if manager.add_link(args.link):
            print("链接已添加。")
        else:
            print("链接无效或已存在。")
        return

    if args.command == "remove":
        if manager.remove_link(args.link):
            print("链接已删除。")
        else:
            print("链接不存在。")
        return


if __name__ == "__main__":
    main()
