"""
Primeiro subimos um o broker para servir de ponte.

Sugestão para client desktop para testes: https://mqttx.app/  

Docker compose para subir um cluster EMQX mqtt:
'''
services:
  emqx1:
    image: emqx:latest
    environment:
    - "EMQX_NODE__NAME=emqx@node1.emqx.io"
    - "EMQX_CLUSTER__DISCOVERY_STRATEGY=static"
    - "EMQX_CLUSTER__STATIC__SEEDS=[emqx@node1.emqx.io]"
    networks:
      emqx-bridge:
        aliases:
        - node1.emqx.io
    ports:
      - 1883:1883
      - 8083:8083
      - 8084:8084
      - 8883:8883
      - 18083:18083 

networks:
  emqx-bridge:
    driver: bridge
'''
"""