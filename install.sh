#!/bin/bash

#~ usage: $ ./install.sh my_project_name

if 	[ $# -eq 0 ]	
        then
        	echo "You need to provide a project name"
        	exit 1
        else
        	echo "Starting Django Mogo installation"
 fi

echo "====================================== Creating virtualenv ====================================="
virtualenv --no-site-packages . && source bin/activate
pip install --upgrade pip

#~ project creation
echo "======================================= Installing Django =======================================" 
pip install 'django>=1.8.0,<1.9.0'
django-admin startproject $1
cd $1

#~ install modules
echo "==================================== Installing python modules =================================="
pip install ipython pillow python-memcached bleach django-debug-toolbar django-nose coverage django-braces django-autofixture django-crispy-contact-form django-admin-bootstrapped django-bootstrap-form django-bootstrap3 django-mptt django-allauth pytz sorl-thumbnail django-ckeditor django-codemirror2 django-reversion django-jssor django-filebrowser-no-grappelli django-app-namespace-template-loader django-blog-zinnia django-mqueue  
mkdir media
mkdir media/uploads #~ for filebrowser
mkdir media/jssor
mkdir media/jssor/thumbnails
pip install git+https://github.com/django-blog-zinnia/zinnia-theme-bootstrap.git
git clone https://github.com/synw/django-zongo.git && mv django-zongo/zongo . && mkdir media/zongo && rm -rf django-zongo
git clone https://github.com/synw/django-alapage.git && mv django-alapage/alapage . && rm -rf django-alapage
git clone https://github.com/synw/django-dirtyedit.git && cp -r django-dirtyedit/dirtyedit . && rm -rf django-dirtyedit
#git clone https://github.com/synw/django-mqueue.git && mv django-mqueue/mqueue . && rm -rf django-mqueue
git clone https://github.com/synw/django-mbase.git && mv django-mbase/mbase . && rm -rf django-mbase
git clone https://github.com/synw/django-mgof.git && mv django-mgof/mgof . && rm -rf django-mgof

#~ static stuff
echo "=============================== Installing external static files ================================"
mkdir static && cd static && mkdir js && mkdir icons
cd js && wget http://code.jquery.com/jquery-2.1.4.min.js
cd ../

#~ config
echo "================== Installing config files, templates and internal staticfiles =================="
git clone https://github.com/synw/django-mogo.git
rm -f $1/urls.py && mv django-mogo/urls.py $1
mv django-mogo/static/css static
mv django-mogo/static/js/utils.js static/js
mv django-mogo/templates .

echo "==================================== Generating settings ==========================================="
rm -f $1/settings.py
touch $1/settings.py
mv django-mogo/create_settings.py .
python create_settings.py $1
rm -rf django-mogo
rm -f create_settings.py
echo "Settings generated for project $1"
echo ">>> Installation completed"







	

 
