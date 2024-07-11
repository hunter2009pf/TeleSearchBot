import threading

from elasticsearch import Elasticsearch

from builders.searchbuilders.base_search_builder import BaseSearchBuilder
from config.env_paras import EnvParas


class ElasticService(object):
    _instance_lock = threading.Lock()
    _es = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(ElasticService, "_instance"):
            with ElasticService._instance_lock:
                if not hasattr(ElasticService, "_instance"):
                    ElasticService._instance = object.__new__(cls)
                    cls._es = Elasticsearch([EnvParas.ELASTIC_HOST],
                                            http_auth=(EnvParas.ELASTIC_USER, EnvParas.ELASTIC_PASSWORD),
                                            timeout=3600)
                    # print(cls._es.info())
        return ElasticService._instance

    def search(self, search_builder: BaseSearchBuilder, index=None):
        search_params = search_builder.get_params()

        return self._es.search(index=index, body=search_params.get("body"))

    def del_index(self, index, ignore):
        return self._es.delete(index=index, ignore=ignore)

    def create_index(self, index):
        return self._es.create(index=index)

    def bulk(self, index, doc_type, body):
        return self._es.bulk(index=index, body=body)

    def index(self, index, body):
        return self._es.index(index=index, body=body)
