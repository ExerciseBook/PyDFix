import subprocess

def _run_command(command, env=None):
    if env:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, env=env)
    else:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    stdout = stdout.decode('utf-8').strip()
    stderr = stderr.decode('utf-8').strip()
    ok = process.returncode == 0
    return process, stdout, stderr, ok