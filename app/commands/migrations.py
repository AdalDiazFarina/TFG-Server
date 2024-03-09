import subprocess

def command_create_migration(description): 
  command = f'alembic revision --autogenerate -m "{description}"'
  r = subprocess.run(command, shell=True, capture_output=True, text=True)
  if (r.returncode == 0):
    print("Command execution was successful")
    print(r.stdout)
  else:
    print("Command execution failed")
    print(r.stderr) 

def command_update_migration():
  command = 'alembic upgrade head'
  r = subprocess.run(command, shell=True, capture_output=True, text=True)
  if (r.returncode == 0):
    print("Command execution was successful")
    print(r.stdout)
  else:
    print("Command execution failed")
    print(r.stderr) 

def command_delete_migration(flag):
  if (flag == 'last'):
    command = 'alembic downgrade -1'
  else:
    command = f'alembic downgrade {flag}'
  r = subprocess.run(command, shell=True, capture_output=True, text=True)
  if (r.returncode == 0):
    print("Command execution was successful")
    print(r.stdout)
  else:
    print("Command execution failed")
    print(r.stderr) 