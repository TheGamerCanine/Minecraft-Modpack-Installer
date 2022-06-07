from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import urllib.request
import platform
import subprocess
import os
import sys
import webbrowser
import pathlib
try:    
    from alive_progress import alive_bar
    import requests
except ModuleNotFoundError:
    os.system('pip3 install -r requirements.txt')
    from alive_progress import alive_bar
    import requests


def install_forge():
    if os.path.exists(versiondirectory + '1.12.2-forge-14.23.5.2859') == True:
        forgeinstalleddia = messagebox.askyesno(title='Forge already installed.', message='Forge appears to already be installed. Continue anyways?')
        if forgeinstalleddia == False:
            return
    urllib.request.urlretrieve('https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2859/forge-1.12.2-14.23.5.2859-installer.jar', 'forge-1.12.2.jar')
    subprocess.call(['java', '-jar', 'forge-1.12.2.jar'])
    os.remove('forge-1.12.2.jar')
    print('Forge 1.12.2 installed.')

def install_mods():
    # Determine what needs to be installed
    modstoinstall=[]
    for x in range(0,len(modpacknames)):
        if os.path.exists(moddirectory+modpacknames[x]) == False:
            modstoinstall.append(x)
    # Throw error if all mods satisfied
    if modstoinstall == []:
        messagebox.showerror(title='Mods already installed', message=f'Mods already installed at {moddirectory}')
        return
    else:
        installmodsokay = messagebox.askyesno(title='Mods directory okay?', message=f'Installing mods at {moddirectory}\n Is this okay?')
        if installmodsokay == True:
            # Create new window to contain progress bar for install 
            progwindow = Toplevel(root)
            Label(progwindow, text=f'Installing {len(modstoinstall)} mods.').pack()
            installmodprogress = Progressbar(progwindow, orient=HORIZONTAL, length=100, mode='determinate')
            installmodprogress.pack()
            progress_step = float(100/len(modstoinstall))
            for x in range(len(modstoinstall)):
                mod = modstoinstall[x]
                urllib.request.urlretrieve(modpackurl[mod], (moddirectory+modpacknames[mod]))
                installmodprogress['value'] += progress_step
                progwindow.update()
            messagebox.showinfo(title='Finished.', message='All mods installed successfully.')
            # Kill progress bar window
            progwindow.destroy()
        else:
            return

def clear_mods():
    existmodsfolder = os.listdir(moddirectory)
    for x in range(0, len(existmodsfolder)):
            if pathlib.Path(existmodsfolder[x]).suffix == '.jar':
                os.remove(moddirectory + existmodsfolder[x])
    messagebox.showinfo(title='Finished.', message='Cleared all preexisting mods from mods folder successfully.')

def creditstxt():
    #credwindow = Toplevel(root)
    credread = open('credit.txt', 'r')
    print(credread.read())
    credread.close()

def dogsite():
    webbrowser.open('toucam.live')


# Set tkinter and window properties
root = Tk()
root.geometry('640x240')
root.title('GamerDog Modpack')
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='dogpack.png'))

# Set title and buttons for window
Label(text='GamerDog Modpack', font=('System', 30, 'bold')).pack()
Button(text='Install Forge 1.12.2', command=install_forge).pack()
Button(text='Install Mods', command=install_mods).pack()
clearmodsb = Button(text="Clear Mods Folder", command=clear_mods)
clearmodsb.pack()
Button(text='View credits.txt', command=creditstxt).pack()
Button(text='Visit Website', command=dogsite).pack()


# Identify Operating System
if platform.system() == 'Windows':
    minecraftdirectory = os.path.expanduser('~')+'\\AppData\\Roaming\\.minecraft\\'
    moddirectory = minecraftdirectory + 'mods\\'
    versiondirectory = minecraftdirectory + 'versions\\'
    print(f'Installing for {platform.system()}')
elif platform.system() == 'Linux':
    minecraftdirectory = os.path.expanduser('~')+'/.minecraft/'
    moddirectory = minecraftdirectory + 'mods/'
    versiondirectory = minecraftdirectory + 'versions/'
    print(f'Installing for {platform.system()}')
elif platform.system() == 'Darwin':
    minecraftdirectory = os.path.expanduser('~')+'/Library/Application Support/minecraft/'
    moddirectory = minecraftdirectory + 'mods/'
    versiondirectory = minecraftdirectory + 'versions/'
    print('Installing for MacOS')

# Check for Java
try:
    subprocess.call(['java', '-version'])
except FileNotFoundError:
    messagebox.showwarning(title='Java not found.', message='Java 8+ must be installed before continuing!')
    webbrowser.open('https://www.java.com/download/ie_manual.jsp')
    sys.exit('Cannot install, quitting install.')

# Define mods to install
modpackurl = ['https://media.forgecdn.net/files/3280/119/aether-1.12.2-v1.5.3.2.jar', 'https://media.forgecdn.net/files/3051/450/twilightforest-1.12.2-3.11.1021-universal.jar', 'https://media.forgecdn.net/files/2629/23/Thaumcraft-1.12.2-6.1.BETA26.jar', 'https://media.forgecdn.net/files/2518/667/Baubles-1.12-1.5.2.jar', 'https://media.forgecdn.net/files/3040/523/jei_1.12.2-4.16.1.301.jar', 'https://media.forgecdn.net/files/2728/585/JustEnoughResources-1.12.2-0.9.2.60.jar', 'https://media.forgecdn.net/files/3359/843/MouseTweaks-2.10.1-mc1.12.2.jar', 'https://media.forgecdn.net/files/3025/548/Controlling-3.0.10.jar', 'https://media.forgecdn.net/files/2666/198/Clumps-3.1.2.jar', 'https://media.forgecdn.net/files/2987/247/AppleSkin-mc1.12-1.0.14.jar', 'https://media.forgecdn.net/files/2898/966/EnchantmentDescriptions-1.12.2-1.1.20.jar', 'https://media.forgecdn.net/files/3778/428/Xaeros_Minimap_22.7.0_Forge_1.12.jar', 'https://media.forgecdn.net/files/3782/698/XaerosWorldMap_1.21.2_Forge_1.12.jar', 'https://media.forgecdn.net/files/2659/258/Aquaculture-1.12.2-1.6.8.jar', 'https://media.forgecdn.net/files/2483/393/BetterFps-1.4.8.jar', 'https://media.forgecdn.net/files/2595/310/Neat+1.4-17.jar', 'https://media.forgecdn.net/files/2747/935/ironchest-1.12.2-7.0.72.847.jar', 'https://media.forgecdn.net/files/2612/52/NetherPortalFix_1.12.1-5.3.17.jar', 'https://media.forgecdn.net/files/3568/240/Bountiful+Baubles-1.12.2-0.1.8.jar', 'https://media.forgecdn.net/files/2848/862/sit-1.12.2-v1.3.jar', 'https://media.forgecdn.net/files/2564/573/IronBackpacks-1.12.2-3.0.8-12.jar', 'https://media.forgecdn.net/files/2917/234/minecolonies-1.12.2-0.11.804-RELEASE-universal.jar', 'https://media.forgecdn.net/files/3760/333/additionallanterns-1.0.1-mc1.12.jar', 'https://media.forgecdn.net/files/2524/58/ChestTransporter-1.12.2-2.8.8.jar', 'https://media.forgecdn.net/files/2859/893/betternether-0.1.8.6.jar', 'https://media.forgecdn.net/files/3558/882/BiomesOPlenty-1.12.2-7.0.1.2445-universal.jar', 'https://media.forgecdn.net/files/2799/213/SereneSeasons-1.12.2-1.2.18-universal.jar', 'https://media.forgecdn.net/files/2641/661/Born+In+A+Barn+V1.8-1.12-1.1.jar', 'https://media.forgecdn.net/files/2949/667/Bountiful-2.2.2.jar', 'https://media.forgecdn.net/files/2747/710/phosphor-1.12.2-0.2.6%2Bbuild50-universal.jar', 'https://media.forgecdn.net/files/2893/527/NaturesCompass-1.12.2-1.8.5.jar', 'https://media.forgecdn.net/files/2450/734/AIImprovements-1.12-0.0.1b3.jar', 'https://media.forgecdn.net/files/3327/893/foamfix-0.10.14-1.12.2.jar', 'https://media.forgecdn.net/files/2733/525/KleeSlabs_1.12.2-5.4.12.jar', 'https://media.forgecdn.net/files/2508/268/stg-1.12.2-1.2.3.jar', 'https://media.forgecdn.net/files/2503/41/MmmMmmMmmMmm-1.12-1.14.jar', 'https://media.forgecdn.net/files/3634/12/SpartanWeaponry-1.12.2-1.4.1.jar', 'https://media.forgecdn.net/files/3567/495/SpartanShields-1.12.2-1.5.5.jar', 'https://media.forgecdn.net/files/3127/288/Artifacts-1.12.2-1.2.3.jar', 'https://media.forgecdn.net/files/2722/385/TrashSlot_1.12.2-8.4.10.jar', 'https://media.forgecdn.net/files/2727/70/Forgelin-1.8.3.jar', 'https://media.forgecdn.net/files/3773/944/supermartijn642corelib-1.0.18-forge-mc1.12.jar', 'https://media.forgecdn.net/files/2902/483/TConstruct-1.12.2-2.13.0.183.jar', 'https://media.forgecdn.net/files/2713/386/Mantle-1.12-1.3.3.55.jar', 'https://media.forgecdn.net/files/2741/812/ArtemisLib-1.12.2-v1.0.6.jar', 'https://media.forgecdn.net/files/2713/918/tropicraft-MC1.12.2-7.1.9.115.jar', 'https://media.forgecdn.net/files/2859/589/Waystones_1.12.2-4.1.0.jar', 'https://media.forgecdn.net/files/2902/920/coroutil-1.12.1-1.2.37.jar', 'https://media.forgecdn.net/files/2505/261/RealBench-1.12.2-1.3.3.jar', 'https://media.forgecdn.net/files/3041/141/spartancompat-1.2.3.jar', 'https://media.forgecdn.net/files/2762/837/SpartanWeaponryArcana-1.12.2-beta-1.0.3.jar', 'https://media.forgecdn.net/files/3507/282/spartantwilight-1.12.2-1.1.1.jar', 'https://media.forgecdn.net/files/3174/535/conarm-1.12.2-1.2.5.10.jar', 'https://media.forgecdn.net/files/2705/304/ThaumicJEI-1.12.2-1.6.0-27.jar', 'https://media.forgecdn.net/files/3330/934/Botania+r1.10-364.4.jar', 'https://media.forgecdn.net/files/3133/651/randompatches-1.12.2-1.22.1.10.jar']
modpacknames = ['Aether-1.12.2.jar', 'Twilight-Forest-1.12.2.jar', 'Thaumcraft-1.12.2.jar', 'Baubles-1.12.2.jar', 'Just-Enough-Items-1.12.2.jar', 'Just-Enough-Resources-1.12.2.jar', 'Mouse-Tweaks-1.12.2.jar', 'Controlling-1.12.2.jar', 'Clumps-1.12.2.jar', 'AppleSkin-1.12.2.jar', 'Enchantment-Descriptions-1.12.2.jar', 'Xaeros-Minimap-1.12.2.jar', 'Xaeros-World-Map-1.12.2.jar', 'Aquaculture2-1.12.2.jar', 'BetterFPS-1.12.2.jar', 'Neat-1.12.2.jar', 'Iron-Chests-1.12.2.jar', 'Nether-Portal-Fix-1.12.2.jar', 'Bountiful-Baubles-1.12.2.jar', 'Sit-1.12.2.jar', 'Iron-Backpacks-1.12.2.jar', 'Minecolonies-1.12.2.jar', 'Additional-Lanterns-1.12.2.jar', 'Chest-Transporter-1.12.2.jar', 'Better-Nether-1.12.2.jar', 'Biomes-O-Plenty-1.12.2.jar', 'Serene-Seasons-1.12.2.jar', 'Born-in-a-Barn-1.12.2.jar', 'Bountiful-1.12.2.jar', 'Phosphor-1.12.2.jar', 'Natures-Compass-1.12.2.jar', 'AI-Improvements-1.12.2.jar', 'FoamFix-1.12.2.jar', 'KleeSlabs-1.12.2.jar', 'SwingThroughGrass-1.12.2.jar', 'MmmMmmTargetDummy-1.12.2.jar', 'SpartanWeaponry-1.12.2.jar', 'SpartanShields-1.12.2.jar', 'Artifacts-1.12.2.jar', 'TrashSlot-1.12.2.jar', 'forgelin-lib-1.12.2.jar', 'supermartijn642-corelib-1.12.2.jar', 'Tinkers-Construct-1.12.2.jar', 'mantle-1.12.2.jar', 'artemislib-1.12.2.jar', 'Tropicraft-1.12.2.jar', 'Waystones-1.12.2.jar', 'coroutil-1.12.2.jar', 'RealBench-1.12.2.jar', 'SpartanCompatibility-1.12.2.jar', 'SpartanWeaponryArcana-1.12.2.jar', 'SpartanWeaponryTwilightForest-1.12.2.jar', 'Constructs-Armory-1.12.2.jar', 'ThaumicJEI-1.12.2.jar', 'Botania-1.12.2.jar', 'RandomPatches-1.12.2.jar']

# Check for mods directory and find what's installed
if os.path.exists(moddirectory) == False:
    os.mkdir(moddirectory)
    messagebox.showinfo(title='', message=f'Mod folder created at {moddirectory}')
    clearmodsb['state'] = 'disabled'
else:
    clearmodsb['state'] = 'normal'

# Start tkinter
root.mainloop()