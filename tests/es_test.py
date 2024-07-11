from builders.searchbuilders.channel_search_builder import ChannelSearchBuilder, BaseSearchBuilder
from services.elastic_service import ElasticService
from constants.constants import ElasticIndices

if __name__ == '__main__':
    search_builder = BaseSearchBuilder()
    search_builder.keywords(["原味"], ["name", "description"])
    es_service = ElasticService()
    resp = es_service.search(search_builder, index=[ElasticIndices.CHANNEL, ElasticIndices.GROUP])
    respBody = resp.body
    hits = respBody["hits"]
    total = hits["total"]["value"]
    hitDatum = hits["hits"]
    print(total)
    for hitData in hitDatum:
        index_name = hitData["_index"]
        data_source = hitData["_source"]
