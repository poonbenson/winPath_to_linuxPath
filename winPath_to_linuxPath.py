#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bensonpoon
#
# Created:     10/10/2019
# Copyright:   (c) bensonpoon 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import pyperclip
    clipboardTXT = pyperclip.paste() + "clipped"
    pyperclip.copy(clipboardTXT)

if __name__ == '__main__':
    main()
