# LaTeX Class Template

Hello and welcome to the wonderful world of perfect LaTeX templates for your classes. Let's start with the installation process.

## Dependency Installation

### Dependencies

- TexLive / MacTeX
- Git
- GitHub
- GitHub CLI
- Python
- VSCode
- Python for VSCode Extension
- LaTeX Workshop

If you already have some of these installed, great! Feel free to skip those sections. Otherwise let's-a go!

### TexLive / MacTeX

Simply follow the link to your appropriate installer:

Windows: https://www.tug.org/texlive/windows.html

Mac: https://www.tug.org/mactex/mactex-download.html

Note that for some stupid reason if you're on windows this will take like hours to install, so do it first and you'll likely just have to leave your computer open for a bit. If you're on mac its really quick though.

### Git

You'll want to install git first which is useful for a lot of things.
If you're on windows, go here: https://git-scm.com/downloads/win and download.

If you're on mac, simply open your terminal and type the following:

```bash
git --version
```
and it should prompt you to install it.

### GitHub

Go to github.com and make an account. 

### GitHub CLI

Download the GitHub CLI here: https://github.com/cli/cli/releases/tag/v2.64.0.

Then, type 
```
gh auth login
```
Follow the prompts to login to your github account. 
Select HTTPS when prompted for preferred protocol.
When asked if you would like to authenticate to Git with your GitHub credentials, enter Y.
Just use your web browser, its way easier.

### Python

Just go to https://www.python.org/downloads/ and install the latest release.

### VSCode

Install VSCode here: https://code.visualstudio.com/download.

### Python for VSCode

Open the marketplace (4 weird squares on the left) tab in VSCode. Install the "Python" extension (description Python language support).

### LaTeX Workshop for VSCode

In the same marketplace, also install the LaTeX Workshop extension. The first/most popular one should be the correct one.

## LaTeX Environment Installation

First create a folder somewhere, maybe called "Notes" or something in your Documents (whatever, your choice).
Then, open your command prompt and using cd commands navigate to that folder.
(For instance, it might start you in your main users folder so you may have to type)
```
cd Documents
cd Notes
```
You should be able to find what folders are within your folder by typing "ls" on mac or "dir" on windows. You can also type "cd .." if you made a mistake and want to go back.

Then, assuming you've done everything right, simply type:
```
git clone https://github.com/eeganr/latexclasstemplate
```

Now, open VSCode, and go File -> Open and click on the new folder that was created.
Now, navigate to the "createnewclass.py" file, and edit the customization settings at the top.
You should probably replace your name, github username, and double check if you're on the quarter vs. semester system.

Once you've done that, simply hit run on the file. It should open up a terminal window where you can follow the prompts.

## Usage

Simply open the folder that was newly created in VSCode. You should also see it show up in your github repositories so it's all backed up online.

You can run the "notes_setup.py" file to create a new notes doc for the day, or the "HW_setup.py" to create a new HW doc (you'll have to enter the number). 

Then, once you're done editing for the class, simply go to the top menu, hit Terminal -> New Terminal.

You can then type "./commit" and everything will be uploaded to the cloud!

If you make changes on one computer and want to have them update on another, simply type "git pull" and that's it!
