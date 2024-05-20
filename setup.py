from setuptools import setup

setup(
    name='conditional_diffusion',
    version='0.1.0',    
    description='Reimplementation of https://github.com/dome272/Diffusion-Models-pytorch as an importable python package',
    url='https://github.com/stevenharperja/conditional_diffusion',
    author='Steven Harper',
    author_email='steven.harper.ja@protonmail.com',
    license='Apache 2.0',
    packages=['conditional_diffusion'],
    install_requires=[
                        'numpy',
                        'matplotlib',
                        'torch',
                        'torchvision',
                        'tqdm',
                        'Pillow',    
                        'tensorboard',       
                      ],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',  
        'Programming Language :: Python :: 3',
    ],
)
