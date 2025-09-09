# Understanding GitHub's Codespaces

*Adapted by [drklis](https://github.com/drklis) for ECON 691 and Tech Tacos at Northern Illinois University*

This is a quick node project template for demoing Codespaces. It is based on the [Azure node sample](https://github.com/Azure-Samples/nodejs-docs-hello-world). We will be using this as an assignment to familiarize you with GitHub Codespaces and how to do "commits" in them. As a bonus, it will also introduce you to "ports" and preview the ability to change webpages with code.

### What is a codespace?
When you code, you're doing so in one of two ways: interacting directly with a terminal (typing commands line-by-line) or working in an **Integrated Development Environment** (IDE), which is a (hopefully) user-friendly application that combines code editing, file management, and terminal access all in one place. If you know you're going to be working directly on your own computer most of the time, it makes a lot of sense to find an IDE set-up that you like and works for your goals, but this can be an involved process to configure all the tools. 

A **codespace** is a complete development environment **hosted in the cloud** that's configured specifically for your project. Think of it as a complete computer setup with user interface, the programming languages you need, integrated tools, and even your files that runs in your browser - so you can access it from any device and share it easily with collaborators. 

We'll be using GitHub Codespaces with Visual Studio (VS) Code as our programming interface. A lot of programmers like to use VS or VS Code as their main way of interacting with their coding projects since it handles a lot of different languages and is visually appealing. When you go to use codespaces, GitHub will create the dev environment automatically based on your repository's configuration.

#### Why use Codespaces?
- 🚀 **Instant setup**: No "it works on my machine" problems
- 🌐 **Access anywhere**: Code from any device with a browser
- 🔧 **Pre-configured**: All tools and dependencies ready to go
- 👥 **Consistent**: Everyone gets the identical development environment

Codespaces aren't intended to completely replace programming on your own machine if you're working on a large number of projects or with huge datasets/tech specifications, but they are a very useful addition to your professional toolbox.

## Instructions
1. In the upper right-hand corner, click the green "Use this template" button and then select "Create new repository."
2. Make sure that the "Include all branches" slider is set to ON.
   ![Screenshot of "Create new repository" page demonstrating the "Include all branches" slider as set to ON.](https://github.com/ECON-691/quickstart-for-codespaces/blob/main/public/images/screenshot-newrepo.png)
   Give your repository a name (quickstart-for-codespaces works) and a short description ("Clone of ECON-691/quickstart-for-codespaces for Tech Tacos" is an easy example). Leave visibility as "Public," and then click the green "Create repository" button at the bottom of the page.

### Choose Your Learning Path

#### 🎨 **Haikus for Codespaces** (Start Here!)
Get familiar with GitHub Codespaces by editing a silly example website with Node.js, EJS templates, and CSS.

**👉 [Start the Haikus Codespace Tutorial](TUTORIAL-HAIKUS.md)** (right-click to open in a new tab!)

*Time: 30-45 minutes | Technologies: JavaScript, HTML, CSS*

#### 🐍 **Python Data Visualization** 
Build on your Codespaces knowledge by working with an interactive expense tracking chart with Python.

**👉 [Start the Python Codepsace Tutorial](TUTORIAL-PYTHON.md)** (right-click to open in a new tab!)

*Time: 45-60 minutes | Technologies: Python, matplotlib, pandas*  
*Prerequisites: Complete the Haikus tutorial first*

## Additional Resources
- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
- [GitHub Student Developer Pack](https://education.github.com/pack/)
- [Datacamp - Introduction to GitHub Codespaces](https://www.datacamp.com/tutorial/github-codespaces)
- [Microsoft Learn - Code with GitHub Codespaces](https://learn.microsoft.com/en-us/training/modules/code-with-github-codespaces/)
- [Visual Studio Code - GitHub Codespaces](https://code.visualstudio.com/docs/remote/codespaces)
- *More about Javascript*
    - [Setting up a Node.js project for GitHub Codespaces](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-nodejs-project-for-codespaces)
    - [Node.js Tutorial](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
    - [EJS Templating Guide](https://ejs.co/#docs)
- *More about Python*
    - [Setting up a Python project for GitHub Codespaces](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces)
    - [Matplotlib Documentation](https://matplotlib.org/stable/tutorials/index.html)
    - [Pandas Getting Started Guide](https://pandas.pydata.org/docs/getting_started/index.html)
    - [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
    - [Jupyter Notebooks on the web](https://code.visualstudio.com/docs/datascience/notebooks-web)

## What's Next?
Having fun with the haikus web development? Consider adding new haiku categories or themes, making styling improvements with advanced CSS, or adding a suggestion box for user-submitted haikus (advanced, but might be fun to try!). 

Wanting to learn more python? Try customizing the expense categories in the Python code, experiment with different chart colors, exploring more advanced data visualizations, or saving expense data from different days and making a daily tracker.

