#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

export APPTAINER_CACHEDIR=$SCRIPT_DIR/cache
export TMPDIR=$SCRIPT_DIR/tmp

if [ ! -e $APPTAINER_CACHEDIR ]; then
    echo "Create a directory or symlink called $APPTAINER_CACHEDIR for the apptainer cache"
    echo "The total space needed may be as large as 30G"
    exit 1
fi

if [ ! -e $TMPDIR ]; then
    echo "Create a directory or symlink called $TMPDIR as a temporary directory"
    echo "The total space needed may be as large as 80G"
    exit 1
fi

apptainer build nemo.sif nemo.recipe

