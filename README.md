# rest_api
install following packages before runnig server.

fastai==1.0.61
opencv-python
torch==1.9.1
torchvision==0.10.1
pil
numpy
Flask

Once done user the following command to run server.

python3 run_dl_server.py

After running the server run the following command in new terminal tab to test server.

curl -X POST -F image=@normal.jpg 'http://localhost:5000/predict' 