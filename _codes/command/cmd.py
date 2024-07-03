# Python >= 3.7

import subprocess

subprocess.run(['whoami'])

command = 'whoami'
result = subprocess.run(command, capture_output=True, text=True)

print(result)
print(result.stdout)
print(result.stderr)
print(result.returncode)
