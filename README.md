# SciPy 2021 Tutorial: Introduction to Numerical Computing With NumPy

#### Presented by: Logan Thomas, [Enthought, Inc.](https://www.enthought.com)

This repository contains all the material needed by students registered for the Numpy tutorial of SciPy 2021 on Monday, July 12th 2021.

For a smooth experience, you will need to make sure that you install or update your Python distribution and download the tutorial material _before_ the day of the tutorial.

## Running the Exercises the (recommended) Easy Way

Run with Binder by clicking this icon: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/enthought/Numpy-Tutorial-SciPyConf-2021/main)


## Running the Exercise Locally

### Install Python

If you don't already have a working python distribution, you may download Anaconda Python ([https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)).


### Install Packages

To be able to run the examples, demos and exercises, you must have the following packages installed:

- numpy 1.17+
- matplotlib 3.3+
- ipython 7.16+ (for running, experimenting and doing exercises)
- pyqt5 5.14+
- jupyter 1.0+

If you are using Anaconda, you can create an environment with the necessary packages with:

```
$ conda create -n numpy-tutorial numpy matplotlib ipython pyqt
```

To test your installation, please execute the `check_env.py` script in the environment where you have installed the requirements.  For example, if you created an Anaconda environment using the instructions above, open up a terminal (or command prompt), navigate to where you have this GitHub repository, and type:

```
$ conda activate numpy-tutorial
$ python check_env.py
```

You should see a window pop up with a plot that looks vaguely like a smiley face.

## Download Tutorial Materials

This GitHub repository is all that is needed in terms of tutorial content. The simplest solution is to download the material using this link:

https://github.com/enthought/Numpy-Tutorial-SciPyConf-2021/archive/main.zip

If you are familiar with Git, you can also clone this repository with:

```
$ git clone https://github.com/enthought/Numpy-Tutorial-SciPyConf-2021.git
```

It will create a new folder named `Numpy-Tutorial-SciPyConf-2021/` with all the content you will need: the slides I will go through (`slides.pdf`), and a folder of exercises.


## Questions? Problems?

You may post messages to the `#tutorial_numpy` Slack channel for this tutorial at in the official Slack team: [https://scipy2021.slack.com](https://scipy2021.slack.com) .
