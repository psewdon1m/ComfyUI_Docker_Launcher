@echo oof
setlocal enabledelayedexpansion

set "PROJECT_PATH=%CD%"

echo VOLUME_OUTPUT=%PROJECT_PATH%/output > .env
echo VOLUME_MODELS=%PROJECT_PATH%/models >> .env
echo VOLUME_NODES=%PROJECT_PATH%/nodes >>> .env

echo file is success created