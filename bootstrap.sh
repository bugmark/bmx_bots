#!/usr/bin/env bash

echo "Download gem installer"
gem install specific_install

echo "Remove old gems"
gem uninstall bmx_api_ruby
gem uninstall bmx_cl_ruby 

echo "Install/Upgrade Bugmark CLI"
gem specific_install http://github.com/bugmark/bmx_api_ruby
gem specific_install http://github.com/bugmark/bmx_cl_ruby

echo "Create configuration for localhost"
echo "(You'll have to tweak the hostname and scheme)"
bmx config set --usermail=admin@bugmark.net --password=bugmark 

bmx help
