.. _scaffolder:

Scaffolder
==========
Colifrapy comes with a scaffolder used to generate code boilerplate. Therefore, a command is automatically added when you install colifrapy with pip.

Usage
-----
To use the scaffolder::

    colifrapy new [name-of-project]

    options :
        {-a/--author: Author of the project}
        {-o/--organization: Organization of the author}

This will generate a standard colifrapy project containing the following files :

    - .gitignore (exluded files for git)
    - requirements.txt (base pip dependencies)
    - README.md (project documentation)
    - [name-of-project].py (command line hub)
    - config/
        - settings.yml (standard settings for your project)
        - strings.yml (externalized strings)
    - model/
        - controller.py (basic controller)
        - example_model.py (basic model)

Every relevant folder will of course come along with its __init__.py file.
