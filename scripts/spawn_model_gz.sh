#!/bin/bash

if [ "$#" -lt 5 ]; then
  echo "Usage: spawn_model_gz.sh <model_name> <model_file> <x> <y> <z>"
  exit 1
fi

MODEL_NAME=$1
MODEL_FILE=$2
X=$3
Y=$4
Z=$5

cd ~/MoMa-ArmLab/ros2_ws || exit 1

source /opt/ros/humble/setup.bash
source install/setup.bash

TMP_FILE="/tmp/${MODEL_NAME}.urdf"

if [[ "$MODEL_FILE" == *.xacro ]]; then
  xacro "$MODEL_FILE" > "$TMP_FILE"
else
  TMP_FILE="$MODEL_FILE"
fi

gz service -s /world/empty_world/create \
  --reqtype gz.msgs.EntityFactory \
  --reptype gz.msgs.Boolean \
  --timeout 5000 \
  --req "sdf_filename: \"$TMP_FILE\" name: \"$MODEL_NAME\" pose { position { x: $X y: $Y z: $Z } orientation { w: 1 } }"
