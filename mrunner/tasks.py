class CommandWithEnv(object):
    def __init__(self, command, env):
        self.command = command
        self.env = env

    def generate_one_liner(self):
        raise NotImplementedError



class PlgridTask(object):
    def __init__(self, command, cwd=None, env={}, modules_to_load=[], venv_path=None,
                 after_module_load_cmd=None, script_name="mrunner"):
        # paths_to_dump (dst_remote_path, local_path)
        self.command = command
        self.cwd = cwd
        self.env = env
        self.venv_path = venv_path
        self.modules_to_load = modules_to_load
        self.after_module_load_cmd = after_module_load_cmd
        self.script_name = script_name

    def construct_command(self):
        command = ''
        if self.cwd is not None:
            command += 'cd {cwd}\n'.format(cwd=self.cwd)

        for module in self.modules_to_load:
            command += 'module load {}\n'.format(module)

        # command += 'module load openmpi/1.10.2-1_gcc463\n'
        # command += 'module load plgrid/tools/python/3.6.0\n'
        # command += 'module load plgrid/tools/pro-viz/1.1\n'
        # command += 'module load tools/ffmpeg/3.2.2\n'
        # command += 'module load plgrid/tools/openmpi/1.6.5-gcc-4.9.2\n'
        # command += 'module load plgrid/tools/imagemagick/6.9.1\n'

        if self.after_module_load_cmd is not None:
            command += self.after_module_load_cmd + '\n'

        # command += "pip install scipy\n"

        if self.venv_path is not None:
            command += 'source {venv_path}/bin/activate\n'.format(venv_path=self.venv_path)

        for name, val in self.env.iteritems():
            command += 'export {name}={val}\n'.format(name=name, val=val)
        command += self.command
        return command
