from setuptools import setup, find_packages

setup(
    name='RankGPT',
    version='0.1',
    packages=find_packages(),  # Automatically finds the 'rankgpt' package
    install_requires=[
        'tqdm',
        'openai',
        'tiktoken',
        'pyserini',
    ],
    include_package_data=True,  # Optional: Include non-Python files
    description="RankGPT: A ranking-focused GPT library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    author="",
    url="https://github.com/HewZK1211/RankGPT",
)
