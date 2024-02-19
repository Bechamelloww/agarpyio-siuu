[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/3a9G6PPC)

# Agarpyio

In this project, our goal was to reproduce the famous game Agar.io but with the PyGame library.

# Prerequisites

Make sure you have Anaconda Navigator installed, so it's easier to change Python version.

Python version needed : 3.11.7
PyGame version  needed : 2.5.2

You can create a new python 3.11.7 environment or use mine if you import this .yaml :

```
name: python-311
channels:
  - defaults
dependencies:
  - bzip2=1.0.8=he774522_0
  - ca-certificates=2023.12.12=haa95532_0
  - libffi=3.4.4=hd77b12b_0
  - openssl=3.0.13=h2bbff1b_0
  - pip=23.3.1=py311haa95532_0
  - powershell_shortcut=0.0.1=3
  - python=3.11.7=he1021f5_0
  - setuptools=68.2.2=py311haa95532_0
  - sqlite=3.41.2=h2bbff1b_0
  - tk=8.6.12=h2bbff1b_0
  - tzdata=2023d=h04d1e81_0
  - vc=14.2=h21ff451_1
  - vs2015_runtime=14.27.29016=h5e58377_2
  - wheel=0.41.2=py311haa95532_0
  - xz=5.4.5=h8cc25b3_0
  - zlib=1.2.13=h8cc25b3_0
  - pip:
      - pygame==2.5.2

```

Create and activate your virtual environment from this .yml file :
```bash
conda env create -n python-311 -f your-yaml-file-name.yml
conda activate python-311
```

# Installation

- Download this repo as a .zip (Code -> Download ZIP)
- Unzip the folder
- Open it with PyCharm
- Activate you python environment (conda activate python-311)
- If not installed, install pygame v2.5.2 (pip3 install pygame)
- Run the main.py file
- Siuuu

## If you get problems with PyCharm

### If no interpreter

- File -> Settings -> Project: agarpiyo.... -> Python  Interpreter -> Add interpreter -> Add a local interpreter -> select the one in the python-311 folder.

### If pygame is not found

Go back to the python Interpreter window from settings. Under the list used to choose the interpreter, you can add a library. Click on the '+' icon. Search for 'pygame' and install it.

## You should be ready to play now !

# How to play

When you run main.py, a windows pop with the main menu opened. You can click on one difficulty and on one control mode. When you are ready, click on 'JOUER' !

Inside the game, you are a ball. You need to eat the little Cristianos to become bigger and faster, and to be careful not to get too close from MessiSpikes, because if you're bigger than it, you'll lose many speed and size. Your goal is to eat as many cristianos as possible in 60 seconds. When the timer is done, you'll get back to the main menu. You can also press the 'Escape' key to go back to the main menu while playing.

Controls if you selected the keyboard : 
- Z : Go up
- Q : Go left
- S : Go down
- D : Go right

When you play with the keyboard, you can also go through the edge of the screen and you'll reappear at the other side of it.
