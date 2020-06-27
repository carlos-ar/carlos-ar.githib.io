---
layout: lesson
title:  Introduction to R
lesson_name: Guides for installation
lesson: 1
---
* TOC
{:toc}

We will be using 3 main programs for the course, and we need you to run through the installation of these programs. So in order to simplify this process, we will have you do the following

- Install R
  - [What is R?](https://en.wikipedia.org/wiki/R_(programming_language))
  - This is the programming language
- Install R studio
  - [What is R studio?](https://en.wikipedia.org/wiki/RStudio)
  - This is an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) (integrated development environment)
- Install Python via Anaconda distribution
  - What is Python? 
    - This is the programming language
    - You can write code and run it from a command line
  - What is Anaconda?
    - This is the "software distribution"
    - It is the Python language, and it includes many tools
- Read more below for more information about each and everyone of these

## Installing R

The programming language R, is available to download for free. If you prefer to watch me install R on my Mac, check out the videos.

### Windows 10 Installation

The other co-instructor will be either sending an instructional video or `how-to.pdf` file to help you with this. 

### Mac OS X Installation

Here is my raw semi-unedited video of installing R and R studio 

## Installing Python via Anaconda

There are many ways to get Python on your computer. I will not detail all of them, because 1) I do not know all of them and 2) for the purposes of this course, you will only need the version that is most self-contained.

We are going to use Anaconda for install both Python and R, but you must understand the following:

- Anaconda lets you manage `environments` in a discrete fashion.

What does this mean? It took me a while to admit it, but when you use programming languages such as Python and R, people make packages that *extend* the capability of the language.

Lets say, for example, that I wanted to write a piece of code, called `stamp`, that stamped all my images with name in the bottom left hand corner, and I wanted to write it in Python, and make it available through Anaconda. When I make it available to everyone, there is a chance I utilized someone else's image reading *library* or *module* or *package* (each of these terms sometimes are use interchangeably, but not always are they true).

Anyhow, I digress, so let's say I give you this piece of code, but I used Sara's code that read images in. Sara called this code `image_reader` and it was in version `2.1`. Well when I give you this code, I must make sure you have `image_reader Version 2.1`. 

Well now, Ismael comes along, and wants to use my code, and finds it online. He installs it without using *my version* that is on Anaconda, and it doesn't work because he never installed Sara's code. Well...it turns out, that if Ismael would have used Anaconda, it most likely would have told him "If you want to install `stamp v0.1` you need `image_reader v2.1`" and then he would have no problems. 

### Windows 10 Installation

I will upload my video and instructions here, so you can see how I installed this on my computer. It has been a while since I've used a Window's machine, but I will try!

### Mac OS X Installation

Installation instructions to come!