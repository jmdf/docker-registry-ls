# Docker registry list

Tool to list information from Docker registries

## Instructions

Print registry catalog
```
python3 docker-registry-ls.py -s https://exampleServer:5000
```

Print tags from a specific repository
```
python3 docker-registry-ls.py -s https://exampleServer:5000 -r group/image
```

Note: `-s https://exampleServer:5000` can be replaced by setting `DOCKER_REGISTRY` environment variable