Provisioning a new site

## Required packages:

+ nginx
+ python 3.6
+ virtualenv + pip
+ Git

eg  on Ubuntu:

​			sudo add-apt-repository ppa:fkrull/deadsnakes

​			sudo apt-get install nginx git python3.6 python3.6-venv

## Nginx Virtual Host config

+ see nginx.template.config
+ replace SITENAME with e.g., staging.my-domain.com

## Systemd service

+ see gunicron-systemd.template.service
+ replace SITENAME with e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username/sites/39.107.110.80

├─database
├─static
│  └─bootstrap
│      ├─css
│      └─js
├─superlists
│  ├─deploy_tools
│  ├─functional_tests
│  │  └─__pycache__
│  ├─lists
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  ├─static
│  │  │  └─bootstrap
│  │  │      ├─css
│  │  │      └─js
│  │  ├─templates
│  │  └─__pycache__
│  └─superlists
│      └─__pycache__
└─virtualenv