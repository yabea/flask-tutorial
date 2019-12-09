ln -s /app/nginx.conf /etc/nginx/conf.d/
nginx && uwsgi --ini uwsgi.ini

python3 serve.py
