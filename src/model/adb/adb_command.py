import subprocess

def adb_command(command, arch='windows'):
    result = subprocess.run([f'arch/{arch}/platform-tools/adb.exe', command],
                            capture_output=True,
                            check=True,
                            text=True)
    return {'stdout': result.stdout, 'stderr': result.stderr, 'returncode': result.returncode}
