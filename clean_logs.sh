#!/bin/bash

# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd "$(dirname "$0")" && pwd)
source "$DIR_HOME/src/common_utils/common_functions.sh"
DIR_LOG="$(dirname "$DIR_HOME")/log"
SCRIPT_NAME="$(getJustStriptName "$0")"
declare -A script_info
export script_info=(
    [name]="${SCRIPT_NAME}"
    [location]="${DIR_HOME}"
    [description]="A simple cleaner for directory log"
    [calling]="$@"
)

# Show main script info
show_script_info

# MAIN
#if [ "0" != "$(ls -l "$DIR_LOG/"*.log | head -1 | cut -d' ' -f2)" ]; then
#    rm "$DIR_LOG/"*.log
#fi
rm "$DIR_LOG/"*.log
