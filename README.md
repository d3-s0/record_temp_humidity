## How to set up
1. Connect arduino to power source (e.g.laptop)
2. Connect sensor to arduino as shown below:
<img src="sensor.jpeg" alt="drawing" width="200"/>
3. Open arduino IDE app
4. Connect to correct board name and port number. Run ls /dev/cu.* command on terminal to find out all ports available
5. Open arduino_code.ino file in arduino IDE and upload the code to the arduino
6. Close arduino IDE app
7. Run the read data python script
8. Look at results in temp_himid_data.csv!
9. I wanted the script to run 24/7, so I moved python script to my raspberry pi and connected the arduinto the pi.
10. Use tmux to run in the background (sudo apt-get install tmux then tmux new -s sensor_log)
11. Run the script in the session and detach from tmux
12. Check the csv has updated