from setuptools import setup, find_packages

setup(
    name='RankGPT',
    version='0.1',
    packages=find_packages(),
    install_requires=['tqdm', 'openai', 'tiktoken', 'pyserini'],
)
