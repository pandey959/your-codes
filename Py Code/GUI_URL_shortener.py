from tkinter import *
from tkinter import ttk
import pyshorteners
import webbrowser

root=Tk()
root.title("Url Shortner")
root.geometry("450x250")

# label
label=ttk.Label(root, text="URL Shortner", font=('Poppins', 20))
label.grid(row=0, column=1)

entry_label=ttk.Label(root, text="Enter Url: ")
entry_label.grid(row=1, column=0, pady=10, padx=(20, 0))
# input field for URL
url = StringVar()
url_entry=ttk.Entry(root, textvariable=url, width=50)
url_entry.grid(row=1, column=1, pady=10)
# button to short URL
shorten_button=ttk.Button(root, text="Shorten", command=lambda: shorten_url(url.get()))
shorten_button.grid(row=2, column=0, pady=10, padx=(20, 0))
# label for output
output_label=ttk.Label(root, text="Shorted Url: ")
output_label.grid(row=3, column=0, pady=10, padx=(20, 0))
# output field for shorted URL
shortened_url=StringVar()
shortened_url_entry=ttk.Entry(root, textvariable=shortened_url, width=50)
shortened_url_entry.grid(row=3, column=1, pady=10)

# button For copy URL
copy_button=ttk.Button(root, text="Copy", command=lambda:copy_url(shortened_url.get()))
copy_button.grid(row=4, column=0, pady=10, padx=(20, 0))
# open button
open_button=ttk.Button(root, text="Open", command = lambda: open_url(url.get()))
open_button.grid(row=4, column=1, pady=10, padx=(20, 0))

# function to short URL:
def shorten_url(url):
    try:
        short_url=pyshorteners.Shortener().tinyurl.short(url)
        shortened_url.set(short_url)
    except:
        print("invalid URL")

# function to copy
def copy_url(url):
    try:
        url_entry.clipboard_clear()
        url_entry.clipboard_append(url)
    except:
        print("invalid URL")

# open url
def open_url(url):
    try:
        webbrowser.open(url)
    except:
        print("invalid URL")
root.mainloop()
