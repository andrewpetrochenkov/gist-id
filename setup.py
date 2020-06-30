import setuptools

setuptools.setup(
    name='gist-id',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/gist-id']
)
