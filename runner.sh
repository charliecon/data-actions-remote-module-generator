DATA_ACTIONS_PATH=$1
DESTINATION="modules"

if [ -d "$DESTINATION" ]; then
    rm -rf $DESTINATION
fi
 
python main.py $DATA_ACTIONS_PATH
