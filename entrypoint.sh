#!/bin/sh

# Replace the html as environment varibles
sed -i "s/{{ content }}/${CONTENT}/g" /usr/share/nginx/html/index.html
sed -i "s/{{ about }}/${ABOUT}/g" /usr/share/nginx/html/index.html

# Start the nginx server with the 'daemon off' option, which means it will run in the foreground
nginx -g 'daemon off;'
