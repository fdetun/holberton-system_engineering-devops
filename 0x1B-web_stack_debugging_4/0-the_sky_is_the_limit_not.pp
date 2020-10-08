# there is no limit

exec { 'limit vers l infini':
provider => 'shell',
command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx && service nginx restart',
}
