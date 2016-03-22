# Django Mogo

Starter kit for Django 1.8 projects. This is a bunch of stuff put thogether to make a good starting base for Django 1.8 projects.

This script installs Python and Django modules as well as usefull static stuff ( jquery, font-awesome ) and base templates. It also autogenerates a settings file.

## Features

This quick start kit installs the following Django modules:

#### Image processing

- [pillow](https://github.com/python-pillow/Pillow): standard image processing lib
- [sorl-thumbnail](https://github.com/mariocesar/sorl-thumbnail): generate thumbnails using cache

#### Authentication

- [django-allauth](https://github.com/pennersr/django-allauth) for authentication with social networks

#### Text editors

- [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor): wysywig text editor
- [django-codemirror2](https://github.com/sk1p/django-codemirror2): code editor

#### Content management

- [django-alapage](https://github.com/synw/django-alapage) for pages management
- [django-jssor](https://github.com/synw/django-jssor) for slideshows management
- [django-zongo](https://github.com/synw/django-zongo) for responsive presentations

#### Utilities

- [ipython](http://ipython.org/) : powerfull python shell integrated with Django
- [pytz](http://pytz.sourceforge.net/): timezones
- [django-reversion](https://github.com/etianen/django-reversion) for version control
- [django-mptt](https://github.com/django-mptt/django-mptt): utility for working with trees
- [django-braces](https://github.com/brack3t/django-braces): usefull mixins
- [django-mqueue](https://github.com/synw/django-mqueue): for logging app events 
- [django-dirtyedit](https://github.com/synw/django-dirtyedit): uility for editing files in the admin interface

#### Bootstrap stuff

- [django-admin-bootstraped](https://github.com/django-admin-bootstrapped/django-admin-bootstrapped) for the admin interface
- [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form)
- [django-bootstrap3](https://github.com/dyve/django-bootstrap3)

#### Test / debug

- [django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar) for apps debug
- [django-nose](https://github.com/django-nose/django-nose): utilities for tests
- [coverage](https://bitbucket.org/ned/coveragepy): utility for test coverage reporting

#### Static files

Batteries are included:

- Jquery
- Font Awesome icons
- Base valid Xhtml 1.0 Strict templates using Bootstrap.
- Some usefull generic css classes

## Install

  ```bash
mkdir PROJECT_NAME
cd PROJECT_NAME
wget https://raw.githubusercontent.com/synw/django-mogo/master/install.sh
chmod a+x install.sh
./install.sh PROJECT_NAME
rm -f install.sh
  ```

Tweak the autogenerated `settings.py` to fit your needs.

Initiate the instance:

  ```bash
source bin/activate
cd PROJECT_NAME
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
  ```

It's ready: go to `/admin` , start creating pages and customizing the templates

## Todo

- [ ] Language option in the installer
- [ ] Better templates





