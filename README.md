# analysis_project_template
This is a sample template meant to be used for workflows centered around notebooks

## Why you should use this template
This template is meant to give you the basic setup of an "analysis" repository, focused on storing notebooks or other pieces of scientific code/documentation. This repository is not meant to be a "one size fits all" repository, but rather, a starting point from which the user can build upon.

## Essential checklist for your repository
- [ ] Software license
- [ ] Detailed readme
- [ ] Update the environment.yml file in include the required libraries/packages
- [ ] Your analysis code/notebooks!

## Choosing a license for this repository
There are a variety of software licenses to choose from. The default for this
repository is the [MIT License](https://opensource.org/licenses/MIT) which is short
and to the point. If you are interested in learning more about which license is
best for you, check out [this resource](https://choosealicense.com/) to help you
determine which is best for your specific needs, or consult [UCAR Legal](https://internal.ucar.edu/counsel/about)

## What to include in your README (README.md)
Once you copy over this template and choose your license, you should populate your README file. This file serves as a landing page for your repository and should provide the following:
- Title of the project
- Introduction and overview of what the analysis covers
- How to contribute
- How to reproduce the conda environment

An example of this is given below
```
# Climate-Analysis
This is a repository meant to show how to do climate analysis.

## Contributing
Clone this repository to your account, then create your own branch to work in

"git checkout -b <nameofyourbranch>"


## Reproducing the environment

"conda env create -f envs/environment.yml"
"conda activate environment_name"


```

## The importance of software citation and minting a DOI
Once your repository is built and you have added your analysis, you may want to mint a DOI for your project, so you can share your work with the community AND receive credit for doing so.

Directions on how to mint a DOI for your project can be found on the [NCAR Software Citation Documentation](https://ncar.github.io/software-citation/pages/recommendation/mint-doi.html)
