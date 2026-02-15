from setuptools import find_packages,setup
from typing import List

Hyphen_e_dot='-e . '
def get_requirements(file_path:str)->List[str]:
    '''
    file_path is the parameter and : str means it should be a string
    -> List[str] ,meaning:This function will return a List of strings.
    {Define a function named get_requirements
It takes a string argument called file_path
It returns a list of strings}
["pandas", "numpy", "scikit-learn"]

    '''
    requirements=[]
    #creating an empty list. To store all package names from requirements.txt.



    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)

    return requirements
'''
 It reads dependencies from requirements.txt, removes newline characters,
 filters out the editable install flag (-e .), and returns a clean
 list of package names.
'''
'''
requirements.txt
        ↓
readlines()
        ↓
remove \n
        ↓
remove "-e ."
        ↓
return list of packages

'''
setup(
    name='mlproject1',
    version='0.0.1',
    author='Nishtha',
    author_email='nishthajain0306@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')

)

'''
Why do you use -e . in ML projects?

Answer:

It installs the current project in editable mode, allowing immediate
reflection of code changes without reinstalling the package. It helps 
maintain modular and production-ready structure.
'''