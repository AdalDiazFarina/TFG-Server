# Tool for the Analysis of Long-Term Investment Strategies for Different Financial Profiles - Server
This project is the server-side application built with Python and Flask. It includes a dockerized database and contains all the business logic of the application.

## Author
Adal Díaz Fariña
## Features
- Database Initialization: Create and migrate the database using a custom command.
- API Documentation: Documentation of the API endpoints available through Swagger.
- Business Logic: The server contains all the business logic for the application.
## Technologies Used
- Python: The programming language used for the server logic.
- Flask: A micro web framework for Python.
- Docker: Used to containerize the database.
- Swagger: For API documentation.
## Getting Started
To get a local copy of the project up and running, follow these steps:

### Prerequisites
- Python: Make sure you have Python installed. You can download it from python.org.
- Docker: Ensure you have Docker installed. You can download it from docker.com.

### Installation
1. Clone the repository:

```sh
git clone git@github.com:AdalDiazFarina/TFG-Server.git
```

2. Create a virtual environment:

```sh 
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:
```sh 
venv\Scripts\activate
```

- On macOS and Linux:
```sh 
source venv/bin/activate
```

4. Activate the virtual environment:
- On Windows:
```sh 
venv\Scripts\activate
```
- On macOS and Linux:
```sh 
source venv/bin/activate
```
5. Create the .env file:

Create a .env file in the root of the project and add the following data:

```env
DB_NAME="FundFowForge"
DB_USER="root"
DB_PASSWORD="1234"
CONTAINER_NAME="server"
PORT="5432"
HOST="localhost"
DATABASE_URL="postgresql://${DB_USER}:${DB_PASSWORD}@${HOST}:${PORT}/${DB_NAME}"
BOOTSTRAP_SERVERS = "localhost:9092"
```

### Running the Project
To initialize and run the server, follow these steps:

Initialize the Database:

This command will create the database in the Docker container and apply the migrations.

sh
Copiar código
python main.py init
Start the Server:

This command will start the server.

sh
Copiar código
python main.py run
API Documentation
The API endpoints are documented using Swagger. You can access the documentation by navigating to the Swagger UI endpoint after starting the server.

Usage
Initialize Database: Run python main.py init to create and migrate the database.
Start Server: Run python main.py run to start the server.
