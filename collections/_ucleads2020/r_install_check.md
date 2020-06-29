---
layout: lesson
title: Installation Check
lesson_name: Running your first programs
lesson: 2
---
* TOC
{:toc}

Since we will be doing an installation check, you will need to run the following instructions once you have installed everything, just to make sure when we meet for the check, that things look good.

If you have any questions, please email us with your problem. As a key takeaway, please keep track of the following using either a Google Doc, Word Document, or simple text document. It is very hard for us to diagnose your problem, without knowing what you have attempted, since we cannot see your computer. The following will help:

- Screen-shot of the error you are having
- Commands you entered (code or command line)
- A recording of the error you encountered

Part of this process is also good to develop good note taking habits, so you can document your problem and solution for a future-you, who will be very thankful for the notes past-you made.

## Preparing for the Installation Check

If you'd like a video of me doing this on my computer, here is the video:

{% include youtubePlayer.html id=page.running_jupyter %}

Make sure you visit my GitHub page ([here](https://github.com/carlos-ar/ucleads-r-programming)) to download two files:

- Jupyter Notebook with R code
- Jupyter Notebook with Python code

You can simply download these files by clicking the big green button on the top right that says: `Clone`

<img src="img/clone_button.png" alt="gitclonebutton" style="zoom: 75%;" />

Once you click on the button, you should see what is below; here you want to download the `.zip` file.

![clickdownload](img/click_download.png)

### Unzipping and moving files

Once you have downloaded the files, you must unzip them, and move them to a location of your choosing. This location is important since you will need to know where to go in your Jupyter Notebook navigator, more about that later.

The only files that are relevant are:

- `python_jupyter_notebook_test.ipynb`
- `r_test.ipynb`

Notice the `.ipynb` extension, this means this is a **iPy**thon Jupyter **N**ote**b**ook, clever isn't is!

## Using Jupyter Notebooks

First, we must make sure that you open the Jupyter Notebooks that know what `R` is so we can run some of the code that is written in `R`.



If you downloaded the code from GitHub, and have it in a location that you trust, we can now navigate to the notebooks location, just as if you were clicking through files in your file navigator (Folders in Windows, or Finder in Mac).

<img src="img/jupyter_files.png" alt="jupyter files" />

In my case, I had to navigate to my notebook locations:

`projects/teaching/ucleads-r-programming/jupyter_notebooks`

Once I get to my notebooks, I should see something like below (note: you all may have deleted the `dummy.md` file, because it actually does nothing).

<img src="img/notebooks_locations.png" alt="location of jupyter notebooks" />

### Running each notebook

From here, you must determine which notebook you want to run first. Lets start with the Python notebook first. If you click on the `python_jupyter_notebook_test.ipynb`, you should see the following:

<img src="img/python_notebook.png" alt="python jupyter notebooks" />

Now you can scroll around and read some of the code. But, for the installation check, you only need to click the follow:

<img src="img/runall.png" alt="runall button" />

This should give you a graph at the bottom, that looks like the one below. And you are **FINISHED** with this part. 

<img src="img/firstplot.png" alt="first plot" />

Now you have to reopen the python 

## Checklist

### Before you start:

- [ ] Download R and R studio
  - [ ] I have downloaded R
  - [ ] Write which version of R:  `______`
  - [ ] I have downloaded R Studio
  - [ ] Write which version of R Studio: `______`
- [ ] Download an Anaconda Distribution
  - [ ] I have downloaded a mac version that works for m
  - [ ] Write in the version of Anaconda: `______`
- [ ] Download Jupyter Notebooks from Carlos's Github
  - [ ] I have located them on my computer, and moved them to a location I know how to get to

### Installations

- [ ] Install R/R Studio
  - [ ] Co-instructor's Windows instructions
  - [ ] [Mac instructions](intro-to-r#mac-os-x-installation)
- [ ] Install Anaconda
- [ ] [Install R using Anaconda Navigator](intro-to-r#installing-r-via-anaconda)
- [ ] Install a command line
  - [ ] If you have a windows computer, Install Git Bash
  - [ ] If you have a mac, you are done

### Testing Programs

- [ ] R/R Studio
  - [ ] Open R Studio
  - [ ] Run a command in R Studio
- [ ] Python via Anaconda
  - [ ] Open Anaconda Navigator
  - [ ] Open Jupyter Notebook with python
  - [ ] Run `python_jupyter_notebook_test.ipynb`
  - [ ] Open Jupyter Notebook with R
  - [ ] Run `r_test.ipynb`
- [ ] Command line
  - [ ] Open 
    - [ ] If on windows, `Git Bash`
    - [ ] If on mac, `terminal`
  - [ ] Type in `pwd`
    - [ ] What was the output: `____`
  - [ ] Type in `echo $USER`
    - [ ] What was the output: `______`
  - [ ] Type in `cd $HOME`
  - [ ] Type in `mkdir testing_commands`
  - [ ] Type in `cd testing_commands`
  - [ ] Type in `pwd`
    - [ ] What was the output: `____`
  - [ ] Type in `ls -A`
    - [ ] What was the output: `_____`
  - [ ] Type in `mkdir file_{0..15}`
  - [ ] Type in `ls -A`
    - [ ] What was the output: `______`
    - [ ] Congratulations! Tell me what happened: `_____`