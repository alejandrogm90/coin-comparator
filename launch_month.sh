#!/bin/bash

# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd `dirname $0` && pwd)
source "ssh_examples/scripts/commonFunctions.sh"
SCRIPT_NAME=`getJustStriptName $0`
export LOG_FILE=${DIR_HOME}"/"${SCRIPT_NAME}"_"`date +%F`".log"
SCRIPT_1="./coinlayer/get_day_sqlitle.py"

echo "" > $LOG_FILE

declare -A script_info
export script_info=(
	[name]="${SCRIPT_NAME}" 
	[location]="${DIR_HOME}" 
	[description]="A simple monthly scrit to get al data of one month" 
	[calling]="./`getStriptName $0` [YEAR] [MONTH]"
)

showScriptInfo

if [ $# -ne 2 ] ; then 
    echo " $0 [YEAR] [MONTH]"
    showError 1 "$(date -u) [ERROR]: Number of incorrect parameters.Must be 2"
else  
    if [ `isValidDate $1 $2` -ne 1 ] ; then    
        showError 2 "Is not a valid date"
    else
        respuesta=0
        for day in `getAllDatesOfOneMonth $1 $2` ; do 
            echo "Saving day: "$day
            $SCRIPT_1 $day
            respuesta=$?
            if [ $respuesta -eq 0 ] ; then
                echo "`date +%F' '%T` [MSG]: Completed $SCRIPT_1 $day" >> $LOG_FILE
            else
                echo "`date +%F' '%T` [ERROR]: $SCRIPT_1 $day" >> $LOG_FILE
                break
            fi
        done
        if [ $respuesta -eq 0 ] ; then $echo $day" DONE ...." ; fi
    fi
fi 
