#!/bin/bash

# run fuzzer
export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/apache2/lib/:$LD_LIBRARY_PATH

AFL_MAP_SIZE=256000 \
SHOW_HOOKS=1 \
ASAN_OPTIONS=detect_leaks=0,abort_on_error=1,symbolize=1,debug=true,check_initialization_order=true,detect_stack_use_after_return=true,strict_string_checks=true,detect_invalid_pointer_pairs=2 \
AFL_DISABLE_TRIM=1 \
 $PWD/../install_dir/bin/httpd -X -f $PWD/conf/default.conf

