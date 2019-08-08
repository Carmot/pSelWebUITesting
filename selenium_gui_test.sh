#!/bin/bash -e
##-------------------------------------------------------------------
## File : selenium_gui_test.sh
## Author : Denny <contact@dennyzhang.com>
## Description :
## --
## Created : <2017-05-18>
## Updated: Time-stamp: <2017-09-04 18:52:17>
##-------------------------------------------------------------------
test_py_script="sysdig_python_selenium_webui_tests.py"

image_name="denny/selenium:v1"
py_script_in_container="sysdig_python_selenium_webui_tests.py"
working_dir="."

[ -d "$working_dir" ] || mkdir -p "$working_dir"

function destroy_container() {
    container_name="sysdig_webui_test"
    # TODO: better implementation
    if docker ps -a | grep "sysdig_webui_test"; then
        docker stop "sysdig_webui_test"; docker rm "sysdig_webui_test"
    fi
}

function shell_exit() {
    errcode=$?
    destroy_container "sysdig_webui_test"
    exit $errcode
}

trap shell_exit SIGHUP SIGINT SIGTERM 0

# Start docker container
destroy_container "sysdig_webui_test"

if [ -z "$add_host" ]; then
    docker run -t -d --privileged -h selenium \
           -v "$test_py_script:$py_script_in_container" \
           --name "sysdig_webui_test" "$image_name"
else
    docker run -t -d --privileged -h selenium \
           --add-host="$add_host" \
           -v "$test_py_script:$py_script_in_container" \
           --name "sysdig_webui_test" "$image_name"
fi

# TODO: better way
sleep 5

# Run test
docker exec "sysdig_webui_test" python "$py_script_in_container"
################################################################################
## File : selenium_gui_test.sh ends