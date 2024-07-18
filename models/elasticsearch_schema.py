from abc import ABC

from constants.constants import Constants


class EsBaseModel(ABC):
    def __init__(self, id):
        self.id = id

    def self_introduce(self):
        pass


class EsTeleGroup(EsBaseModel):
    def __init__(self, id, name, description, link, member_count, tags):
        self.id = id
        self.name = name
        self.description = description
        self.link = link
        self.member_count = member_count
        self.tags = tags

    def self_introduce(self) -> str:
        return f"{Constants.TELEGROUP_IN_CHINESE} {self.name}({self.member_count}) {self.link} \n"


class EsTeleChannel(EsBaseModel):
    def __init__(self, id, name, description, link, subscriber_count, tags):
        self.id = id
        self.name = name
        self.description = description
        self.link = link
        self.subscriber_count = subscriber_count
        self.tags = tags

    def self_introduce(self) -> str:
        return f"{Constants.TELECHANNEL_IN_CHINESE} {self.name}({self.subscriber_count}) {self.link} \n"
