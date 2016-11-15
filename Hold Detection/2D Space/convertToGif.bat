@ECHO off
set /p length= "Enter Length: "
set /p fps= "Enter FPS: "
ECHO Converting %~n1%~x1...
ffmpeg -i %~n1%~x1 -vf scale=500:-1 -t %length% -r %fps% %~n1%.gif
ECHO Done!
pause