from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import Progressbar
import urllib.request
import platform
import subprocess
import os
import sys
import webbrowser
import pathlib
import time
try:
    from ttkthemes import ThemedTk
except ModuleNotFoundError:
    os.system('pip3 install -r requirements.txt')
    from ttkthemes import ThemedTk


def define_mods():
    global modpackURL
    global modpackNames
    modpackFileDir = f'modpackfiles/{modpackOption.get()}'
    with open(f'{modpackFileDir}/modpackURL', 'r') as f:
        modpackURL = [line.strip() for line in f]
    with open(f'{modpackFileDir}/modpackNames', 'r') as f:
        modpackNames = [line.strip() for line in f]

def install_modloader():
    # Define a folder the modloader should be installed to, set a download URL and determine whether there are logs that need to be deleted or not.
    if modpackOption.get() == 'Official Dogpack (1.12.2)':
        modloaderFolder = '1.12.2-forge-14.23.5.2859'
        modloaderURL = 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2859/forge-1.12.2-14.23.5.2859-installer.jar'
        delLog = 1
    elif modpackOption.get() == 'Official Dogpack (1.18.2)':
        modloaderFolder = '1.18.2-forge-40.1.52'
        modloaderURL = 'https://maven.minecraftforge.net/net/minecraftforge/forge/1.18.2-40.1.52/forge-1.18.2-40.1.52-installer.jar'
        delLog = 1
    elif modpackOption.get() == 'QoL Doggo (1.19)':
        modloaderFolder = 'fabric-loader-0.14.8-1.19'
        modloaderURL = 'https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.0/fabric-installer-0.11.0.jar'
        delLog = 0
    # Install necessary modloader
    if os.path.exists(versionDirectory + modloaderFolder) == True:
        modloaderInstalledDia = messagebox.askyesno(title='Modloader already installed.', message='Necessary modloader appears to already be installed. Continue anyways?')
        if modloaderInstalledDia == False:
            return
    urllib.request.urlretrieve(modloaderURL, 'modloader.jar')
    subprocess.call(['java', '-jar', 'modloader.jar'])
    os.remove('modloader.jar')
    if delLog == 1:
        os.remove('installer.log')
    print('Done.')

def install_mods():
    # Find what modpack is being used
    define_mods()
    # Check if clear mods checked off
    if clearModsFirst.get() == 1:
        clear_mods()
    # Determine what needs to be installed
    modsToInstall=[]
    for x in range(0,len(modpackNames)):
        if os.path.exists(modDirectory+modpackNames[x]) == False:
            modsToInstall.append(x)
    # Throw error if all mods satisfied
    if modsToInstall == []:
        messagebox.showerror(title='Mods already installed', message=f'Mods already installed at {modDirectory}')
        return
    else:
        installModsOkay = messagebox.askyesno(title='Mods directory okay?', message=f'Installing mods at {modDirectory}\n Is this okay?')
        if installModsOkay == True:
            # Create new window to contain progress bar for install 
            progWindow = Toplevel(root)
            Label(progWindow, text=f'Installing {len(modsToInstall)} mods.').pack()
            installModProgress = Progressbar(progWindow, orient=HORIZONTAL, length=100, mode='determinate')
            installModProgress.pack()
            Button(progWindow, text='Cancel', command=progWindow.destroy).pack()
            startInstallTime = time.time()
            progress_step = float(100/len(modsToInstall))
            for x in range(len(modsToInstall)):
                mod = modsToInstall[x]
                urllib.request.urlretrieve(modpackURL[mod], (modDirectory+modpackNames[mod]))
                installModProgress['value'] += progress_step
                print('Downloaded '+modpackNames[mod])
                progWindow.update()
            endInstallTime = time.time()
            print('Finished in ' + str(round(endInstallTime-startInstallTime, 2)) + 's')
            messagebox.showinfo(title='Finished.', message='All mods installed successfully.')
            print('Done.')
            # Kill progress bar window
            progWindow.destroy()
        else:
            return

def clear_mods():
    existModsFolder = os.listdir(modDirectory)
    for x in range(0, len(existModsFolder)):
            if pathlib.Path(existModsFolder[x]).suffix == '.jar':
                os.remove(modDirectory + existModsFolder[x])
    messagebox.showinfo(title='Finished.', message='Cleared all preexisting mods from mods folder successfully.')

def browse_button():
    global extract_dir
    extract_dir = filedialog.askdirectory()
    extWindow.update()
    print(extract_dir)

def extract_to_dir():
    # Find what modpack is being used
    define_mods()
    # Extract mods to desired folder
    Label(extWindow, text='Extracting...').grid(row=4, column=0)
    extractModProgress = Progressbar(extWindow, orient=HORIZONTAL, length=100, mode='determinate')
    extractModProgress.grid(row=5, column=0)
    progress_step = float(100/len(modpackNames))
    for x in range(len(modpackNames)):
        urllib.request.urlretrieve(modpackURL[x], (extract_dir+'/'+modpackNames[x]))
        extractModProgress['value'] += progress_step
        extWindow.update()
    messagebox.showinfo(title='Finished.', message='Finished extracting mods to the desired folder.')
    extWindow.destroy()

def extract_mods():
    global extWindow
    extWindow = Toplevel(root)
    extWindow.transient(root)
    extract_dir = StringVar()
    Label(extWindow, text=f'Extracting {modpackOption.get()}', font=('Arial', 12, 'bold')).grid(row=0, column=0)
    Label(extWindow, text='Choose folder to extract to.').grid(row=1, column=0)
    Entry(extWindow, textvariable=extract_dir, state='disabled', width=30).grid(row=2, column=0)
    Button(extWindow, text="...", command=browse_button).grid(row=2, column=3)
    Button(extWindow, text='Extract', command=extract_to_dir).grid(row=3, column=0, pady=2)

def credits_txt():
    webbrowser.open('credit.txt')

def dogsite():
    webbrowser.open('https://toucam.live')

def wiki_view():
    webbrowser.open('https://github.com/TheGamerCanine/GamerDog-Modpack/wiki')


# Set tkinter and window properties
root = ThemedTk(theme='yaru')
root.geometry('480x280')
root.title('Dogcraft')
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='dogpack.png'))

# Set menu functions
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Clear Mods Folder', command=clear_mods)
filemenu.add_command(label='Extract Mods', command=extract_mods)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='View Wiki', command=wiki_view)
helpmenu.add_command(label='View Credits', command=credits_txt)
helpmenu.add_command(label='View Website', command=dogsite)
menubar.add_cascade(label='Help', menu=helpmenu)

root.config(menu=menubar)
# Set title and buttons for window
Label(root, text='Dogcraft Installer', font=('Arial', 30, 'bold')).pack(pady=5)
Label(root, text='Modpack to Install', font=('Arial', 12)).pack(pady=2)
modpackAvailable = os.listdir('modpackfiles')
modpackOption = StringVar()
modpackOption.set('Official Dogpack (1.18.2)')
modpackSelector = OptionMenu(root, modpackOption, *modpackAvailable)
modpackSelector.pack(pady=2)
Label(root, text='Installation Options', font=('Arial', 12)).pack(pady=3)
Button(root, text='Install Modloader (Forge/Fabric)', command=install_modloader).pack(pady=3)
Button(root, text='Install Mods', command=install_mods).pack(pady=3)
clearModsFirst = IntVar(value=1)
ttk.Checkbutton(root, text='Clear mods folder before install.', variable=clearModsFirst, onvalue=1, offvalue=0).pack()

# Identify Operating System
if platform.system() == 'Windows':
    minecraftDirectory = os.path.expanduser('~')+'\\AppData\\Roaming\\.minecraft\\'
    modDirectory = minecraftDirectory + 'mods\\'
    versionDirectory = minecraftDirectory + 'versions\\'
    print(f'Installing for {platform.system()}')
elif platform.system() == 'Linux':
    minecraftDirectory = os.path.expanduser('~')+'/.minecraft/'
    modDirectory = minecraftDirectory + 'mods/'
    versionDirectory = minecraftDirectory + 'versions/'
    print(f'Installing for {platform.system()}')
elif platform.system() == 'Darwin':
    minecraftDirectory = os.path.expanduser('~')+'/Library/Application Support/minecraft/'
    modDirectory = minecraftDirectory + 'mods/'
    versionDirectory = minecraftDirectory + 'versions/'
    print('Installing for MacOS')

# Check for Java
try:
    subprocess.call(['java', '-version'])
except FileNotFoundError:
    messagebox.showwarning(title='Java not found.', message='Java 8+ must be installed before continuing!')
    webbrowser.open('https://www.java.com/download/ie_manual.jsp')
    sys.exit('Cannot install, quitting install.')

# Check for mods directory and find what's installed
if os.path.exists(modDirectory) == False:
    os.mkdir(modDirectory)
    messagebox.showinfo(title='', message=f'Mod folder created at {modDirectory}')

# Start tkinter
root.mainloop()
