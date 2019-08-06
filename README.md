
# ClickTrackLogger
ClickTrackLogger is a Python based tool to record mouseclicks, scrolling and keypresses with timestamps in a log file. 
It was developed for a scientific project where user input had to recorded. It is tested to run on Windows 7 and Windows 10.
ClickTarckLogger uses a simple wxPython based GUI to start and stop logging.

Main file:
*wx_logger.py*

## Dependencies
- pynput (tested with v.1.4.2) <https://pypi.org/project/pynput/>
- wxPython (tested with v.4.0.6) <https://www.wxpython.org/>

## Building ClickTrackLogger
A one-file exe version of ClickTrackLogger can be build using pyinstaller (tested with v.3.4) <https://www.pyinstaller.org/>.
Executing the `build.bat` in the terminal should be enough to build it into a single exe file.


## References
The basic code for ClickTrackLoggers mouse and Keyboard functions is partly copied from following sources:

### Mouse Logging
<https://nitratine.net/blog/post/how-to-get-mouse-clicks-with-python/> (last accessed 06.Aug.2019)

### Keylogging
<https://nitratine.net/blog/post/python-keylogger/>  (last accessed 06.Aug.2019)

## License
The source code in this Project is completely open source and free to use, modify and redistribute for everyone. 
I do not give any warranty for this software.
