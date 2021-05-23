"""
infoget setup 

"""
from setuptools import setup

setup(
    name="infoget",
    version="1.0.0",
    description="Get info about website ",
    packages=['infoget'],
    
    install_requires=[
        "click",
        "questionary"
    		],
    
    entry_points={
        'console_scripts': ['infoget=infoget.__main__:main']
                },

)

