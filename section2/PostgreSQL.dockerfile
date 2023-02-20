
docker run -d 
    --name postgres 
    -p 5432:5432
    -e POSTGRES_PASSWORD=<password> 
    -v postgres:/var/lib/postgresql/data 
    postgres:14