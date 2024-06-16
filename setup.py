from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        # Filter out any empty lines or comments
        return [line for line in lines if line and not line.startswith('#')]


setup(
	name="loraclip",
	version="0.1.0",
	packages=find_packages(),
	install_requires=parse_requirements("requirements.txt"),
    author='Jaisidh Singh',
    author_email='jaisidhsingh@gmail.com',
    description='A simple and efficient wrapper for LoRA-ifying CLIP.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jaisidhsingh/LoRA-CLIP',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)