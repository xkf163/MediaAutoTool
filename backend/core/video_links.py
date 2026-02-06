# 视频链接管理模块

class VideoLinksManager:
    def __init__(self):
        self.video_links = []  # 存储视频链接

    def add_link(self, link):
        if link not in self.video_links:
            self.video_links.append(link)
            return True  # 添加成功
        return False  # 链接已经存在

    def remove_link(self, link):
        if link in self.video_links:
            self.video_links.remove(link)
            return True  # 删除成功
        return False  # 链接不存在

    def list_links(self):
        return self.video_links  # 返回所有链接