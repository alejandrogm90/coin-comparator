#!/bin/bash
# Example: ./launch_month.sh src/connector_coinlayer_json.py 2024 01

# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd "$(dirname "$0")" && pwd)
source "$DIR_HOME/src/common_utils/common_functions.sh"
SCRIPT_NAME="$(getJustStriptName "$0")"
#DIR_LOG="$(dirname "$DIR_HOME")/log"
#export LOG_FILE="${DIR_LOG}/${SCRIPT_NAME}_$(date +%F).log"
declare -A script_info
export script_info=(
    [name]="${SCRIPT_NAME}"
    [location]="${DIR_HOME}"
    [description]="A simple monthly scrit to get al data of one month"
    [calling]="./$(getScriptName "$0") [CONNECTOR] [YEAR] [MONTH]"
)

# Show main script info
show_script_info

# MAIN
if [ $# -ne 3 ]; then
    showError 1 "Number of incorrect parameters. [CONNECTOR] [YEAR] [MONTH]"
else
    if [ ! -f "$1" ]; then
        showError 2 "Connector $1 do not exist"
    elif [ "$(isValidDate "$2" "$3")" == "0" ]; then
        showError 3 "Is not a valid date YYYY-MM-DD"
    else
        for day in $(getAllDatesOfOneMonth "$2" "$3"); do
            echo "pipenv run python $1 $day"
            # pipenv run python "$1" "$day"
            respuesta=$?
            if [ $respuesta -ne 0 ]; then
                showWarn "ERROR in $1 $day"
            fi
        done
    fi
fi
