from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='onto_network',
    version='0.0.1',
    author='Abril Azocar Guzman, Sarath Menon',
    author_email='sarath.menon@pyscal.org',
    description='Simple tool for programmatically working with ontologies',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(include=['onto_network', 'onto_network.*']),
    zip_safe=False,
    download_url = 'https://github.com/pyscal/onto_network',
    url = 'https://pyscal.org',
    install_requires=['rdflib', 
    'pyyaml', 'networkx'],
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
)
