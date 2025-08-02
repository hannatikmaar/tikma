import base64
from seleniumbase import SB

# Ask the user for base64 input
a_input = 'aHR0cHM6Ly9raWNrLmNvbS9icnV0YWxsZXM='
tiki = base64.b64decode(a_input)
mtiki = tiki.decode('utf-8')
with SB(uc=True, test=True) as tikma:
    url = mtiki
    tikma.uc_open_with_reconnect(url, 5)
    tikma.uc_gui_click_captcha()
    tikma.sleep(2)
    tikma.uc_gui_handle_captcha()
    while(tikma.is_element_present('video#video-player')):
        tikma.sleep(10)
    
