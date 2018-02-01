#!/usr/bin/env bash

echo "Download gem installer"
gem install specific_install

echo "Install/Upgrade Bugmark CLI"
gem specific_install http://github.com/bugmark/bmx_api_ruby
gem specific_install http://github.com/bugmark/bmx_cl_ruby

echo "Create configuration for localhost"
bmx config set --scheme=https --host=localhost --usermail=admin@bugmark.net --password=bugmark 

echo "Show Bugmark host info"
bmx host info

echo "Show database counts"
bmx host counts
