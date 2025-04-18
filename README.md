# CORE-Balancer (Cycle Optimization & Resource Balancer)

-----------

## Table of Contents

- [CORE-Balancer (Cycle Optimization \& Resource Balancer)](#core-balancer-cycle-optimization--resource-balancer)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Environment Setup](#environment-setup)
    - [Prerequisites](#prerequisites)
    - [Installation steps](#installation-steps)
    - [Dependency groups](#dependency-groups)
  - [Branching strategy](#branching-strategy)
    - [Branching strategy workflow (instructions)](#branching-strategy-workflow-instructions)
    - [Conventional commits list](#conventional-commits-list)
  - [Repository Structure](#repository-structure)
    - [Subdirectories overview](#subdirectories-overview)

## Introduction

CORE-Balancer is a Python-based system designed to optimize the supply chain of the Micron Technology Inc. semiconductor manufacturing process. It focuses on the cycle time and both inventory and resource balancing of the production process.
The system consists of a graphical user interface (_GUI_) built int _PyQt5_, which allows users to interact with the optimization model and visualize the results presented supply chain data and analysis.
The optimization model is implemented using the _PuLP_ library, which provides a high-level interface for defining and solving linear programming problems. The system is designed to be modular and extensible, allowing for easy integration of new features and improvements in the future.

## Environment Setup

Although this project should be "installed" through the [_core-balancer-setup.sh_](https://drive.google.com/file/d/1bwDlIBD4AmIf4Xa3jrCRAJl-3-BzjjRw/view?usp=drive_link) script provided by the Python Development department, it is important to know how to set up the environment manually in case of any issues with the script.

### Prerequisites

- Python (3.12)
- pip (Python package manager)
- git (version control system)

### Installation steps

1. Create a new directory for the project:

```bash
    mkdir <your-local-directory>
    cd <your-local-directory>
```

2. Clone the repository:

```bash
    git clone https://github.com/Gabbo0709/core-balancer.git <your-local-directory>
```

3. Create a virtual environment (optional but _strongly_ recommended):

```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    cd <the-repository-directory>
```

4. Install the required dependencies required for your role (these are listed in the [dependency groups section](#dependency-groups) below):

```bash
    pip install -e .[<dependency-group>]
```

5. After finishing the installation, you can start developing the project. If you are using a virtual environment, make sure to activate it before running any scripts or commands related to the project.

### Dependency groups

The project uses a `pyproject.toml` file to manage its dependencies. The dependencies are organized into groups, which can be installed separately based on your role in the project. The available groups are:

- `base`: The base group contains the core dependencies required for development and testing. This group is required for all developers and should be installed first.
- `testing`: The dev group contains dependencies required for advanced testing and development. This group is optional and can be installed if you need additional tools or libraries for your development work.
- `analysis`: The analysis group contains dependencies required for data analysis, exploration and visualization. This group is optional and can be installed if you need additional tools or libraries for your data analysis work.
- `ml`: The ml group contains dependencies required for machine learning and data science. This group is optional and can be installed if you need additional tools or libraries for your machine learning work.
- `forecasting`: The forecasting group contains dependencies required for time series forecasting and analysis. This group is optional and can be installed if you need additional tools or libraries for your forecasting work.
- `ui`: The ui group contains dependencies required for the graphical user interface (GUI) development. This group is optional and can be installed if you need additional tools or libraries for your GUI development work.
- `database`: The database group contains dependencies required for database management and interaction. This group is optional and can be installed if you need additional tools or libraries for your database work.
- `docs`: The docs group contains dependencies required for documentation generation and management. This group is optional and can be installed if you need additional tools or libraries for your documentation work.
- `dev`: The dev group contains dependencies required for development and testing. This group is optional and can be installed if you need additional tools or libraries for your development work. It contains the following groups: `base`, `testing` and `ui`.
- `data`: The data group contains dependencies required for data management and interaction. This group is optional and can be installed if you need additional tools or libraries for your data work. It contains the following groups: `base`, `analysis`, `ml`, `forecasting` and `database`.
- `all`: The all group contains all the dependencies required for development, testing, analysis, machine learning, forecasting, GUI development, database management and documentation generation. This group is optional and can be installed if you need all the tools or libraries for your work. It contains the following groups: `base`, `testing`, `analysis`, `ml`, `forecasting`, `ui`, `database` and `docs`.

## Branching strategy

The repository uses the [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/) branching strategy. The main branches are:

- `main`: The main branch contains the stable version of the code. It is the default branch and should always be in a deployable state.
- `develop`: The develop branch is used for development and contains the latest changes that are being worked on. It is the branch where new features and bug fixes are merged before being released to the main branch.
- `feature/*`: Feature branches are used to develop new features or improvements. They are created from the develop branch and should be merged back into the develop branch when the feature is complete.

### Branching strategy workflow (instructions)

1. Create a new branch from the `develop` branch for your feature:

```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them to you feature branch:

```bash
    git add . || git add <specific-files>
    git commit -m "[<type>] <description for the commit>"
```

3. Push your changes to the remote repository:

> The type of the commit are listed in the [conventional commits list](#conventional-commits-list) below.

```bash
    git push origin feature/your-feature-name
```

4. Create a pull request (PR) from your feature branch to the develop branch. In the PR description, provide a summary of the changes made and any relevant information for reviewers.

> All PRs should be reviewed by at least one other developer before being merged into the develop branch. The reviewer should check for code quality, adherence to coding standards, and any potential issues.

5. Once the PR is approved and merged by the reviewer, delete the feature branch to keep the repository clean:

```bash
    git branch -d feature/your-feature-name
    git push origin --delete feature/your-feature-name
```

### Conventional commits list

The following is a list of conventional commit types that _must_ be used in the project:

- `[feat]`: A new feature or improvement.
- `[fix]`: A bug fix or issue resolution.
- `[docs]`: Documentation changes or updates.
- `[style]`: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc.).
- `[refactor]`: A code change that neither fixes a bug nor adds a feature.
- `[add]`: A new file or directory added to the project.
- `[remove]`: A file or directory removed from the project.
- `[test]`: Adding or updating tests.
- `[chore]`: Changes to the build process or auxiliary tools and libraries such as documentation generation.
- `[ci]`: Changes to the CI/CD configuration files and scripts.

Aditional to the conventional commit types, the following prefixes are also allowed for involved departments:

- Data management and testing department: `[data]`
- Data analysis department: `[analysis]`
- GUI development department: `[gui]`
- Product development department: `[product]`
- Linear programming and modeling department: `[lp]`
- Python development department: `[dev]`

> All commit messages should be written in the imperative mood, starting with a capital letter. The message should be concise and descriptive, providing enough information for other developers to understand the changes made.

For reference, here are some examples of commit messages that follow the conventional commit format:

```bash
    [feat] Add new feature to improve performance
    [fix] Fix bug in the LP model that caused incorrect results
    [docs] Update README.md with installation instructions
    [style] Fix whitespace issues in the code
    [refactor] Refactor data loading code for better readability
    [add] Add new test cases for data validation
    [remove] Remove unused functions from the codebase
    [test] Add unit tests for the optimization model
    [chore] Update dependencies to latest versions
    [ci] Update CI/CD configuration for better performance
```

## Repository Structure

The repository directories are structured as follows:
> The following structure is a simplified version of the actual repository structure. The actual repository may contain additional files and directories not listed here.
> The final repository structure will be updated to include aditional directories and files as the project progresses.

``` bash
CORE-Balancer
└── core-balancer <- You are here
    ├── data
    ├── docs
    ├── scripts
    ├── tests
    └── src
        └── core_balancer
            ├── analysis
            ├── data
            ├── gui
            ├── optimization
            └── utils
```

### Subdirectories overview

- `data`: Contains the data files used in the project.
- `docs`: Contains the documentation files.
- `scripts`: Contains auxiliary scripts useful for development and/or maintenance.
- `tests`: Contains the test code for the project.
- `src`: Contains the source code of the project.
  - `core_balancer`: Contains the main source code for the project.
    - `analysis`: Contains the data and sensitivity analysis code.
    - `data`: Contains data load, validation and preprocessing code.
    - `gui`: Contains the _PyQt5_ graphical user interface code.
    - `optimization`: Contains the LP model logic and solver implementation code.
    - `utils`: Contains utility functions and classes shared across the project.

If you whish to check out each directory overview in detail, there will be a README file in each directory with a detailed description of the directory and its contents.
> The README files in each directory will be updated as the project progresses to include additional information and details about the directory and its contents.
