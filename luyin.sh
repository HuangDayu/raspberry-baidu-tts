#!/bin/bash
sudo arecord -Dhw:1,0 -c 2 -r 16000 -f S16_LE shibie.wav