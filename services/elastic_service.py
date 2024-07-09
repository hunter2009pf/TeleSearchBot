from elasticsearch import Elasticsearch

from builders.searchbuilders.base_search_builder import BaseSearchBuilder
from config.env_paras import EnvParas


class ElasticService:
    es = None

    @classmethod
    def connect_es(cls):
        cls.es = Elasticsearch([EnvParas.ELASTIC_HOST], http_auth=(EnvParas.ELASTIC_USER, EnvParas.ELASTIC_PASSWORD),
                               timeout=3600)

        print("connect_es:", cls.es)

    @classmethod
    def search(cls, search_builder: BaseSearchBuilder):
        print("es search method call:", search_builder.get_params())
