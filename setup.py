import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'
REPO_NAME = 'indi'
AUTHOR_USER_NAME = 'aaron'
SRC_REPO = 'indi'
AUTHOR_EMAIL = 'dataaaronsanchezbelber@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Package for app',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify content type
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'': 'src'},  # Adjust if necessary
    packages=setuptools.find_packages(where='src'),  # Automatically discover packages
)
