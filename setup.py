from setuptools import find_packages, setup
from typing import List

# Constant for editable installs (we will remove it if present)
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads requirements.txt and returns a list of dependencies
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters
        requirements = [req.strip() for req in requirements]
        # Remove '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',                        # Your project name
    version='0.0.1',                         # Initial version
    author='Owaish Patel',                   # Your name
    author_email='owaish@example.com',       # Your email
    packages=find_packages(where='src'),     # Automatically find packages in src/
    package_dir={'': 'src'},                 # Tell setuptools that packages are under src/
    install_requires=get_requirements('requirements.txt'),  # Dependencies from requirements.txt
)
