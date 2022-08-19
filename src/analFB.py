from frontend import Main
import sys
import os


if __name__ == '__main__':
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    resource_path("analFB logo.png")
    main = Main()
    main.run()
