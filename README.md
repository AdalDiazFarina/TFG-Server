## TFG Server

### Env file
Specify .env file with the following data

```
DB_NAME="FundFowForge"
DB_USER="root"
DB_PASSWORD="1234"
CONTAINER_NAME="server"
PORT="5432"
HOST="localhost"
DATABASE_URL="postgresql://${DB_USER}:${DB_PASSWORD}@${HOST}:${PORT}/${DB_NAME}"
BOOTSTRAP_SERVERS = "localhost:9092"
```
