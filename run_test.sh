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
	[description]="test for launch_agent.sh"
	[calling]="./`getScriptName $0`"
)

# Show main script info
showScriptInfo

# MAIN
#./src/launch_agent.sh src/agent1.py ABC 100 100

exec src/launch_month.sh test/launch_month.sh 2023 2
