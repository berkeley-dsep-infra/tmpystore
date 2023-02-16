import setuptools

setuptools.setup(
    name="tmpystore",
    version="0.0.1",
    url="https://github.com/ryanlovett/tmpystore",
    author="Ryan Lovett",
    author_email="rylo@berkeley.edu",
    description="Move jupyter ystore db to /tmp",
    packages=setuptools.find_packages(),
    keywords=["jupyterlab"],
    install_requires=["ypy_websocket"],
)
