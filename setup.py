from setuptools import setup, find_packages

setup(
    name='cleanmail',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
      "google-api-python-client>=2.0.0",
      "google-auth-oauthlib>=1.0.0",
      "requests>=2.0.0" 
    ],
    entry_points={
        'console_scripts': [
           'cleanmail=cleanmail.cli:main'
        ]
    },
    author='Joshua Suhas J',
    description='CLI Gmail cleaner tool to delete or trash emails by sender and time range.',
    python_requires='>=3.7',
)