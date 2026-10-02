# Docker + PostgreSQL Notes

## Pull PostgreSQL image
docker pull postgres:16

## Run PostgreSQL container
docker run --name postgres-db -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=mydb -p 5432:5432 -d postgres:16

## Check running containers
docker ps

## Connect with psql
docker exec -it postgres-db psql -U postgres -d mydb

## Stop the container
docker stop postgres-db

## Start the container again
docker start postgres-db