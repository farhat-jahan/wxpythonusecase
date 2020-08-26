import wx
from backend.conversions import *

def get_result(event):
    meter = float(input_box.GetValue())
    try:
        result_box.SetLabel(str(meter_feet(meter) ))
    except Exception as e:
        input_box.SetLabel("Enter correct Value")


app =wx.App()
frame = wx.Frame(parent= None, title ="Meter to feet")
panel = wx.Panel(frame)
define_size = wx.GridBagSizer()

input_lable = wx.StaticText(panel, label = "Meter")
input_box = wx.TextCtrl(panel)
result_lable = wx.StaticText(panel, label = "Feet")
result_box = wx.TextCtrl(panel)
submit_button = wx.Button(panel, label = "Convert")
submit_button.Bind(wx.EVT_BUTTON, get_result)

define_size.Add(input_lable, (0, 0))
define_size.Add(input_box,(0, 2))
define_size.Add(result_lable,(1, 0))
define_size.Add(result_box, (1, 2))
define_size.Add(submit_button, (2, 2))

panel.SetSizerAndFit(define_size)
frame.SetSizerAndFit(define_size)
frame.Show()

app.MainLoop()




