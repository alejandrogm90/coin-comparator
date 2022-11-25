#!/bin/bash

# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd `dirname $0` && pwd)
source "commons/commonFunctions.sh"
SCRIPT_NAME=`getJustStriptName $0`
export LOG_FILE=${DIR_HOME}"/"${SCRIPT_NAME}"_"`date +%F`".log"
SCRIPT_1="./coinlayer/get_day_sqlitle.py"

declare -A script_info
export script_info=(
	[name]="${SCRIPT_NAME}" 
	[location]="${DIR_HOME}" 
	[description]="A simple monthly scrit to get al data of one month" 
	[calling]="./`getStriptName $0` [YEAR] [MONTH]"
)

showScriptInfo

echo "" > $LOG_FILE

if [ $# -ne 2 ] ; then
    showError 1 "Number of incorrect parameters. $0 [YEAR] [MONTH]"
else  
    if [ `isValidDate $1 $2` -ne 1 ] ; then    
        showError 2 "Is not a valid date YYYY-MM-DD"
    else
        for day in `getAllDatesOfOneMonth $1 $2` ; do 
            showInfo "Saving day: "$day
            $SCRIPT_1 $day
            respuesta=$?
            if [ $respuesta -eq 0 ] ; then
                showInfo "Completed $SCRIPT_1 $day"
            else
                showWarn "$SCRIPT_1 $day"
            fi
        done
    fi
fi 
