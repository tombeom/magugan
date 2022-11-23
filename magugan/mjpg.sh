export STREAMER_PATH=$HOME/magugan/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=$STREAMER_PATH
$STREAMER_PATH/mjpg_streamer -i "input_uvc.so" -o "output_http.so -w $STREAMER_PATH/www"
