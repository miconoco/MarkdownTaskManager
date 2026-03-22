setup(
    name="MarkdownTaskManager",
    version="0.1.0",
    description="Task Manager for local files",
    url="https://github.com/miconoco/MarkdownTaskManager",
    author="coco von miconoco",
    author_email="coco@miconoco.de",
    license="MPL",
    classifiers=[
        "License :: OSI Approved :: Mozilla Public License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["."],
    include_package_data=True,
    install_requires=[
        "Flask"
    ],
    entry_points={"console_scripts": ["realpython=.__main__:main"]},
)
