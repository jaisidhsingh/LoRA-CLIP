from setuptools import setup, find_packages


setup(
	name="loraclip",
	version="0.1.0",
	packages=find_packages(),
	install_requires=[
		"numpy",
		"torch",
		"ftfy",
		"regex",
		"clip@git+https://github.com/openai/CLIP.git",
	],
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