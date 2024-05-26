# Ensure the ~/.ssh directory exists with the correct permissions
file { '/home/vagrant/.ssh':
  ensure => directory,
  owner  => 'vagrant',
  group  => 'vagrant',
  mode   => '0700',
}

# Ensure the SSH config file exists with the correct permissions
file { '/home/vagrant/.ssh/config':
  ensure => file,
  owner  => 'vagrant',
  group  => 'vagrant',
  mode   => '0600',
}

# Add configuration to use the private key ~/.ssh/school
file_line { 'Declare identity file':
  path  => '/home/vagrant/.ssh/config',
  line  => '  IdentityFile ~/.ssh/school',
  match => '^\s*IdentityFile\s+',
}

# Add configuration to refuse password authentication
file_line { 'Turn off passwd auth':
  path  => '/home/vagrant/.ssh/config',
  line  => '  PasswordAuthentication no',
  match => '^\s*PasswordAuthentication\s+',
}
