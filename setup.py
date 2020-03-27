from setuptools import setup, find_packages


setup(
    name='mkdocs-bootstrap-tables-plugin',
    version='0.1.1',
    description='A MkDocs plugin to add bootstrap classes to plan markdown generated tables.',
    long_description='',
    keywords='mkdocs bootstrap css',
    url='https://github.com/byrnereese/mkdocs-bootstrap-tables-plugin',
    author='Byrne Reese',
    author_email='byrne@majordojo.com',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'bootstrap-tables = mkdocs_bootstrap_tables_plugin.plugin:BootstrapTablesPlugin'
        ]
    }
)
