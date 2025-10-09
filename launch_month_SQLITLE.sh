#!/bin/bash

# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd $(dirname $0) && pwd)
source "$DIR_HOME/src/common_utils/common_functions.sh"
DIR_LOG="$(dirname $DIR_HOME)/log"
SCRIPT_NAME="$(getJustStriptName $0)"
CONNECTOR="src/connectors/connector_coinlayer_sqlittle.py"
# export LOG_FILE="${DIR_LOG}/${SCRIPT_NAME}_$(date +%F).log"
declare -A script_info
export script_info=(
    [name]="${SCRIPT_NAME}"
    [location]="${DIR_HOME}"
    [description]="A simple monthly scrit to get al data of one month"
    [calling]="./$(getScriptName $0) [YEAR] [MONTH]"
)

# Show main script info
show_script_info

# MAIN
if [ $# -ne 2 ]; then
    showError 1 "Number of incorrect parameters. [YEAR] [MONTH]"
else
    YEAR=$1
    MONTH=$2
    for day in $(getAllDatesOfOneMonth $YEAR $MONTH); do
        # echo "pipenv run python $CONNECTOR $day"
        pipenv run python $CONNECTOR $day
        respuesta=$?
        if [ $respuesta -eq 0 ]; then
            showInfo "Completed $day"
        else
            showWarn "ERROR in $day"
        fi
    done
fi
