#!/usr/bin/env bash

# Define Miniconda version
MINICONDA_VERSION="Miniconda3-py310_24.4.0-0-Linux-x86_64.sh"

# Download Miniconda installer
wget https://repo.anaconda.com/miniconda/$MINICONDA_VERSION -O miniconda.sh

# Make the installer executable
chmod +x miniconda.sh

# Run the installer
./miniconda.sh -b -p $HOME/miniconda

# Add Miniconda to PATH in .bashrc
echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> $HOME/.bashrc

# Activate the installation
source $HOME/.bashrc

# Remove the installer
rm miniconda.sh

# Update conda
conda update -y conda

# Display conda version to verify installation
conda --version