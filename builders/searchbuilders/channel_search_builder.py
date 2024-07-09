from builders.searchbuilders.base_search_builder import BaseSearchBuilder


class ChannelSearchBuilder(BaseSearchBuilder):
    def __init__(self):
        super().__init__()
        self.params["index"] = "channel"
