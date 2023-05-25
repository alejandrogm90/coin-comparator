#!/bin/bash

# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd `dirname $0` && pwd)
source "$DIR_HOME/commons/common_functions.sh"
DIR_LOG="`dirname $DIR_HOME`/log"
SCRIPT_NAME="`getJustStriptName $0`"
export LOG_FILE="${DIR_LOG}/${SCRIPT_NAME}_`date +%F`.log"
declare -A script_info
export script_info=(
	[name]="${SCRIPT_NAME}"
	[location]="${DIR_HOME}"
	[description]="A simple monthly scrit to get al data of one month"
	[calling]="./`getScriptName $0` [CONNECTOR] [YEAR] [MONTH]"
)

# Show main script info
showScriptInfo

# MAIN
if [ $# -ne 3 ] ; then
    showError 1 "Number of incorrect parameters. [CONNECTOR] [YEAR] [MONTH]"
else
    if [ ! -f "$1" ] ; then
        showError 2 "Connector $1 do not exist"
    elif [ "`isValidDate $2 $3`" == "0" ] ; then
        showError 3 "Is not a valid date YYYY-MM-DD"
    else
        for day in `getAllDatesOfOneMonth $2 $3` ; do
            $1 "$day"
            respuesta=$?
            if [ $respuesta -eq 0 ] ; then
                showInfo "Completed $1 $day"
            else
                showWarn "ERROR in $1 $day"
            fi
        done
    fi
fi 
