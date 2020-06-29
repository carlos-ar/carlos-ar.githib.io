---
layout: lesson
title:  Preparing for R
lesson_name: Guides for installation
lesson: 1
win_r_install: p_di4Zn4wz4
mac_r_install: Yn1hWAkJZK0
win_anaconda_install: p_di4Zn4wz4
mac_anaconda_install: p_di4Zn4wz4
win_gitbash_install: p_di4Zn4wz4
open_jupyter: p_di4Zn4wz4
r_anaconda_jupyter: 0c9P7izOG2c
---
* TOC
{:toc}
We will be using 3 main programs for the course, and we need you to run through the installation of these programs. So in order to simplify this process, we will have you do the following below. Download [this](/assets/files/checklist.pdf) `.pdf` in order to have a checklist of things you need to do.

### Topics covered

- Install R
  - [What is R?](https://en.wikipedia.org/wiki/R_(programming_language))
  - This is the programming language
- Install R studio
  - [What is R studio?](https://en.wikipedia.org/wiki/RStudio)
  - This is an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) (integrated development environment)
- Install Python via Anaconda distribution
  - What is [Python](https://en.wikipedia.org/wiki/R_(programming_language))? 
    - This is the programming language
    - You can write code and run it from a command line
  - What is [Anaconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution))?
    - This is the "software distribution"
    - It includes the Python language, and it includes many tools
    - You can also use R from Anaconda! More about this below.

Read more below for more information about each and everyone of these

## Installing R

The programming language R, is available to download for free. If you prefer to watch me install R on my Mac, check out the videos.

### Windows 10 Installation

The other co-instructor will be either sending an instructional video or `how-to.pdf` file to help you with this. 

### Mac OS X Installation

Here is my raw semi-unedited video of installing R and R studio 

{% include youtubePlayer.html id=page.mac_r_install %}

## Installing Python via Anaconda

There are many ways to get Python on your computer. I will not detail all of them, because 1) I do not know all of them and 2) for the purposes of this course, you will only need the version that is most self-contained.

We are going to use Anaconda for install both Python and R, but you must understand the following:

- Anaconda lets you manage `environments` in a discrete fashion.

What does this mean? It took me a while to admit it, but when you use programming languages such as Python and R, people make packages that *extend* the capability of the language.

Lets say, for example, that I wanted to write a piece of code, called `stamp`, that stamped all my images with name in the bottom left hand corner, and I wanted to write it in Python, and make it available through Anaconda. When I make it available to everyone, there is a chance I utilized someone else's image reading *library* or *module* or *package* (each of these terms sometimes are use interchangeably, but not always are they true, especially in each different programming language).

Anyhow, I digress, so let's say I give you this piece of code, but I used Sara's code that read images in. Sara called this code `image_reader` and it was in version `2.1`. Well when I give you this code, I must make sure you have `image_reader Version 2.1`. 

Well now, Ismael comes along, and wants to use my code, and finds it online. He installs it without using *my version* that is on Anaconda, and it doesn't work because he never installed Sara's code. Well...it turns out, that if Ismael would have used Anaconda, it most likely would have told him "If you want to install `stamp v0.1` you need `image_reader v2.1`" and then he would have no problems. 

### Preparing for installation

First, I will list the steps that I followed: 

- I did a google search saying "install anaconda windows 10"
  - Without showing a screen-shot of my window showing the google results, this was the second link on there.
  - [https://docs.anaconda.com/anaconda/install/](https://docs.anaconda.com/anaconda/install/)
  - There were also a bunch of videos, that have step by step installation, but feel free to see any one of those, or click on my video above
- Click on the link above, or the google link that you did when you searched this
  - You should see something like the image below:
  - Several things are highlighted in red:
    - Operating system: tells you if you can install it with your current operating system. **WARNING: Some of you have Mac OS X 10.12.6 Sierra** so you will have to google "how to install Anaconda on Sierra 10.12.6" since you haven't updated your operating system
    - The green links are highlighted to show you where you can click for your own directions to install the `v. latest` of Anaconda
    - Final thing I have highlighted is the version. This will install the latest version of Anaconda. For those that do not have Mac OS X 13 and above, you can change this button to an earlier version and follow those instructions, though there are no guarantees that it will work

<img src="img/anaconda_install.png" alt="anaconda install webpage" style="width:750px;" />

- Now you must download the installer for Python via Anaconda
  - Click this link here: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)
  - In theory, you should scroll all the way down the page until you see what is in the image below
  - For Windows, [download](https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe) `Python 3.7 64-Bit Graphical Installer`
  - For Mac, [download](https://repo.anaconda.com/archive/Anaconda3-2020.02-MacOSX-x86_64.pkg) `Python 3.7 64-Bit Graphical Installer`
  - For those of you with Mac OS X 10.12.6 Sierra, this is the last time officially, there was a report in the release notes for Anaconda:
    - "Anaconda 4.2 is the last release that supports macOS 10.7 and macOS 10.8. Anaconda 4.3 supports macOS versions from 10.9 through the current version 10.12."
    - This means that possibly, 4.3 works for 10.12.6.
    - You can go [here](https://repo.anaconda.com/archive/) to try to download 4.3
    - No guarantees here! 

<img src="img/anaconda_installers.png" alt="installers for anaconda" style="width:750px;" />

### Windows 10 Installation

I will upload my video and instructions here, so you can see how I installed this on my computer. It has been a while since I've used a Window's machine, but I will try!

Here are the instructions from Anaconda that I followed: [https://docs.anaconda.com/anaconda/install/windows/](https://docs.anaconda.com/anaconda/install/windows/)

{% include youtubePlayer.html id=page.win_anaconda_install %}

### Mac OS X Installation

Since I already have Anaconda installed, I will only post the instructions for installing on Mac OS X here, from the official documents: [https://docs.anaconda.com/anaconda/install/mac-os/](https://docs.anaconda.com/anaconda/install/mac-os/)

### Opening Jupyter Notebooks

Jupyter is kind of like an IDE, which allows us to run code from our computer browers. You typically can open Jupyter Notebook using two methods, a command line executing if you are running an operating system that is Unix based (like a Mac), or just opening it from the Anaconda Navigator.

Here is the instructions I found in order to open the Anaconda Navigator: [https://docs.anaconda.com/anaconda/user-guide/getting-started/](https://docs.anaconda.com/anaconda/user-guide/getting-started/).

{% include youtubePlayer.html id=page.open_jupyter %}

## Installing R via Anaconda

Since, we most likely be using Jupyter Notebooks with R, then we can use the Anaconda package manager to install R! Here are the instructions one you have installed Anaconda

**GO Back and [Install](#installing-python-via-anaconda) Anaconda, you need it before you proceed**

Since you have already downloaded and installed Anaconda, now you just need to create an environment that knows about R. The instructions below will let you install an environment that knows about the `Python` and `R` languages. 

[https://docs.anaconda.com/anaconda/navigator/tutorials/r-lang/](https://docs.anaconda.com/anaconda/navigator/tutorials/r-lang/)

Once you have installed this, you should be able to run the code in this tutorial. You will run that once again for the installation check.

{% include youtubePlayer.html id=page.r_anaconda_jupyter %}

https://youtu.be/0c9P7izOG2c

## Command line emulator

We will be typing things into a (typically) black window that looks a lot like something from a movie where "hackers" are breaking into some classified computer system. The [command line](https://docs.freebsd.org/doc/2.2.7-RELEASE/usr/share/doc/handbook/term:uses.html) is how computers were initially used, before the introduction of the "mouse". 

<img src="img/terminal_example.png" alt="terminal example" style="width:750px;" />

What you see in the image above is a terminal that allows me to *enter* commands into the *command line* and make the computer do pretty much anything. This is a [Linux operating system](https://www.linux.com/what-is-linux/) terminal (read this page, I learned a thing or two as well!). Since you all will be using a different one on your machine, because you may have a windows operating system or Mac operating system, it might look differently. 

Additionally, terminals come in different *flavors*, meaning that there are different types. For example, there are "shell" and "bourne-again shell" terminals which are the ones I have more experience with. If you want to learn more about this history of terminals, visit this [wiki page](https://en.wikipedia.org/wiki/Computer_terminal#Capabilities).

We will list some instructions for you go to download a terminal operating system in the next section.

### Windows 10: Git Bash

On Windows, it isn't the easiest to use a command line aside from the old `cmd` terminal that had an [emulation](https://www.lifewire.com/command-prompt-2625840) of `MS-DOS`, where you could do a lot of things. But now, you can install a "Window Subsystem for Linux" and other great additions. But we are not going to do that, we are only going to do Git Bash, since it will be more than enough for our course.

Here are the instructions for installing that I used [https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows/](https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows/). One day we will talk about Git, but not today!

Also, here is my recording installation on Windows, which I have never done!

{% include youtubePlayer.html id=page.win_gitbash_install %}

### Mac OSX: Terminal

Since Mac runs an Unix based system, then you typically have the terminal window already installed! Great, no need to install things. 

Check these few links out to play around with the command line.

- [Open the command line](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac)
- Using `bash` [command line](https://www.codecademy.com/articles/command-line-commands)

