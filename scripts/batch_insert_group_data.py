import json
from services.elastic_service import ElasticService
from constants.constants import ElasticIndices

if __name__ == "__main__":
    with open("scripts/data/group_example.json", "r", encoding="utf8") as fcc_file:
        fcc_data = json.load(fcc_file)
        elastic_service = ElasticService()
        index_name = ElasticIndices.GROUP
        for item in fcc_data:
            elastic_service.index(index_name, item)
        print("import group example data success!")
