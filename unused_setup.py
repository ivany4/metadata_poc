from setuptools import setup
import pathlib

license_text = (pathlib.Path(__file__).parent / "license.txt").read_text()

print(repr(license_text))
setup(
    name="metadata_poc",
    description="PoC for metadata bug",
    version="0.0.1",
    install_requires=[
        "requests",
    ],
    license=license_text,
)
