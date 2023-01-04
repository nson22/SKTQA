import subprocess
from operator import add


def adb_command(*args, arch='windows'):
    result = subprocess.run([f'arch/{arch}/platform-tools/adb.exe', *args],
                            capture_output=True,
                            check=True,
                            text=True)

    return {'stdout': result.stdout, 'stderr': result.stderr, 'return_code': result.returncode}


