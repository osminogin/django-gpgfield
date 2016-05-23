from setuptools import setup

setup(
    name="django-pgpfield",
    version="0.0.1",
    description="PGPField for django models",
    url="https://github.com/osminogin/django-pgpfield",
    license='MIT',
    author="Vladimir Osintsev",
    author_email="osintsev@gmail.com",
    packages=[
        "pgpfield",
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ],
)
