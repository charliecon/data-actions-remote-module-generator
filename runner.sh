MODULES_DIR="modules"

if [ -d "$MODULES_DIR" ]; then
    rm -rf $MODULES_DIR
fi

python main.py