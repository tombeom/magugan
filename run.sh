cd magugan
lxterminal --title="Camera Server" --command sh "mjpg.sh" --working-directory "/home/magugan/"
lxterminal --title="Flask Server" --command sh "serverOpen.sh" --working-directory "/home/magugan/"
python3 /home/magu/magugan/magu.py


