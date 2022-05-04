MODULES_DIR="modules"

if [ -d "$MODULES_DIR" ]; then
    rm -rf $MODULES_DIR
fi

python main.py testing

cd $MODULES_DIR

for d in */ ; do 
    cp ../test_tf_files/dev.auto.tfvars ./$d
    echo "\n$d"
    cd $d

    echo "-> Running 'terraform init'"
    INIT_RESULT=$(terraform init)

    if [[ "$INIT_RESULT" != *"successfully initialized"* ]]
    then
        echo "--> Initialization failed."
        exit 0
    else
        echo "--> Successful initialization."
    fi

    cd ..
done

echo "\nAll tests passed."
cd ..

echo "\nResetting module directories..."
./runner.sh