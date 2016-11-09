# Viimi

init.d Script

/etc/init/gunicorn.conf

description "Gunicorn daemon for Django project"

start on (local-filesystems and net-device-up IFACE=eth0)
stop on runlevel [!12345]

# If the process quits unexpectadly trigger a respawn
respawn

setuid django
setgid django
chdir /home/django/django_project/src

exec /home/django/django_project/venv/bin/gunicorn --error-logfile /home/django/error.log -w 2 -b 127.0.0.1:9000 viimiweb.wsgi:application
