from adb_command import adb_command


def get_device_ids():
    command = adb_command('devices').get('stdout')

    devices_ids = {key: value for key, value in [dev_id.rsplit('\t', 1) for dev_id in command.splitlines()[1:-1]]}

    return devices_ids
