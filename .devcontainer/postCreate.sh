#!/bin/bash

# Install Python packages
pip install matplotlib pandas numpy

# Install Node.js dependencies (for the web server)
npm install

# Install steam locomotive for fun
sudo apt-get update
sudo apt-get install sl
sudo apt-get install git-lfs && git lfs install
echo "export PATH=\$PATH:/usr/games" >> ~/.bashrc
echo "export PATH=\$PATH:/usr/games" >> ~/.zshrc

echo "Setup complete! Ready for Python expense tracking and Node.js web serving."