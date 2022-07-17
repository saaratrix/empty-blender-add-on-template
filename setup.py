from setuptools import setup  # type: ignore

VERSION = '0.0.1'
REQUIREMENTS = [
    'fake-bpy-module-3.2==20220615',
]

# For example unit test libraries.
DEV_REQUIREMENTS = [
]

if __name__ == '__main__':
    setup(
        name='Blender Add-on',
        version=VERSION,
        description='Blender Add-on template',
        install_requires=REQUIREMENTS,
        extras_require={
            'dev': DEV_REQUIREMENTS,
        },
    )
