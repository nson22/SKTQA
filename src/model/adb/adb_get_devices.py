from src.model.adb.adb_command import adb_command


def get_device_ids():
    command = adb_command('devices', '-l').get('stdout')
    return [i.rsplit()[:-1] for i in command.splitlines()[1:-1]]

