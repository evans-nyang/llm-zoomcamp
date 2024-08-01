# Miniconda Installation Script

This script automates the installation of Miniconda on a Linux system. It downloads the Miniconda installer, installs it, and sets up the environment.

## Prerequisites

+ A Linux-based operating system
+ `wget` installed on your system

## Usage

1. Download the script to your system.

```bash
wget https://github.com/evans-nyang/llm-zoomcamp/raw/main/bin/install_miniconda.sh -O install_miniconda.sh
```

2. Make the script executable by running the following command:

```bash
chmod +x install_miniconda.sh
```

3. Run the script:

```bash
./install_miniconda.sh
```

4. After running the script, you can verify the installation by checking the conda version:

```bash
conda --version
```

## What the Script Does

+ Defines the Miniconda version to be installed.
+ Downloads the Miniconda installer.
+ Makes the installer executable.
+ Runs the installer in batch mode.
+ Adds Miniconda to the PATH in .bashrc.
+ Sources the .bashrc to update the current shell session.
+ Removes the installer script.
+ Updates conda to the latest version.
+ Displays the installed conda version to verify the installation.

## Extras

You can customize the script by changing the Miniconda version or the installation directory. You can also add additional packages to be installed after setting up Miniconda.

To learn more about Miniconda, visit the official documentation by clicking on this link: [Miniconda Documentation](https://docs.anaconda.com/miniconda/)
