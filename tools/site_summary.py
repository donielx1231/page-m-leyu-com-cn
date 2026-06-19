class SiteSummary:
    def __init__(self):
        self.site_data = [
            {
                "name": "乐鱼体育门户",
                "url": "https://page-m-leyu.com.cn",
                "keywords": ["乐鱼体育", "体育赛事", "在线娱乐"],
                "tags": ["体育", "娱乐", "门户"],
                "description": "提供丰富的体育赛事资讯和综合娱乐服务"
            },
            {
                "name": "乐鱼资讯",
                "url": "https://page-m-leyu.com.cn/news",
                "keywords": ["乐鱼体育", "新闻", "赛事动态"],
                "tags": ["新闻", "体育", "资讯"],
                "description": "实时更新体育新闻与行业动态"
            },
            {
                "name": "乐鱼社区",
                "url": "https://page-m-leyu.com.cn/community",
                "keywords": ["乐鱼体育", "社区", "互动"],
                "tags": ["社区", "社交", "体育"],
                "description": "用户交流与分享的互动平台"
            }
        ]

    def format_site_summary(self, site: dict) -> str:
        keywords = ", ".join(site["keywords"])
        tags = ", ".join(site["tags"])
        return (
            f"站点名称：{site['name']}\n"
            f"URL：{site['url']}\n"
            f"关键词：{keywords}\n"
            f"标签：{tags}\n"
            f"简介：{site['description']}\n"
        )

    def generate_all_summaries(self) -> str:
        lines = []
        for site in self.site_data:
            lines.append(self.format_site_summary(site))
            lines.append("-" * 40)
        return "\n".join(lines)

    def print_summaries(self):
        output = self.generate_all_summaries()
        print(output)

    def get_summary_as_dict(self, site: dict) -> dict:
        return {
            "name": site["name"],
            "url": site["url"],
            "keywords": site["keywords"],
            "tags": site["tags"],
            "description": site["description"]
        }

    def list_all_names(self) -> list:
        return [site["name"] for site in self.site_data]

    def find_by_keyword(self, keyword: str) -> list:
        results = []
        for site in self.site_data:
            if keyword.lower() in [k.lower() for k in site["keywords"]]:
                results.append(site)
        return results


def main():
    summary = SiteSummary()
    print("====== 站点资料结构化摘要 ======\n")
    summary.print_summaries()

    print("\n所有站点名称：")
    for name in summary.list_all_names():
        print(f" - {name}")

    search_term = "乐鱼体育"
    found = summary.find_by_keyword(search_term)
    if found:
        print(f"\n包含关键词 '{search_term}' 的站点：")
        for site in found:
            print(f"   → {site['name']} ({site['url']})")
    else:
        print(f"\n未找到包含关键词 '{search_term}' 的站点。")


if __name__ == "__main__":
    main()