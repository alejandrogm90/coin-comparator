#!/bin/bash
# Example: ./launch_bot.sh src/agents/bot_1.py ABC 100 100
# config: dict, date: str, coin_name: str, cash: float, coins: float):
# pipenv run python src/connector/coinlayer_json.py config/config_agent.json 2024-01-01 ABC 100 100


# VARIABLES AND FUNCTIONS
DIR_HOME=$(cd "$(dirname "$0")" && pwd)
source "$DIR_HOME/src/agents/common_utils/common_functions.sh"
DIR_LOG="$(dirname "$DIR_HOME")/log"
SCRIPT_NAME="$(getJustStriptName "$0")"
export LOG_FILE="${DIR_LOG}/${SCRIPT_NAME}_$(date +%F).log"
declare -A script_info
export script_info=(
    [name]="${SCRIPT_NAME}"
    [location]="${DIR_HOME}"
    [description]="A simple monthly script to get al data of one month"
    [calling]="$@"
)

# Show main script info
show_script_info

# Main
DEFAULT_CONFIG_FILE="config/config_agent.json"
if [ $# -ne 4 ]; then
    showError 1 "Number of incorrect parameters. [BOT] [COIN_NAME] [INITIAL_COINS] [INITIAL_CASH]"
else
    COINS=$3
    CASH=$4
    #for c_date in $(getAllDatesOfOneMonth 2024 1); do
        #reaction=$(pipenv run python "$1" "$DEFAULT_CONFIG_FILE" "$c_date" "$2" "$CASH" "$COINS")
    for c_date in "2022-01-01" "2022-01-02" "2022-01-03" ; do
        reaction=$(python bot_master.py "$1" "$DEFAULT_CONFIG_FILE" "$c_date" "$2" "$CASH" "$COINS")
        echo "REACTION -> $reaction"
        CASH=$(echo "$reaction" | cut -d'|' -f3)
        COINS=$(echo "$reaction" | cut -d'|' -f4)
        echo "$CASH $COINS"
    done
fi
