# A KHIS module to analyze facilities from the KMHFL 
#### This module utilizes the <b> Streamlit <b> App Framework
## Project Organization

```
KMHFL_HACKATHON/
    |- __pycache__/
    |- apps/
    |  |- bars.py
    |  |- charts.py
    |  |- map.py 
    |- venv 
    |- app.py 
    |- multiapp.py 
    |- README.md
    |- requirements.txt
```
# Development
To run any commands ensure that the current working directory is the root of the project

# Requirements
The app requires Python version 3.8 or newer installed on your system.     

Python can be downloaded from [Python Official Site](https://www.python.org/downloads/)
# Getting Started
## Pip Installation
### On Linux and Mac OS X
``` bash
   $ python get-pip.py 
```
### On Windows OS   
``` bash
   $ py get-pip.py 
```
## Create a Virtual Environment
In the current working directory create a venv directory.
``` bash
$ python3 -m venv [virtualEnvironmentName]
```
<b>Activate the Virtual Environment using:<b>
``` bash
$ source venv/bin/activate
```
## Install required Packages
``` bash 
$ pip install -r requirements.txt
```
## To Run the application run the following command
```bash 
$ streamlit run [filename]
``` 
For example,
``` $ streamlit run app.py```

**The app will run on the following url:**
 ``` bash 
     Local URL:http://localhost:8501
     Network URL:http://192.168.42.90:8501