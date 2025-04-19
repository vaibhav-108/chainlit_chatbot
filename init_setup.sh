echo [$(date)] : "START"
echo [$(date)] : "Creating env with python 3.12.0"
conda create --prefix ./env python=3.12.0 -y
echo [$(date)] : "creating env"
source  activate ./env
echo [$(date)] : "activated conda env"
echo [$(date)] : "installing requirements"
pip install -r requirements.txt
echo [$(date)] : "installed requirements"
echo [$(date)] : "END"