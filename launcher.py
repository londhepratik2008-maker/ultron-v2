import os
import sys
import threading
import webview

def get_html_path():
    if getattr(sys, 'frozen', False):
        base = os.path.dirname(sys.executable)
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, 'index.html')

class UltronAPI:
    def __init__(self, window):
        self._window = window

    def minimize(self):
        self._window.minimize()

    def toggle_maximize(self):
        if self._window.maximized:
            self._window.restore()
        else:
            self._window.maximize()

    def close(self):
        self._window.destroy()

    def get_title(self):
        return "Ultron A.I. v2"

def main():
    html_path = get_html_path()

    if not os.path.exists(html_path):
        print(f"ERROR: index.html not found at {html_path}")
        input("Press Enter to exit...")
        sys.exit(1)

    url = 'file:///' + html_path.replace('\\', '/')

    window = webview.create_window(
        title='Ultron A.I. v2',
        url=url,
        width=1400,
        height=900,
        min_size=(1000, 700),
        resizable=True,
        frameless=False,
        easy_drag=False,
        background_color='#1B0303',
        text_select=True,
    )

    api = UltronAPI(window)
    window.expose(api.minimize, api.toggle_maximize, api.close, api.get_title)

    webview.start(debug=False)

if __name__ == '__main__':
    main()
