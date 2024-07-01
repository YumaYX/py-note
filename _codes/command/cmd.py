import subprocess

subprocess.run(['whoami'])

command = 'whoami'
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

print(result)
print(result.stdout)
print(result.stderr)
print(result.returncode)
