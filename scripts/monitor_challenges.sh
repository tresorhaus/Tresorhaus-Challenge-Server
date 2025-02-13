#!/bin/bash

echo "=== Tresorhaus Challenge Monitor ==="
echo "Current time: $(date)"
echo ""

echo "Active Challenges:"
echo "================="
docker ps --filter "name=challenger_" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo ""
echo "Resource Usage:"
echo "=============="
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}" $(docker ps -q --filter "name=challenger_")

echo ""
echo "Recent Logs:"
echo "==========="
for container in $(docker ps -q --filter "name=challenger_"); do
    echo "Container: $(docker inspect --format '{{.Name}}' $container)"
    docker logs --tail 5 $container
    echo "-------------------"
done
