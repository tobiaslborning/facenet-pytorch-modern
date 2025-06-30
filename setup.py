import setuptools, os

PACKAGE_NAME = 'facenet-pytorch-modern'  # Updated package name
VERSION = '2.5.3'  # Bump major version for significant dependency updates
AUTHOR = 'Tobias Borning'  # Update to your name
EMAIL = 'tobias.borning@stud.ntnu.no'  # Update to your email
DESCRIPTION = 'Pytorch face detection and recognition models with updated dependencies'
GITHUB_URL = 'https://github.com/tobiaslborning/facenet-pytorch-modern'  # Update to your fork URL

parent_dir = os.path.dirname(os.path.realpath(__file__))
import_name = os.path.basename(parent_dir)

with open('{}/README.md'.format(parent_dir), 'r') as f:
    long_description = f.read()

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=GITHUB_URL,
    packages=[
        'facenet_pytorch_modern',
        'facenet_pytorch_modern.models',
        'facenet_pytorch_modern.models.utils',
        'facenet_pytorch_modern.data',
    ],
    package_dir={'facenet_pytorch_modern':'.'},
    package_data={'': ['*net.pt']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy>=1.24.0,<2.0.0',
        'Pillow>=10.2.0,<10.3.0',
        'requests>=2.0.0,<3.0.0',
        'torch>=2.2.0,<=2.7.0',
        'torchvision>=0.17.0,<=0.21.0',
        'tqdm>=4.0.0,<5.0.0',
    ],
)
