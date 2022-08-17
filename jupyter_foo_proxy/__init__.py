import os
import shutil
import logging


logger = logging.getLogger(__name__)
logger.setLevel('INFO')


def setup_foo():
    """Setup commands and icon paths and return a dictionary compatible
    with jupyter-server-proxy.
    """
    def _get_icon_path():
        return os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'icons', 'foo.svg')

    # Make sure executable is in $PATH
    def _get_foo_command(port):
        executable = shutil.which('foo')
        if not executable:
            raise FileNotFoundError('Can not find foo executable in $PATH')
        # Create theia working directory
        home_dir = os.environ.get('HOME') or '/home/jovyan'
        working_dir = f'{home_dir}/foo'
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
            logger.info("Created directory %s" % working_dir)
        else:
            logger.info("Directory %s already exists" % working_dir)
        return ['foo']
    
    return {
        'command': ['flask', 'run', '-p {port}'],
        'timeout': 20,
        'new_browser_tab': True,
        'launcher_entry': {
            'title': 'testjsp',
            'icon_path': _get_icon_path()
        },
    }
