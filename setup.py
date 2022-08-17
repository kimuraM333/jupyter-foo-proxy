import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="jupyter-foo-proxy",
    version='0.1.0',
    url="https://github.com/kimuraM333/jupyter-foo-proxy",
    author="lm",
    description="sample@example.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    keywords=['jupyter', 'testjsp', 'jupyterhub'],
    classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy>=3.2.0',
        'Flask'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'foo = jupyter_foo_proxy:setup_foo',
        ]
    },
    package_data={
        'jupyter_foo_proxy': ['icons/foo.svg'],
    },
)
