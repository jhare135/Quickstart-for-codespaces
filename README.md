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

## Haikus for Codespaces
This tutorial is a modification of [Quickstart for GitHub Codespaces](https://docs.github.com/en/codespaces/getting-started/quickstart), which provides a tour of using codespaces with the [github/haikus-for-codespaces](https://github.com/github/haikus-for-codespaces) repo. This project uses JavaScript (Node.js), HTML templating (EJS), and CSS for styling to create a fun little webpage, but you don't have to actually know any of these programming languages in order to work with this tutorial and learn more about codespaces.

### Instructions
1. In the upper right-hand corner, click the green "Use this template" button and then select "Create new repository."
2. Make sure that the "Include all branches" slider is set to ON.
   ![Screenshot of "Create new repository" page demonstrating the "Include all branches" slider as set to ON.](https://github.com/ECON-691/quickstart-for-codespaces/blob/main/public/images/screenshot-newrepo.png)
   Give your repository a name (quickstart-for-codespaces works) and a short description ("Clone of ECON-691/quickstart-for-codespaces for Tech Tacos" is an easy example). Leave visibility as "Public," and then click the green "Create repository" button at the bottom of the page.
3. Please open [Quickstart for GitHub Codespaces](https://docs.github.com/en/codespaces/getting-started/quickstart) in a separate tab from this README set of instructions.
4. Read just the "Introduction" section; then come back to this instructions page.
5. Click the green "<> Code" button and then click "Create codespace on main." Wait for the Codespace to load, which might take a few minutes! **You should now have 3 tabs open: A) these repo instructions, B) the GitHub document on getting started with codespaces, and C) the codespace itself.**
6. In Tab B (the GitHub document tutorial), scroll down to "Running the application." Follow the instructions to run the `npm run dev` command in the codespace (Tab C) and open the port in a new browser tab. **You should now have a 4th tap open: D) a webpage with haikus and pics of Octocat!**
7. Back in Tab B (GitHub tutorial), continue with "Edit the application" section. For the instruction "Edit the text field of the first haiku to personalize the application," simply **change the city** in the first poem from "seattle" to your favorite city.
8. Follow the "Committing and pushing your changes" section in Tab B. After you commit, you'll see a "Sync changes" option (not "publish new branch" since you're using an existing repo).

## Additional Resources
- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
- [Node.js Tutorial](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- [EJS Templating Guide](https://ejs.co/#docs)

## What's Next?
Ready for more? Check out the `python` branch of this repository to explore data visualization with Python while keeping the same familiar Codespaces workflow!
