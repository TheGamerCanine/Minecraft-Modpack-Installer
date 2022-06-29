from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Progressbar
import urllib.request
import platform
import subprocess
import os
import sys
import webbrowser
import pathlib


def define_mods():
    global modpackURL
    global modpackNames
    # Official Dogpack (1.12.2)
    if modpackOption.get() == 'Official Dogpack (1.12.2)':
        modpackURL = ['https://media.forgecdn.net/files/3280/119/aether-1.12.2-v1.5.3.2.jar', 'https://media.forgecdn.net/files/3051/450/twilightforest-1.12.2-3.11.1021-universal.jar', 'https://media.forgecdn.net/files/2629/23/Thaumcraft-1.12.2-6.1.BETA26.jar', 'https://media.forgecdn.net/files/2518/667/Baubles-1.12-1.5.2.jar', 'https://media.forgecdn.net/files/3040/523/jei_1.12.2-4.16.1.301.jar', 'https://media.forgecdn.net/files/2728/585/JustEnoughResources-1.12.2-0.9.2.60.jar', 'https://media.forgecdn.net/files/3359/843/MouseTweaks-2.10.1-mc1.12.2.jar', 'https://media.forgecdn.net/files/3025/548/Controlling-3.0.10.jar', 'https://media.forgecdn.net/files/2666/198/Clumps-3.1.2.jar', 'https://media.forgecdn.net/files/2987/247/AppleSkin-mc1.12-1.0.14.jar', 'https://media.forgecdn.net/files/2898/966/EnchantmentDescriptions-1.12.2-1.1.20.jar', 'https://media.forgecdn.net/files/3778/428/Xaeros_Minimap_22.7.0_Forge_1.12.jar', 'https://media.forgecdn.net/files/3782/698/XaerosWorldMap_1.21.2_Forge_1.12.jar', 'https://media.forgecdn.net/files/2659/258/Aquaculture-1.12.2-1.6.8.jar', 'https://media.forgecdn.net/files/2483/393/BetterFps-1.4.8.jar', 'https://media.forgecdn.net/files/2595/310/Neat+1.4-17.jar', 'https://media.forgecdn.net/files/2747/935/ironchest-1.12.2-7.0.72.847.jar', 'https://media.forgecdn.net/files/2612/52/NetherPortalFix_1.12.1-5.3.17.jar', 'https://media.forgecdn.net/files/3568/240/Bountiful+Baubles-1.12.2-0.1.8.jar', 'https://media.forgecdn.net/files/2848/862/sit-1.12.2-v1.3.jar', 'https://media.forgecdn.net/files/2564/573/IronBackpacks-1.12.2-3.0.8-12.jar', 'https://media.forgecdn.net/files/2917/234/minecolonies-1.12.2-0.11.804-RELEASE-universal.jar', 'https://media.forgecdn.net/files/3760/333/additionallanterns-1.0.1-mc1.12.jar', 'https://media.forgecdn.net/files/2524/58/ChestTransporter-1.12.2-2.8.8.jar', 'https://media.forgecdn.net/files/2859/893/betternether-0.1.8.6.jar', 'https://media.forgecdn.net/files/3558/882/BiomesOPlenty-1.12.2-7.0.1.2445-universal.jar', 'https://media.forgecdn.net/files/2799/213/SereneSeasons-1.12.2-1.2.18-universal.jar', 'https://media.forgecdn.net/files/2641/661/Born+In+A+Barn+V1.8-1.12-1.1.jar', 'https://media.forgecdn.net/files/2949/667/Bountiful-2.2.2.jar', 'https://media.forgecdn.net/files/2747/710/phosphor-1.12.2-0.2.6%2Bbuild50-universal.jar', 'https://media.forgecdn.net/files/2893/527/NaturesCompass-1.12.2-1.8.5.jar', 'https://media.forgecdn.net/files/2450/734/AIImprovements-1.12-0.0.1b3.jar', 'https://media.forgecdn.net/files/3327/893/foamfix-0.10.14-1.12.2.jar', 'https://media.forgecdn.net/files/2733/525/KleeSlabs_1.12.2-5.4.12.jar', 'https://media.forgecdn.net/files/2508/268/stg-1.12.2-1.2.3.jar', 'https://media.forgecdn.net/files/2503/41/MmmMmmMmmMmm-1.12-1.14.jar', 'https://media.forgecdn.net/files/3634/12/SpartanWeaponry-1.12.2-1.4.1.jar', 'https://media.forgecdn.net/files/3567/495/SpartanShields-1.12.2-1.5.5.jar', 'https://media.forgecdn.net/files/3127/288/Artifacts-1.12.2-1.2.3.jar', 'https://media.forgecdn.net/files/2722/385/TrashSlot_1.12.2-8.4.10.jar', 'https://media.forgecdn.net/files/2727/70/Forgelin-1.8.3.jar', 'https://media.forgecdn.net/files/3773/944/supermartijn642corelib-1.0.18-forge-mc1.12.jar', 'https://media.forgecdn.net/files/2902/483/TConstruct-1.12.2-2.13.0.183.jar', 'https://media.forgecdn.net/files/2713/386/Mantle-1.12-1.3.3.55.jar', 'https://media.forgecdn.net/files/2741/812/ArtemisLib-1.12.2-v1.0.6.jar', 'https://media.forgecdn.net/files/2713/918/tropicraft-MC1.12.2-7.1.9.115.jar', 'https://media.forgecdn.net/files/2859/589/Waystones_1.12.2-4.1.0.jar', 'https://media.forgecdn.net/files/2902/920/coroutil-1.12.1-1.2.37.jar', 'https://media.forgecdn.net/files/2505/261/RealBench-1.12.2-1.3.3.jar', 'https://media.forgecdn.net/files/3041/141/spartancompat-1.2.3.jar', 'https://media.forgecdn.net/files/2762/837/SpartanWeaponryArcana-1.12.2-beta-1.0.3.jar', 'https://media.forgecdn.net/files/3507/282/spartantwilight-1.12.2-1.1.1.jar', 'https://media.forgecdn.net/files/3174/535/conarm-1.12.2-1.2.5.10.jar', 'https://media.forgecdn.net/files/2705/304/ThaumicJEI-1.12.2-1.6.0-27.jar', 'https://media.forgecdn.net/files/3330/934/Botania+r1.10-364.4.jar', 'https://media.forgecdn.net/files/3133/651/randompatches-1.12.2-1.22.1.10.jar']
        modpackNames = ['Aether-1.12.2.jar', 'Twilight-Forest-1.12.2.jar', 'Thaumcraft-1.12.2.jar', 'Baubles-1.12.2.jar', 'Just-Enough-Items-1.12.2.jar', 'Just-Enough-Resources-1.12.2.jar', 'Mouse-Tweaks-1.12.2.jar', 'Controlling-1.12.2.jar', 'Clumps-1.12.2.jar', 'AppleSkin-1.12.2.jar', 'Enchantment-Descriptions-1.12.2.jar', 'Xaeros-Minimap-1.12.2.jar', 'Xaeros-World-Map-1.12.2.jar', 'Aquaculture2-1.12.2.jar', 'BetterFPS-1.12.2.jar', 'Neat-1.12.2.jar', 'Iron-Chests-1.12.2.jar', 'Nether-Portal-Fix-1.12.2.jar', 'Bountiful-Baubles-1.12.2.jar', 'Sit-1.12.2.jar', 'Iron-Backpacks-1.12.2.jar', 'Minecolonies-1.12.2.jar', 'Additional-Lanterns-1.12.2.jar', 'Chest-Transporter-1.12.2.jar', 'Better-Nether-1.12.2.jar', 'Biomes-O-Plenty-1.12.2.jar', 'Serene-Seasons-1.12.2.jar', 'Born-in-a-Barn-1.12.2.jar', 'Bountiful-1.12.2.jar', 'Phosphor-1.12.2.jar', 'Natures-Compass-1.12.2.jar', 'AI-Improvements-1.12.2.jar', 'FoamFix-1.12.2.jar', 'KleeSlabs-1.12.2.jar', 'SwingThroughGrass-1.12.2.jar', 'MmmMmmTargetDummy-1.12.2.jar', 'SpartanWeaponry-1.12.2.jar', 'SpartanShields-1.12.2.jar', 'Artifacts-1.12.2.jar', 'TrashSlot-1.12.2.jar', 'forgelin-lib-1.12.2.jar', 'supermartijn642-corelib-1.12.2.jar', 'Tinkers-Construct-1.12.2.jar', 'mantle-1.12.2.jar', 'artemislib-1.12.2.jar', 'Tropicraft-1.12.2.jar', 'Waystones-1.12.2.jar', 'coroutil-1.12.2.jar', 'RealBench-1.12.2.jar', 'SpartanCompatibility-1.12.2.jar', 'SpartanWeaponryArcana-1.12.2.jar', 'SpartanWeaponryTwilightForest-1.12.2.jar', 'Constructs-Armory-1.12.2.jar', 'ThaumicJEI-1.12.2.jar', 'Botania-1.12.2.jar', 'RandomPatches-1.12.2.jar']
    # Official Dogpack (1.18.2)
    if modpackOption.get() == 'Official Dogpack (1.18.2)':
        modpackURL = ['https://mediafiles.forgecdn.net/files/3686/482/appleskin-forge-mc1.18-2.4.0.jar', 'https://mediafiles.forgecdn.net/files/3812/675/twilightforest-1.18.2-4.1.1052-universal.jar', 'https://mediafiles.forgecdn.net/files/3847/103/jei-1.18.2-9.7.0.209.jar', 'https://mediafiles.forgecdn.net/files/3705/938/JustEnoughResources-1.18.2-0.14.1.160.jar', 'https://mediafiles.forgecdn.net/files/3835/773/Xaeros_Minimap_22.9.3_Forge_1.18.2.jar', 'https://mediafiles.forgecdn.net/files/3835/789/XaerosWorldMap_1.23.3_Forge_1.18.2.jar', 'https://mediafiles.forgecdn.net/files/3833/879/Clumps-forge-1.18.2-8.0.0%2B10.jar', 'https://mediafiles.forgecdn.net/files/3758/406/Controlling-forge-1.18.2-9.0%2B19.jar', 'https://mediafiles.forgecdn.net/files/3798/367/BetterF3-1.2.5-Forge-1.18.2.jar', 'https://mediafiles.forgecdn.net/files/3782/776/cloth-config-6.2.62-forge.jar', 'https://mediafiles.forgecdn.net/files/3578/801/MouseTweaks-forge-mc1.18-2.21.jar', 'https://mediafiles.forgecdn.net/files/3658/64/trashslot-forge-1.18.1-11.0.2.jar', 'https://mediafiles.forgecdn.net/files/3847/503/sophisticatedbackpacks-1.18.2-3.17.9.616.jar', 'https://mediafiles.forgecdn.net/files/3830/849/waystones-forge-1.18.2-10.1.0.jar', 'https://mediafiles.forgecdn.net/files/3821/23/EnchantmentDescriptions-Forge-1.18.2-10.0.4.jar', 'https://mediafiles.forgecdn.net/files/3684/917/NaturesCompass-1.18.2-1.9.5-forge.jar', 'https://mediafiles.forgecdn.net/files/3807/626/StorageDrawers-1.18.2-10.2.1.jar', 'https://mediafiles.forgecdn.net/files/3816/497/TerraBlender-forge-1.18.2-1.1.0.102.jar', 'https://mediafiles.forgecdn.net/files/3759/236/BiomesOPlenty-1.18.2-16.0.0.109-universal.jar', 'https://mediafiles.forgecdn.net/files/3829/975/Mantle-1.18.2-1.9.27.jar', 'https://mediafiles.forgecdn.net/files/3829/979/TConstruct-1.18.2-3.5.1.31.jar', 'https://mediafiles.forgecdn.net/files/3703/960/BetterAdvancements-1.18.2-0.1.2.125.jar', 'https://mediafiles.forgecdn.net/files/3844/973/Aquaculture-1.18.2-2.3.7.jar', 'https://mediafiles.forgecdn.net/files/3682/307/comforts-forge-1.18.2-5.0.0.4.jar', 'https://mediafiles.forgecdn.net/files/3717/855/ToastControl-1.18.2-6.0.2.jar', 'https://mediafiles.forgecdn.net/files/3795/374/ironchest-1.18.2-13.1.9.jar', 'https://mediafiles.forgecdn.net/files/3717/873/FastWorkbench-1.18.2-6.0.2.jar', 'https://mediafiles.forgecdn.net/files/3732/401/Botania-1.18.2-430.jar', 'https://mediafiles.forgecdn.net/files/3801/87/AttributeFix-Forge-1.18.2-14.0.2.jar', 'https://mediafiles.forgecdn.net/files/3832/270/Bookshelf-Forge-1.18.2-13.2.21.jar', 'https://mediafiles.forgecdn.net/files/3729/975/Patchouli-1.18.2-67.jar', 'https://mediafiles.forgecdn.net/files/3845/997/Placebo-1.18.2-6.4.1.jar', 'https://mediafiles.forgecdn.net/files/3830/790/balm-3.1.0%2B0.jar', 'https://mediafiles.forgecdn.net/files/3847/441/sophisticatedcore-1.18.2-0.3.6.53.jar', 'https://mediafiles.forgecdn.net/files/3841/948/curios-forge-1.18.2-5.0.7.1.jar', 'https://mediafiles.forgecdn.net/files/3579/775/curious-armor-stands-1.18.1-4.0.0.jar', 'https://mediafiles.forgecdn.net/files/3752/209/curiouslights-forge-1.1.0%2B1.18.2.jar', 'https://mediafiles.forgecdn.net/files/3735/509/dynamiclights-1.18.6.jar', 'https://mediafiles.forgecdn.net/files/3549/513/netherportalfix-forge-1.18-9.0.0.jar', 'https://mediafiles.forgecdn.net/files/3737/418/create-mc1.18.2_v0.4.1.jar', 'https://mediafiles.forgecdn.net/files/3737/402/flywheel-forge-1.18-0.6.2.jar', 'https://mediafiles.forgecdn.net/files/3593/906/Neat+1.8-30.jar', 'https://mediafiles.forgecdn.net/files/3798/941/AI-Improvements-1.18.2-0.5.0.jar', 'https://mediafiles.forgecdn.net/files/3738/144/CosmeticArmorReworked-1.18.2-v2.jar', 'https://mediafiles.forgecdn.net/files/3830/906/craftingtweaks-forge-1.18.2-14.0.3.jar', 'https://mediafiles.forgecdn.net/files/3832/545/supplementaries-1.18.2-1.4.6.jar', 'https://mediafiles.forgecdn.net/files/3842/421/selene-1.18.2-1.17.9.jar', 'https://mediafiles.forgecdn.net/files/3767/288/ferritecore-4.2.1-forge.jar', 'https://mediafiles.forgecdn.net/files/3578/339/swingthroughgrass-1.18.1-1.8.0.jar', 'https://mediafiles.forgecdn.net/files/3666/468/clienttweaks-forge-1.18.1-7.1.0.jar', 'https://mediafiles.forgecdn.net/files/3850/527/fancymenu_forge_2.9.0_MC_1.18.2.jar', 'https://mediafiles.forgecdn.net/files/3830/896/defaultoptions-forge-1.18.2-14.1.1.jar', 'https://mediafiles.forgecdn.net/files/3804/257/SereneSeasons-1.18.2-7.0.0.15.jar' ,'https://mediafiles.forgecdn.net/files/3601/975/curiouselytra-forge-1.18.1-5.0.1.0.jar', 'https://mediafiles.forgecdn.net/files/3777/934/YungsBetterDungeons-1.18.2-Forge-2.1.0.jar', 'https://mediafiles.forgecdn.net/files/3779/88/YungsApi-1.18.2-Forge-2.0.8.jar', 'https://mediafiles.forgecdn.net/files/3778/231/YungsBetterStrongholds-1.18.2-Forge-2.1.1.jar', 'https://mediafiles.forgecdn.net/files/3777/944/YungsBridges-1.18.2-Forge-2.1.0.jar', 'https://mediafiles.forgecdn.net/files/3593/196/konkrete_forge_1.3.3_MC_1.18-1.18.1.jar', 'https://mediafiles.forgecdn.net/files/3650/485/caelus-forge-1.18.1-3.0.0.2.jar', 'https://mediafiles.forgecdn.net/files/3745/784/ToolBelt-1.18.2-1.18.8.jar', 'https://mediafiles.forgecdn.net/files/3553/486/curioofundying-forge-1.18-5.3.0.0.jar', 'https://mediafiles.forgecdn.net/files/3771/85/artifacts-1.18.2-4.1.0.jar', 'https://mediafiles.forgecdn.net/files/3785/422/simple-rpc-1.18.2-3.0.1.jar', 'https://mediafiles.forgecdn.net/files/3670/345/JustEnoughProfessions-1.18.2-1.2.2.jar', 'https://mediafiles.forgecdn.net/files/3834/420/BetterThirdPerson-Forge-1.18.2-1.8.1.jar', 'https://mediafiles.forgecdn.net/files/3678/612/expandability-6.0.0.jar', 'https://mediafiles.forgecdn.net/files/3845/190/Jade-1.18.2-forge-5.2.2.jar', 'https://mediafiles.forgecdn.net/files/3669/531/light-overlay-6.0.5-forge.jar', 'https://mediafiles.forgecdn.net/files/3808/404/3dskinlayers-forge-1.4.6-mc1.18.2.jar', 'https://mediafiles.forgecdn.net/files/3780/535/goblintraders-1.7.2-1.18.2.jar', 'https://mediafiles.forgecdn.net/files/3847/219/FallingTree-1.18.2-3.5.2.jar', 'https://mediafiles.forgecdn.net/files/3756/959/tumbleweed-1.18-0.4.12.jar', 'https://mediafiles.forgecdn.net/files/3803/98/catalogue-1.6.2-1.18.2.jar', 'https://mediafiles.forgecdn.net/files/3739/668/notenoughanimations-forge-1.6.0-mc1.18.2.jar', 'https://mediafiles.forgecdn.net/files/3775/919/soundphysics-forge-1.18.2-1.0.6.jar', 'https://mediafiles.forgecdn.net/files/3794/929/createaddition-1.18.2-20220517a.jar', 'https://mediafiles.forgecdn.net/files/3771/721/JadeAddons-1.18.2-2.0.0.jar', 'https://mediafiles.forgecdn.net/files/3843/622/architectury-4.5.75-forge.jar', 'https://mediafiles.forgecdn.net/files/3654/272/EquipmentCompare-1.18.1-1.2.12.jar', 'https://mediafiles.forgecdn.net/files/3800/622/Iceberg-1.18.2-1.0.44.jar', 'https://mediafiles.forgecdn.net/files/3751/574/logprot-1.18.2-1.6.jar', 'https://mediafiles.forgecdn.net/files/3836/415/Tips-Forge-1.18.2-5.0.3.jar']
        modpackNames = ['AppleSkin-1.18.2.jar', 'Twilight-Forest-1.18.2.jar', 'JEI-1.18.2.jar', 'JER-1.18.2.jar', 'Xaeros-Minimap-1.18.2.jar', 'Xaeros-World-Map-1.18.2.jar', 'Clumps-1.18.2.jar', 'Controlling-1.18.2.jar', 'BetterF3-1.18.2.jar', 'cloth-config-api-1.18.2.jar', 'Mouse-Tweaks-1.18.2.jar', 'Trash-Slot-1.18.2.jar', 'Sophisticated-Backpacks-1.18.2.jar', 'Waystones-1.18.2.jar', 'Enchantment-Descriptions-1.18.2.jar', 'Natures-Compass-1.18.2.jar', 'Storage-Drawers-1.18.2.jar', 'terra-blender-1.18.2.jar', 'Biomes-O-Plenty-1.18.2.jar', 'mantle-1.18.2.jar', 'Tinkers-Construct-1.18.2.jar', 'Better-Advancements-1.18.2.jar', 'Aquaculture2-1.18.2.jar', 'Comforts-1.18.2.jar', 'Toast-Control-1.18.2.jar', 'Iron-Chests-1.18.2.jar', 'Fast-Workbench-1.18.2.jar', 'Botania-1.18.2.jar', 'AttributeFix-1.18.2.jar', 'bookshelf-1.18.2.jar', 'patchouli-1.18.2.jar', 'placebo-1.18.2.jar', 'balm-1.18.2.jar', 'sophisticated-core-1.18.2.jar', 'curios-1.18.2.jar', 'Curious-Armor-Stands-1.18.2.jar', 'Curious-Lights-1.18.2.jar', 'Dynamic-Lights-1.18.2.jar', 'Nether-Portal-Fix-1.18.2.jar', 'Create-1.18.2.jar', 'flywheel-1.18.2.jar', 'Neat-1.18.2.jar', 'AI-Improvements-1.18.2.jar', 'Cosmetic-Armor-Reworked-1.18.2.jar', 'Crafting-Tweaks-1.18.2.jar', 'Supplementaries-1.18.2.jar', 'selene-1.18.2.jar', 'Ferrite-Core-1.18.2.jar', 'Swing-Through-Grass-1.18.1.jar', 'Client-Tweaks-1.18.2.jar', 'Fancy-Menu-1.18.2.jar', 'Default-Options-1.18.2.jar', 'Serene-Seasons-1.18.2.jar', 'Curious-Elytra-1.18.2.jar', 'Yungs-Better-Dungeons-1.18.2.jar', 'yungs-api-1.18.2.jar', 'Yungs-Better-Strongholds-1.18.2.jar', 'Yungs-Bridges-1.18.2.jar', 'konkrete-1.18.2.jar', 'caelus-api.1.18.2.jar', 'Tool-Belt-1.18.2.jar', 'Curio-of-Undying-1.18.2.jar', 'Artifacts-1.18.2.jar', 'Simple-Discord-RPC-1.18.2.jar', 'JEP-1.18.2.jar', 'Better-Third-Person-1.18.2.jar', 'expandability-1.18.2.jar', 'Jade-1.18.2.jar', 'Light-Overlay-1.18.2.jar', 'Skin-Layer-3D-1.18.2.jar', 'Goblin-Traders-1.18.2.jar', 'FallingTree-1.18.2.jar', 'Tumbleweed-1.18.2.jar', 'Catalogue-1.18.2.jar', 'Not-Enough-Animations-1.18.2.jar', 'Sound-Physics-Remastered-1.18.2.jar', 'Create-Additions-1.18.2.jar', 'Jade-Addons-1.18.2.jar', 'architectury-1.18.2.jar', 'Equipment-Compare-1.18.2.jar', 'iceberg-1.18.2.jar', 'Login-Protection-1.18.2.jar', 'Tips-1.18.2.jar']
    # QoL Doggo (1.19)
    if modpackOption.get() == 'QoL Doggo (1.19)':
        modpackURL = ['https://mediafiles.forgecdn.net/files/3845/981/fabric-api-0.56.3%2B1.19.jar', 'https://mediafiles.forgecdn.net/files/3821/727/appleskin-fabric-mc1.19-2.4.0.jar', 'https://mediafiles.forgecdn.net/files/3846/514/RoughlyEnoughItems-9.0.493.jar', 'https://mediafiles.forgecdn.net/files/3821/162/modmenu-4.0.0.jar', 'https://mediafiles.forgecdn.net/files/3835/774/Xaeros_Minimap_22.9.3_Fabric_1.19.jar', 'https://mediafiles.forgecdn.net/files/3835/790/XaerosWorldMap_1.23.3_Fabric_1.19.jar', 'https://mediafiles.forgecdn.net/files/3822/621/Controlling-fabric-1.19-10.0%2B1.jar', 'https://mediafiles.forgecdn.net/files/3824/125/InventoryHUD-fabric-%5b1.19%5d+-3.4.2.jar']
        modpackNames = ['fabric-api-1.19.jar','AppleSkin-1.19.jar', 'REI-1.19.jar', 'Mod-Menu-1.19.jar', 'Xaeros-Minimap-1.19.jar', 'Xaeros-World-Map-1.19.jar', 'Controlling-1.19.jar', 'Inventory-HUDplus-1.19.jar']

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
            progress_step = float(100/len(modsToInstall))
            for x in range(len(modsToInstall)):
                mod = modsToInstall[x]
                urllib.request.urlretrieve(modpackURL[mod], (modDirectory+modpackNames[mod]))
                installModProgress['value'] += progress_step
                print('Downloaded '+modpackNames[mod])
                progWindow.update()
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
root = Tk()
root.geometry('480x280')
root.title('GamerDog Modpack')
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
Label(root, text='GamerDog Modpack', font=('Arial', 30, 'bold')).pack(pady=5)
Label(root, text='Modpack to Install', font=('Arial', 12)).pack(pady=2)
modpackOption = StringVar()
modpackOption.set('Official Dogpack (1.18.2)')
modpackSelector = OptionMenu(root, modpackOption, 'Official Dogpack (1.12.2)', 'Official Dogpack (1.18.2)', 'QoL Doggo (1.19)')
modpackSelector.pack(pady=2)
Label(root, text='Installation Options', font=('Arial', 12)).pack(pady=3)
Button(root, text='Install Modloader (Forge/Fabric)', command=install_modloader).pack(pady=3)
Button(root, text='Install Mods', command=install_mods).pack(pady=3)
clearModsFirst = IntVar(value=1)
Checkbutton(root, text='Clear mods folder before install.', variable=clearModsFirst, onvalue=1, offvalue=0).pack()

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