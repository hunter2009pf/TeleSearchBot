from builders.searchbuilders.channel_search_builder import ChannelSearchBuilder
from services import app_service
from services.elastic_service import ElasticService

if __name__ == '__main__':
    ElasticService.connect_es()
    channel_search_builder = ChannelSearchBuilder()
    channel_search_builder.keywords(["许东为什么还不退群"])
    channel_search_builder.paginate(5, 60)
    ElasticService.search(channel_search_builder)
