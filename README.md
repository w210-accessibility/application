# Local Development instructions
1. Open your terminal or command prompt
2. If you don't have it already, pip install virtualenv
3. Change directory into outer folder of this repo and create new virtualenvironment called "virt" by running
	virtualenv virt
(note that if you give it a different name, you need to add that new name to the .gitignore).
4. Activate your virtualenv:
	source/bin/activate
5. Install all packages in requirements file to your virtualenv:
	pip install -r requirements.txt
6. Run
	python application.py
to start your local application
7. If you install new Python packages and add new code that requires them, remember to
	pip freeze > requirements.txt
before pushing your code.
8. Commit all new code to a feature branch. Push that feature branch and open a new pull request on github when you want to merge it in. 
