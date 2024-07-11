import json
from config.env_paras import EnvParas
from constants.constants import ElasticIndices
"""
创建索引
"""

if __name__ == '__main__':
    # es_service = ElasticService()
    ELASTIC_HOST = EnvParas.ELASTIC_HOST
    ELASTIC_USER = EnvParas.ELASTIC_USER
    ELASTIC_PASSWORD = EnvParas.ELASTIC_PASSWORD

    index_name = ElasticIndices.GROUP

    # if exits index: curl -XDELETE http://localhost:9200/products
    delete_index_cmd = f"curl -XDELETE -u {ELASTIC_USER}:{ELASTIC_PASSWORD} {ELASTIC_HOST}/{index_name}"

    # 1. create index example: curl -XPUT http://localhost:9200/products?pretty
    create_index_cmd = f"curl  -XPUT -u {ELASTIC_USER}:{ELASTIC_PASSWORD} {ELASTIC_HOST}/{index_name}?pretty"

    # 2. design mapping example:
    """
    curl -H'Content-Type: application/json' -XPUT http://localhost:9200/products/_mapping/?pretty -d'{
  "properties": {
    "type": { "type": "keyword" } ,
    "title": { "type": "text", "analyzer": "ik_smart" }, 
    "long_title": { "type": "text", "analyzer": "ik_smart" }, 
    "category_id": { "type": "integer" },
    "category": { "type": "keyword" },
    "category_path": { "type": "keyword" },
    "description": { "type": "text", "analyzer": "ik_smart" },
    "price": { "type": "scaled_float", "scaling_factor": 100 },
    "on_sale": { "type": "boolean" },
    "rating": { "type": "float" },
    "sold_count": { "type": "integer" },
    "review_count": { "type": "integer" },
    "skus": {
      "type": "nested",
      "properties": {
        "title": { "type": "text", "analyzer": "ik_smart" }, 
        "description": { "type": "text", "analyzer": "ik_smart" },
        "price": { "type": "scaled_float", "scaling_factor": 100 }
      }
    },
  }
}'
    """
    mapping_dict = {
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "text", "analyzer": "ik_smart"},
            "description": {"type": "text"},
            "link": {"type": "text"},
            "member_num": {"type": "integer"},
            "tags": {"type": "keyword"}
        }
    }

    mapping_str = json.dumps(mapping_dict)
    create_mapping_cmd = f"curl -u {ELASTIC_USER}:{ELASTIC_PASSWORD} -H 'Content-Type: application/json' -XPUT {ELASTIC_HOST}/{index_name}/_mapping/?pretty -d'{mapping_str}'"

    readme = f"""
    1:delete index cmd:
    {delete_index_cmd}
    2:create index cmd:
    {create_index_cmd}
    3:create mapping cmd:
    {create_mapping_cmd}
    """
    print(readme)
