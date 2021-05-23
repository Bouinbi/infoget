"""
infogit setup 

"""
from setuptools import setup

setup(
    name="infogit",
    version="1.0.0",
    description="Git info about website ",
    packages=['infogit'],
    
    install_requires=[
        "click",
        "questionary"
    		],
    
    entry_points={
        'console_scripts': ['infogit=infogit.__main__:main']
                },

)

