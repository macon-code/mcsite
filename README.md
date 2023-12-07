# Macon Code Website <!-- omit in toc -->

The website for Macon Code, developed by volunteers of Macon Code to share information about the group. The website offers information about:
- How to join meetings and the Slack channel
- Current, past, and planned projects
- How to suggest new projects
- Our mission and history as an organization
- Community partners

## Table of Contents <!-- omit in toc -->
- [Building](#building)
	- [Virtual environment](#virtual-environment)
	- [Development server](#development-server)
- [Contributing](#contributing)
- [License](#license)

## Building

### Virtual environment

It is recommended to use a virtual environment while developing. Using the latest version of Python, you can create a virtual environment by running:

```
python -m venv .env
```

Activate the environment by running:


(bash): 
```
source .env/bin/activate
```
(command prompt):
  ```
  .env/bin/activate.bat
  ```
(powershell):
```
.env/bin/activate.ps1
```

When finished, either close your terminal or deactivate the environment by running:

```
deactivate
```

### Development server

Within your virtual environment, install dependencies by running:
		
```
pip install -r requirements.txt
```

Start the development server by running:

```
python manage.py runserver
```


## Contributing
1. Fork the repository
2. Create a new branch: 
   ```
   git checkout -b feature_name
   ```
3. Make your changes and commit them: 
   ```
   git commit -m "Description of changes"
   ```
4. Push the changes to your branch: 
   ```
   git push -u origin HEAD
   ```
5. Submit a pull request

When contributing, only include the project files - do not include the virtual environment. 

## License

All rights reserved. 
