import wx
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyListener
import logging

logging.basicConfig(filename=("logger.txt"), level=logging.DEBUG, format='%(asctime)s:%(message)s')


class WxExportFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="ClickTrackLogger")
        self.panel = WxExportPanel(self)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Show()

    def Info(self, parent, message, caption='ClickTrackLogger'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def OnClose(self, event):
        print('OnClose')
        if event.CanVeto() and (self.panel.keylogger.running or self.panel.mouselogger.running):
            print('Will not close - Logger still running')
            self.Info(self, 'Logger still running')
            event.Veto()
        else:
            self.Destroy()  # you may also do:  event.Skip() since the default event handler does call Destroy(), too
            print('Will close window')

class WxExportPanel(wx.Panel):

    mouselogger: MouseListener = None
    keylogger: KeyListener = None


    def __init__(self, parent):
        super().__init__(parent)
        self.mouselogger = MouseListener(on_click=self.on_click, on_scroll=self.on_scroll)
        self.keylogger = KeyListener(on_press=self.on_press, on_release=self.on_release)

        main_sizer_vert = wx.BoxSizer(wx.VERTICAL)
        main_sizer_vert.AddStretchSpacer()

        # Create the "Start (to Tray)"-Button
        self.wx_button_export = wx.Button(self, label="Start")
        self.wx_button_export.Bind(wx.EVT_BUTTON, self.toggle_logging)
        main_sizer_vert.Add(self.wx_button_export, 0, wx.TOP | wx.CENTER, 20)

        #set the sizer of the panel
        main_sizer_vert.AddStretchSpacer()
        self.SetSizer(main_sizer_vert)

    def on_log_path_set(self, event):
        print('[ClickTrackLogger] on_log_path_set')
        # Get the source path
        self.log_path = self.wx_file_picker_log.GetPath()

    def toggle_logging(self, event):
        if not self.mouselogger.running or not self.keylogger.running:
            self.mouselogger.start()
            print('mouselogger started')
            self.keylogger.start()
            print('keylogger started')
            self.wx_button_export.SetLabel('Stop')
        else:
            if self.mouselogger.running:
                self.mouselogger.stop()
                print('Mouselogger stoped')
            if self.keylogger.running:
                self.keylogger.stop()
                print('Keylogger stoped')
            self.wx_button_export.SetLabel('Start')

    def on_click(self, x, y, button, pressed):
        if pressed:
            logging.info(f'mouse_click,{button},pos_x{x}_y{y}')

    def on_scroll(self, x, y, dx, dy):
        name = 'mouse_scroll'
        if dy <= -1:
            name += '_down'
        if dy >= 1:
            name += '_up'
        if dx <= -1:
            name += '_left'
        if dx >= 1:
            name += '_right'
        logging.info(f'{name},MouseScroll,pos_x{x}_y{y}')

    def on_press(self, key):
        logging.info(f'keyboard_press,{str(key)},no_pos')

    def on_release(self, key):
        logging.info(f'keyboard_release,{str(key)},no_pos')


if __name__ == "__main__":
    app = wx.App(False)
    frame = WxExportFrame()
    app.MainLoop()
