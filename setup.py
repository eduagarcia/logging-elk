from setuptools import setup, find_packages

VERSION = '0.0.1'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="logging-elk",
    version=VERSION,
    author="Marco Aleixo",
    author_email="marco.aleixo@misterturing.com",
    description="Facilitar a inserção de logs no nosso ELK.",
    long_description="Facilitar a inserção de logs no nosso ELK utilizando esse pacote como handler da biblioteca logging padrão do python como base",
    packages=find_packages(),
    install_requires=["requests==2.25.1"],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)