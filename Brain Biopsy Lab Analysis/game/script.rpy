define s = Character(name=("Nina"), image="nina")

define l = Character("Dr. Luk")

default current_cursor = 'default'
default default_mouse = "default"
# default show_case_files = False
# default show_toolbox = False
default location = "hallway"

# checking for main segment completion
default microscopy_completed = False
default lcms_completed = False
default fingerprint_completed = False

# for microscopy section
default microscope_setup = False
default microscope_focus = 2  # Start at medium focus
default phone_setup = False
default phone_focus = 5
default phone_secured_added = False

# for wet lab section
default tool = "none"
default ready_to_mix = False

### entries on afis when search
default afis_search = []
default afis_search_coordinates = [{'score_xpos': 0.53, 'xpos':0.61, 'ypos':0.505}]

init python:
    config.mouse = {
        "default": [("images/cursors/cursor.png", 10, 10)],
        "slide": [("images/Inventory Items/inventory-slide.png", 60, 60)],
        "phone": [("images/cursors/cursor.png", 10, 10)],
        "phone_holder": [("images/Toolbox Items/toolbox-phone_holder.png", 35, 30)],
        "phone_secure": [("images/cursors/cursor.png", 10, 10)]
    }

    def set_cursor(cursor):
        global default_mouse
        global current_cursor
        if current_cursor == cursor:
            default_mouse = ''
            current_cursor = ''
        else:
            default_mouse = cursor
            current_cursor = cursor
    
    def calculate_afis(evidence):
        global afis_search
        afis_search = []
        evidence.processed = True
    
        for e in afis_evidence:
            if e.processed and e!= evidence:
                afis_search.append(e)
    
    class Evidence:
        def __init__(self, name, afis_details):
            self.name = name
            self.afis_details = afis_details
            self.processed = False
    
    ### declare each piece of evidence
    laptop_fingerprint = Evidence(name = 'laptop_fingerprint',
                                afis_details = {
                                    'image': 'laptop_fingerprint',
                                    'xpos':0.18, 'ypos':0.3,
                                    'score': '70'})
    screwdriver = Evidence(name = 'screwdriver',
                        afis_details = {
                            'image': 'screwdriver_fingerprint',
                            'xpos':0.18, 'ypos':0.3,
                            'score': '70'})
    
    ### declare afis relevant evidence
    afis_evidence = [laptop_fingerprint, screwdriver]

    ### set current_evidence to track which evidence is currently active
    current_evidence = screwdriver

#################################### START #############################################
label start:
    # REQUIRED FOR INVENTORY:
    $config.rollback_enabled = False # disables rollback
    $quick_menu = False # removes quick menu (at bottom of screen) - might put this back since inventory bar moved to right side
    
    # environment:
    $environment_SM = SpriteManager(event = environmentEvents) # sprite manager that manages environment items; triggers function environmentEvents() when event happens with sprites (e.g. button click)
    $environment_sprites = [] # holds all environment sprite objects
    $environment_items = [] # holds environment items
    $environment_item_names = [] # holds environment item names
    
    # inventory
    $inventory_SM = SpriteManager(update = inventoryUpdate, event = inventoryEvents) # sprite manager that manages evidence items; triggers function inventoryUpdate 
    $inventory_sprites = [] # holds all evidence sprite objects
    $inventory_items = [] # holds evidence items
    $inventory_item_names = ["Tape on acetate", "Tapeglo in bag", "Tape photo", "Duct tape tapeglo", "Distilled water", "Tape in tweezers", "Duct tape", "Tapeglo", 
    "Fingerprint on card", "Backing card","Scalebar", "Lifting tape", "Jar photo", "Lid in tweezers", "Camel brush", "Lid with soot", "Lid", "Camphor smoke", "Lighter", 
    "Tweezers", "Gloves box", "Evidence bag", "Jar in bag", "Tape in bag", "Pvs in bag"] # holds names for inspect pop-up text 
    $inventory_db_enabled = False # determines whether up arrow on evidence hotbar is enabled or not
    $inventory_ub_enabled = False # determines whether down arrow on evidence hotbar is enabled or not
    $inventory_slot_size = (int(215 / 2), int(196 / 2)) # sets slot size for evidence bar
    $inventory_slot_padding = 120 / 2 # sets padding size between evidence slots
    $inventory_first_slot_x = 110 # sets x coordinate for first evidence slot
    $inventory_first_slot_y = 175 # sets y coordinate for first evidence slot
    $inventory_drag = False # by default, item isn't draggable

    # toolbox:
    $toolbox_SM = SpriteManager(update = toolboxUpdate, event = toolboxEvents) # sprite manager that manages toolbox items; triggers function toolboxUpdate 
    $toolbox_sprites = [] # holds all toolbox sprite objects
    $toolbox_items = [] # holds toolbox items
    $toolbox_item_names = ["Tape", "Ziploc bag", "Jar in bag", "Tape in bag", "Gun all", "Empty gun", "Cartridges", "Gun with cartridges", "Tip", "Pvs in bag"] # holds names for inspect pop-up text 
    $toolbox_db_enabled = False # determines whether up arrow on toolbox hotbar is enabled or not
    $toolbox_ub_enabled = False # determines whether down arrow on toolbox hotbar is enabled or not
    $toolbox_slot_size = (int(215 / 2), int(196 / 2)) # sets slot size for toolbox bar
    $toolbox_slot_size = (100, 100)
    $toolbox_slot_padding = 125 / 2 # sets padding size between toolbox slots
    $toolbox_slot_padding = 69
    $toolbox_first_slot_x = 110 # sets x coordinate for first toolbox slot
    $toolbox_first_slot_y = 175 # sets y coordinate for first toolbox slot
    $toolbox_drag = False # by default, item isn't draggable

    # toolbox popup:
    $toolboxpop_SM = SpriteManager(update = toolboxPopUpdate, event = toolboxPopupEvents) # sprite manager that manages toolbox pop-up items; triggers function toolboxPopUpdate
    $toolboxpop_sprites = [] # holds all toolbox pop-up sprite objects
    $toolboxpop_items = [] # holds toolbox pop-up items
    # $toolboxpop_item_names = ["Tape", "Ziploc bag", "Jar in bag", "Tape in bag", "Gun all", "Empty gun", "Cartridges", "Gun with cartridges", "Tip", "Pvs in bag"] # holds names for inspect pop-up text 
    $toolboxpop_db_enabled = False # determines whether up arrow on toolbox pop-up hotbar is enabled or not
    $toolboxpop_ub_enabled = False # determines whether down arrow on toolbox pop-up hotbar is enabled or not
    $toolboxpop_slot_size = (100, 100) # sets slot size for toolbox pop-up bar
    $toolboxpop_slot_padding = 69 # sets padding size between toolbox pop-up slots
    $toolboxpop_first_slot_x = 406 # sets x coordinate for first toolbox pop-up slot
    $toolboxpop_first_slot_y = 445 # sets y coordinate for first toolbox pop-up slot
    $toolboxpop_drag = False # by default, item isn't draggable

    # $current_scene = "scene1" # keeps track of current scene
    
    $dialogue = {} # set that holds name of character saying dialogue and dialogue message
    $item_dragged = "" # keeps track of current item being dragged
    $mousepos = (0.0, 0.0) # keeps track of current mouse position
    $i_overlap = False # checks if 2 inventory items are overlapping/combined
    $ie_overlap = False # checks if an inventory item is overlapping with an environment item

    $all_pieces = 0

    #################################### SET-UP SCENE LABEL #############################################

    # sets up environment items for first scene
    label setupScene1:

        # environment items to interact with in this scene - remember to put exact file name
        $environment_items = ["lid"]

        # python code block
        python:
            # iterate through environment items list
            for item in environment_items:
                idle_image = Image("Environment Items/{}-idle.png".format(item)) # idle version of image
                hover_image = Image("Environment Items/{}-hover.png".format(item)) # hover version of image
    
                t = Transform(child= idle_image, zoom = 0.5) # creates transform to ensure images are half size
                environment_sprites.append(environment_SM.create(t)) # creates sprite object, pass in transformed image
                environment_sprites[-1].type = item # grabs recent item in list and sets type to the item
                environment_sprites[-1].idle_image = idle_image # sets idle image
                environment_sprites[-1].hover_image = hover_image # sets hover image


                # SETTING ENV ITEM WIDTH/HEIGHT AND X, Y POSITIONS ------------------------------
            
                # for each item, make sure to set width/height to width and height of actual image
                if item == "lid":
                    environment_sprites[-1].width = 300 / 2
                    environment_sprites[-1].height = 231 / 2
                    environment_sprites[-1].x = 1000
                    environment_sprites[-1].y = 500

            # adding items to inventory/evidence box and toolbox

            addToInventory([])

            # microscopy stuff
            addToToolbox(["phone_holder", "phone"])
            addToToolboxPop(["phone_holder", "phone"])

            # wet lab stuff
            addToToolbox(["methanol", "acetic_acid", "dfo", "hfe"])
            addToInventory(["slide","gin"])


        # scene scene-1-bg at half_size - sets background image, don't need rn
        
    #################################### TRANSFORM #############################################

    # make sure to add this add the bottom of the setup labels to ensure that images are properly sized
    transform half_size:
        zoom 0.5



label lab_hallway_intro:  

    scene lab_hallway_idle

    show nina_normal

    s normal1 "Officer, good to see you again."

    hide nina_normal

    show nina_talk

    s normal2 "Great job helping Dr. Luk conduct the autopsy. I knew I could count on you!"

    s normal2 "Welcome to the lab! Here, you can process all the evidence you gathered through the autopsy."

    hide nina_talk

    show nina_think

    s normal3 "I'll need you to examine the brain biopsy more closely under the microscope."

    s normal1 "Then compare the brain biopsy with different known brain samples that we have in the lab to see if there are any abnormalities."

    hide nina_think

    show nina_talk

    s "Oh! By the way, the biopsy sample has already been prepared for you to view under the microscope."


label hallway:
    $ hide_all_inventory()
    hide nina_talk

    call screen lab_hallway_screen

label data_analysis_lab:
    
    show screen full_inventory
    show screen back_button_screen('hallway') onlayer over_screens
    call screen data_analysis_lab_screen


label afis:
    $ location = "afis"
    call screen afis_screen


label materials_lab:
    $ hide_all_inventory()

    show screen back_button_screen('hallway') onlayer over_screens
    call screen materials_lab_screen


# label fumehood:
#     show screen back_button_screen('materials_lab') onlayer over_screens
#     call screen fumehood_screen


label analytical_instruments:
    $ hide_all_inventory()

    show screen back_button_screen('materials_lab') onlayer over_screens
    call screen analytical_instruments_screen






#################################################### Microscopy Section ####################################################
############################################################################################################################

label compound_microscope:
    if microscopy_completed:
        l "We already got all we need from the microscopy section."
        jump analytical_instruments

    if microscope_setup:
        l "We have already set up the stereo microscope for the brain biopsy. You can use it to examine the sample."
        call screen analytical_instruments_screen

    show vivienne
    l "That is the wrong microscope! You need to use a microscope that can view small samples like the brain biopsy."
    hide vivienne
    
    call screen analytical_instruments_screen

label stereo_microscope:
    $ location = "stereo"

    if microscopy_completed:
        l "We already got all we need from the microscopy section."
        jump analytical_instruments

    show screen back_button_screen('analytical_instruments') onlayer over_screens

    if phone_secured_added:
        scene microscope_with_phone
        l "Let's continue where we left off."
        jump place_phone

    if microscope_setup:
        l "Let's continue where we left off."
        jump start_examining

    scene stereo_microscope_unplugged
    
    l "Yes, this is the microscope we need. Please plug it in."

    call screen stereo_microscope_plug_screen

label magnifying_glass:
    if microscopy_completed:
        l "We already got all we need from the microscopy section."
        jump analytical_instruments

    if microscope_setup:
        l "We have already set up the stereo microscope for the brain biopsy. You can use it to examine the sample."
        call screen analytical_instruments_screen

    show vivienne
    l "That is not even a microscope! You need to use a microscope that can view small samples like the brain biopsy."
    hide vivienne
    
    call screen analytical_instruments_screen

label stereo_microscope_plugged:
    scene stereo_microscope_plugged
    hide screen back_button_screen
    "The microscope is now plugged in."

    l "Nice, now place the brain biopsy slide from your inventory on the stage of the stereo microscope."

    show screen full_inventory

    call screen stereo_microscope_setup_screen

label stereo_microscope_exam:
    scene stereo_microscope_exam
    hide screen back_button_screen

    $ renpy.notify(f"Mouse: {default_mouse}")

    $ default_mouse = "default"
    $ removeToolboxItemByName("slide")

    l "Great! You can now examine the brain biopsy sample under the stereo microscope."

    $ microscope_setup = True

    label start_examining:

    l "Click on the microscope to start examining the sample."

    call screen stereo_microscope_exam


label view_microscope:
    scene stereo_microscope_exam
    hide screen back_button_screen

    l "Adjust the knob to focus the microscope."

    call screen microscope_focus_screen


label phone_segment:
    if (microscope_focus != 5):
        l "You need to adjust the focus of the microscope to see the sample clearly."

        call screen microscope_focus_screen
    
    scene table

    show screen full_inventory

    l "Perfect. Let's set up your phone using the phone holder so that it can properly attach to the microscope."

    call screen phone_setup_screen


label attach_segment:
    $ location = "phone_holder"

    $ removeToolboxItemByName("phone")
    
    call screen attach_screen


label photo_segment:
    scene phone_with_holder_on_table
    $ removeToolboxItemByName("phone_holder")

    $ location = "phone_secured"
    $ default_mouse = "default"
    $ phone_secured_added = True

    $ addToToolbox(["phone_secure"])

    l "Now, remove the lens cap from the microscope and place your phone on the microscope."

    call screen remove_lens_cap_screen


label place_phone_loop:
    if not renpy.get_screen("full_inventory"):
        show screen full_inventory
    
    $ default_mouse = "default"
    scene microscope_headless
    call screen place_phone_loop

label place_phone:
    call screen place_phone_screen

label phone_focus:

    call screen phone_focus_screen

label finished_microscopy:
    scene materials_lab

    show vivienne

    l "Good job! We got the picture. You can now compare it with known brain samples in the data analysis lab."

    $ microscopy_completed = True

    if not lcms_completed and fingerprint_completed:
        l "You still have to process the blood sample that we took from the victim's hematoma."

    elif not lcms_completed and not fingerprint_completed:
        l "You still have to process the blood sample that we took from the victim's hematoma and the alcohol bottle retrieved from the scene."
    
    else:
        l "You still have to process the finger print from the alcohol bottle retrieved from the scene."
    
    jump materials_lab

############################################################################################################################
############################################################################################################################



################################################### Finger Print Section ###################################################
############################################################################################################################


############################################################################################################################
############################################################################################################################


label end:
    hide screen back_button_screen onlayer over_screens
    show nina_normal
    n "It looks like you've analyzed all the evidence. Great work!"
    n "I hope you took note of the results. Tomorrow, you'll be testifying in court about your findings."
    hide nina_normal
    show nina_talk
    n "But for now, give yourself a pat on the back and go get some rest!"
    return

