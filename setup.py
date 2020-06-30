import setuptools

setuptools.setup(
    name='touch',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
