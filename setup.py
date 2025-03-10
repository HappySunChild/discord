import setuptools

setuptools.setup(
	name='discord',
	description='',
	version='1.0.2',
	author='HappySunChild',
	url='https://github.com/HappySunChild/discord',
	
	packages=setuptools.find_packages(),
	python_requires='>=3.9',
	install_requires=[
		'websockets>=12.0'
	]
)