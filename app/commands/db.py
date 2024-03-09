import subprocess
import os
from dotenv import load_dotenv
load_dotenv()
CONTAINER_NAME = os.getenv("CONTAINER_NAME")
DB_NAME = os.getenv("DB_NAME")

### This command cretes the database
def commmand_db_create():
  if there_is_a_db(): 
    print("The database already exists")
    return
  print("Creating database ....") 
  command = f'docker compose up -d'
  r = subprocess.run(command, shell=True, capture_output=True, text=True)
  if (r.returncode == 0):
    print(f"Database with the name '{DB_NAME}' successfully created")
    print(r.stdout)
  else:
    print("Command execution failed")
    print(r.stderr)

### This command check if the database exits
def there_is_a_db():
    try:
        output = subprocess.check_output(["docker", "ps", "-f", f"name={CONTAINER_NAME}"])
        output_str = output.decode("utf-8")
        return CONTAINER_NAME in output_str
    except subprocess.CalledProcessError:
        return False

