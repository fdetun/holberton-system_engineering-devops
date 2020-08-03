#task 1

exec { 'gem install puppet-lint -v 2.1.1':
    path => '/usr/bin'
}
