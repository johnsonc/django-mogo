#!/bin/bash

#~ usage: $ ./install.sh my_project_name

if [ -z "$1	" ]
        then
        	echo "Starting Django Mogo installation"
        else
        	echo "You need to provide a project name"
        	exit 1
        fi
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
pip install ipython pillow django-debug-toolbar django-nose coverage django-braces django-admin-bootstrapped django-bootstrap-form django-bootstrap3 django-mptt django-allauth pytz sorl-thumbnail django-autoslug django-ckeditor django-codemirror2 django-reversion django-filer
git clone https://github.com/synw/django-jssor.git && mv django-jssor/jssor . && mkdir media && mkdir media/jssor && mkdir media/jssor/thumbnails && rm -rf django-jssor
git clone https://github.com/synw/django-zongo.git && mv django-zongo/zongo . && mkdir media/zongo && rm -rf django-zongo
git clone https://github.com/synw/django-alapage.git && mv django-alapage/alapage . && rm -rf django-alapage
git clone https://github.com/synw/django-dirtyedit.git && cp -r django-dirtyedit/dirtyedit . && rm -rf django-dirtyedit

#~ static stuff
echo "=============================== Installing external static files ================================"
mkdir static && cd static && mkdir js && mkdir icons
cd js && wget http://code.jquery.com/jquery-2.1.4.min.js
cd ../icons && wget https://fortawesome.github.io/Font-Awesome/assets/font-awesome-4.5.0.zip
unzip -qq font-awesome-4.5.0.zip && mv font-awesome-4.5.0 font-awesome && rm -f font-awesome-4.5.0.zip
cd ../..

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


if [ -z "$2" ]
        then
        	echo "==================================== Activating instance ==========================================="
        	./initiate.py $1
        else
        if [[ "$2" == '-na' ]]
                then
                echo ">>> Installation completed ( without database initialisation )"
        fi
 fi




	

 
