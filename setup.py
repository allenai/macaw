#!/usr/bin/env python3

from setuptools import setup

setup(
  name='macaw_t5',
  version='0.1.0',
  author='AllenAI',
  author_email='ai2-info@allenai.org',
  packages=['macaw'],
  license='LICENSE',
  description='Multi-angle c(q)uestion answering',
  long_description=open('README.md').read(),
  install_requires=[
      "torch==1.12.1",
      "transformers==4.21.1",
      "sentencepiece==0.1.97",
      "protobuf==4.21.5",
  ],
)
