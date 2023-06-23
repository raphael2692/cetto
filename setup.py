from distutils.core import setup
setup(
  name = 'cetto',         # How you named your package folder (MyLib)
  packages = ['cetto'],   # Chose the same as "name"
  version = '0.0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Simple CLI interface for ChatGPT Based on Langchain. Blazingly fast, easily hackable.',   # Give a short description about your library
  author = 'Raffaele Spataro',                   # Type in your name
  author_email = 'raffaele2692@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/raphael2692/cetto',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_0_0_4.tar.gz',    # I explain this later on
  keywords = ['CHAT', 'GPT', 'CLI'],   # Keywords that define your package best
  install_requires=
        ['beautifulsoup4', 'aiohttp', 'aiosignal', 'async-timeout', 'attrs', 'certifi', 'charset-normalizer', 'colorama', 'dataclasses-json', 'frozenlist', 'greenlet', 'idna', 'langchain', 'langchainplus-sdk', 'marshmallow', 'marshmallow-enum', 'multidict', 'mypy-extensions', 'numexpr', 'numpy', 'openai', 'openapi-schema-pydantic', 'packaging', 'pydantic', 'pyfiglet', 'PyYAML', 'requests', 'SQLAlchemy', 'tenacity', 'tqdm', 'typing-inspect', 'typing_extensions', 'urllib3', 'yarl'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
  entry_points={'console_scripts': ['cetto=cetto.cetto:main']}
)