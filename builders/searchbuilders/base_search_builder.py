class BaseSearchBuilder:
    def __init__(self):
        self.params = {
            # "index": "channel",
            "body": {
                "track_total_hits": True,  # 设置最大可索引数量
                "query": {
                    "bool": {
                        "filter": [],
                        "must": [],  # 所有的语句必须 (must) 匹配,与 AND 等价
                        "must_not": [],  # 所有的语都不能 (must no) 与匹配,与 NO 等价
                        "should": [],  # 至少 (or) 有一个语句要匹配,与 OR 等价
                    }
                }
            }
        }

    def keywords(self, worlds: list[str], weights=[]):
        if not worlds:
            return self
        for word in worlds:
            self.params["body"]["query"]["bool"]["must"].append({
                "multi_match": {
                    "query": word,
                    "fields": weights,
                }
            })
        return self

    def must_not(self, filed, value):
        self.params['body']['query']['bool']['must_not'].append([{
            "team": {filed: value}
        }])
        return self

    def paginate(self, page, page_size=10):
        self.params["body"]["from"] = (page - 1) * page_size
        self.params["body"]["size"] = page_size
        return self

    def order_by(self, field, direction):
        return self

    def get_params(self):
        return self.params
