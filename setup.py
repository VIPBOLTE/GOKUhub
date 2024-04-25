
from setuptools import setup, find_packages
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'GOKUhub',        
  packages = ['GOKUhub'],
  include_package_data=True,
  version = '1.2',    
  license='MIT',     
  description = 'GOKUhub Logo Generator', 
  author = 'Mr GOKU',                  
  author_email = 'kdivesh657@gmail.com',     
  url = 'https://github.com/VIPBOLTE/GOKUhub',   
  download_url = 'https://github.com/VIPBOLTE/GOKUhub/archive/1.2.tar.gz',    
  keywords = ['GOKUhub', 'logo', 'generator'], 
  install_requires=[           
          'pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
