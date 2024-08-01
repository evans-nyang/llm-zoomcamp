#!/usr/bin/env bash

# Define Miniconda version
MINICONDA_VERSION="Miniconda3-py310_24.4.0-0-Linux-x86_64.sh"

# Download Miniconda installer
wget https://repo.anaconda.com/miniconda/$MINICONDA_VERSION -O miniconda.sh

# Check if download was successful
if [ $? -ne 0 ]; then
    echo "Failed to download Miniconda installer"
    exit 1
fi

# Make the installer executable
chmod +x miniconda.sh

# Run the installer
./miniconda.sh -b -p $HOME/miniconda

# Check if installation was successful
if [ $? -ne 0 ]; then
    echo "Miniconda installation failed"
    exit 1
fi

# Add Miniconda to PATH in .bashrc
echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> $HOME/.bashrc

# Activate the installation
source $HOME/.bashrc

# Remove the installer
rm miniconda.sh

# Update conda
conda update -y conda

# Check if conda update was successful
if [ $? -ne 0 ]; then
    echo "Conda update failed"
    exit 1
fi

# Display conda version to verify installation
conda --version
