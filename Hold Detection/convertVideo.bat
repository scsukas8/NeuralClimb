@ECHO off
ECHO Converting %~n1%~x1...
ffmpeg -i %~n1%~x1 -c:v rawvideo -pix_fmt yuv420p %~n1-converted.avi
ECHO Done!
pause