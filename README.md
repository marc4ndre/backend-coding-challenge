# Coveo Backend Coding Challenge

# Requirements
- pip install awsebcli

# Local setup
To prepare your setup for deployment, follow those simples steps:

- create a virtual environment
```bash
$ virtualenv env
```
- Activate the environment
```bash
$ source env/bin/activate
```
- Install requirements
```bash
$ pip install -r requirements.txt
```

# Deployment
Starting deployment on aws elastic beanstalk ( make sure to install requirements first )
```bash
$ eb create [environment]
```
you can pick the environment name of your choice. Once deployment is done
you can do the following command which will open a browser on the
aws address. The only thing left to get a suggestion out of it is to add
/suggestions?q=... to your browser path.
```bash
$ eb open
```

Stopping
```bash
$ eb terminate [environment]
```

# Unit test
To run all the unit test, you can simply type in a shell on the root path of the project:
```bash
$ python -m unittest discover -v
```

