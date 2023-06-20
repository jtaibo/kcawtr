#!/bin/bash
#

if [ $# -lt 3 ]; then
    echo "KCAWTR - scenecheck.sh: Bad arguments"
    exit 1
fi

MAYA_VERSION=$1
MAYA_PROJECT=$2
MAYA_SCENE=$3

MAYA_BIN_DIR="/usr/autodesk/maya${MAYA_VERSION}/bin"

${MAYA_BIN_DIR}/mayapy scenecheck.py "$MAYA_PROJECT" "$MAYA_SCENE"
