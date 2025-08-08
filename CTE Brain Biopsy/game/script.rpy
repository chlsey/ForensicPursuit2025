define n = Character("Nina")

define l = Character("Dr. Luk")

define d = Character("")


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

    $current_scene = "scene1" # keeps track of current scene
    
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

            # addToInventory(["evidence_bag"])

            addToToolbox(["formalin"])
            addToToolboxPop(["formalin"])




        # scene scene-1-bg at half_size - sets background image, don't need rn
        
    #################################### TRANSFORM #############################################

    # make sure to add this add the bottom of the setup labels to ensure that images are properly sized
    transform half_size:
        zoom 0.5



    scene morgue

    pause 1.0

    d "Welcome to the morgue!"

    d "Here comes Nina..."

    show nina_normal with moveinbottom

    n "Hey there! Today, we've got a 35-year-old male boxer."
    
    n "He was found dead in his home with signs of a violent struggle."

    n "We suspect from family testimonies that he might have had some neurological issues so we need to conduct a brain biopsy."

    n "You'll be assisting Dr. Luk in conducting the procedure today!"

    hide nina_normal

    show nina_normal at right

    show vivienne at left with moveinleft

    l "Hi there, you'll be helping me today by handing me the right tools and ensuring that my procedure steps are correct."

    l "Let's begin."



label body_opened:

    scene body

    l "Let's start by noting any peripheral injuries and marking them in a checklist for the post-mortem report later."

    l "First, inspect each injury and click continue to proceed."

label body_start:
    # Declare checklist states
    default injury_hematoma = False
    default injury_puncture = False  
    default injury_avulsion = False 
    default injury_swelling = False 
    default injury_knuckles = False
    default injury_dental = False 
    default injury_abrasion = False 
    default injury_otorrhea = False 
    default injury_fracture = False 
    default injury_burn = False
    default injury_laceration = False

    default click_hematoma = False
    default click_knuckle1 = False
    default click_knuckle2 = False
    default click_laceration = False

    # $ addToToolbox(["pvs_kit"])

    call screen injuries_body


# SCREEN: injuries_body ------------------------------------------------------------ #
screen injuries_body:

    imagemap:
        ground "body.png"
        hover "body_heatmap.png"

        hotspot (200, 840, 200, 200) action [Hide("injuries_body"), Show("knuckle1")]
        hotspot (900, 840, 200, 200) action  [Hide("injuries_body"),Show("knuckle2")]
        hotspot (720, 350, 200, 200) action  [Hide("injuries_body"),Show("laceration")]
        
        hotspot (10, 920, 200, 150) action [
            Hide("injuries_body", transition=Dissolve(0.2)), 
            Show("injuries_legs", transition=Dissolve(0.2))
        ]  # Down to legs

        # # Clipboard hotspot to open checklist
        # hotspot (1590, 600, 500, 1000) action Call("checklist_screen", screen_to_return="injuries_body")

        hotspot (15, 400, 300, 200) action If(
            click_hematoma and click_knuckle1 and click_knuckle2 and click_laceration,
            Jump("checklist_screen"),
            Notify("Inspect all injuries before proceeding to the checklist.")
        )


# SCREEN: injuries_legs ------------------------------------------------------------ #
screen injuries_legs:

    imagemap:
        ground "legs.png"
        hover "legs_heatmap.png"

        hotspot (400, 5, 200, 300) action [Hide("injuries_legs"), Show("hematoma")]
        hotspot (0, 0, 200, 200) action [Hide("injuries_legs"), Show("injuries_body")]  # Up to body

        # # Clipboard hotspot to open checklist
        # hotspot (1590, 600, 500, 1000) action Call("checklist_screen", screen_to_return="injuries_legs")

        hotspot (15, 400, 300, 200) action If(
            click_hematoma and click_knuckle1 and click_knuckle2 and click_laceration,
            [Hide("injuries_legs", transition=Dissolve(0.2)), Call("checklist_screen")],
            Notify("Inspect all injuries before proceeding.")
        )

        $ print(f"H: {click_hematoma}, K1: {click_knuckle1}, K2: {click_knuckle2}, L: {click_laceration}")

# INJURY SCREENS ------------------------------------------------------------ #

screen hematoma:
    imagemap:
        ground "images/injury_screens/hematoma.png"
        hover "images/injury_screens/hematoma_heatmap.png"
        hotspot (1700, 0, 600, 300) action [SetVariable("click_hematoma", True), Hide("hematoma"), Show("injuries_legs")]

screen knuckle1:
    imagemap:
        ground "images/injury_screens/knuckle1.png"
        hover "images/injury_screens/knuckle1_heatmap.png"
        hotspot (1700, 0, 600, 300) action [SetVariable("click_knuckle1", True), Hide("knuckle1"), Show("injuries_body")]

screen knuckle2:
    imagemap:
        ground "images/injury_screens/knuckle2.png"
        hover "images/injury_screens/knuckle2_heatmap.png"
        hotspot (1700, 0, 600, 300) action [SetVariable("click_knuckle2", True), Hide("knuckle2"), Show("injuries_body")]

screen laceration:
    imagemap:
        ground "images/injury_screens/laceration.png"
        hover "images/injury_screens/laceration_heatmap.png"
        hotspot (1700, 0, 600, 300) action [SetVariable("click_laceration", True), Hide("laceration"), Show("injuries_body")]



label checklist_screen:
    show clipboard:  # Add transform to center it
        xalign 0.5   # Horizontal center (50% of screen width)
        yalign 0.5   # Vertical center (50% of screen height)
    
    call screen checklist  # Show the checklist screen on top
    
    hide clipboard with dissolve  # Smooth fade-out



label continue_after_checklist:
    d "All done with the checklist! Let's see how you did..."

    if injury_hematoma and injury_knuckles and injury_laceration and not (injury_puncture or injury_avulsion):
        l "Great job! You got it all correct."
    else:
        l "That was not quite right... Please try again." 
        call screen injuries_body 

    l "Let's move on to the brain biopsy."





# ------------------------------------------------BRAIN BIOPSY----------------------------------------------------

label brain_biopsy:
    scene brain_biopsy with fade

    # --- STEP 1: Make Incision ---
    l "First, I need to make a 1cm scalp incision. Select the proper tool from the tray."

    label incision_start:
    call screen incision_imagemap  # This will pause here until a jump occurs

    # Execution continues here after jump
    label after_incision:

    scene sliced with fade
    l "Moving to the next step..."

    # --- STEP 2: Drill Hole ---
    l "Now drilling a 1cm burr hole. Choose the correct tool."

    label drill_start:
    call screen drill_imagemap

    label after_drilling:
    scene drilled with fade
    l "Preparing for final step..."

    # --- STEP 3: Extract Sample ---
    l "Finally, pass me the tool to extract the brain tissue cube."

    label sample_start:
    call screen sample_imagemap

    label after_sampling:
    l "Perfect. Now please pass me the correct preservative from the inventory."

    show screen full_inventory

    label call_sample_preservation:
    $ default_mouse = "default"
    call screen sample_preservation

    $ addToInventory(["formalin"])

    $ default_mouse = default

    show screen full_inventory

    l "Great! Hold on to that in your evidence inventory. We'll be needing it again in the lab."



    label end:
        scene morgue

        show vivienne with moveinbottom

        l "Awesome work today!"

        l "Go ahead and take a look at your inventory to see if you have all the samples we collected today."

        l "See you in the lab!"

        $ renpy.quit()




    




label lab:
    scene lab_hallway_idle

    d "This is the lab."

    scene slicer

    d "Use this to prepare the brain biopsy by slicing it thin."

    scene microscope

    d "Take a look to see the brain sample up close!"

    scene look_microscope

    d "Yikes! That doesn't look normal... Let's go do some comparisons"

    scene computer

    d "Comparing our brain sample to those brains with CTE... it seems there is a m*tch."

    scene lab_hallway_idle

    show nina with moveintop

    n "Great job! Let's send this to the court for further examination."


    $ renpy.quit()




# ===== IMAGEMAP SCREENS =====
screen incision_imagemap:
    imagemap:
        ground "brain_biopsy.png"
        hover "brain_biopsy_heatmap.png"

        # Bone teether
        hotspot (1700, 20, 600, 350) action Jump("incorrect_incision")

        # scissors
        hotspot (1500, 20, 200, 340) action Jump("incorrect_incision")

        # saw
        hotspot (1150, 20, 300, 720) action Jump("incorrect_incision")
    
        # puncher
        hotspot (1450, 380, 870, 70) action Jump("incorrect_incision")

        # syringe
        hotspot (1450, 480, 870, 70) action Jump("incorrect_incision")

        # drill
        hotspot (1250, 730, 320, 800) action Jump("incorrect_incision")

        # Correct scalpel
        hotspot (1450, 20, 70, 350) action Jump("incision_complete")

screen drill_imagemap:
    imagemap:
        ground "sliced.png"
        hover "sliced_heatmap.png"
        
        # Bone teether
        hotspot (1700, 20, 600, 350) action Jump("incorrect_drill")

        # scissors
        hotspot (1500, 20, 200, 340) action Jump("incorrect_drill")

        # saw
        hotspot (1150, 20, 300, 720) action Jump("incorrect_drill")
    
        # puncher
        hotspot (1450, 380, 870, 70) action Jump("incorrect_drill")

        # syringe
        hotspot (1450, 480, 870, 70) action Jump("incorrect_drill")

        # drill
        hotspot (1250, 730, 320, 800) action Jump("drilling_complete")

        # scalpel
        hotspot (1450, 20, 70, 350) action Jump("incorrect_drill")

screen sample_imagemap:
    imagemap:
        ground "drilled.png"
        hover "drilled_heatmap.png"
        
        # Bone teether
        hotspot (1700, 20, 600, 350) action Jump("incorrect_sample")

        # scissors
        hotspot (1500, 20, 200, 340) action Jump("incorrect_sample")

        # saw
        hotspot (1150, 20, 300, 720) action Jump("incorrect_sample")
    
        # puncher
        hotspot (1450, 380, 870, 70) action Jump("biopsy_complete")

        # syringe
        hotspot (1450, 480, 870, 70) action Jump("incorrect_sample")

        # drill
        hotspot (1250, 730, 320, 800) action Jump("incorrect_sample")

        # scalpel
        hotspot (1450, 20, 70, 350) action Jump("incorrect_sample")


screen sample_preservation:
    imagemap:
        ground "hole_punch.png"
        hover "hole_punch_heatmap.png"

        hotspot (350, 200, 500, 350) action [
            If(
                default_mouse == "formalin",
                Return(True),  # Success
                [
                    Jump("call_sample_preservation")
                ]
            )
        ]

# In your script.rpy or wherever you handle the flow:
label retry_sample:
    l "Please try again with the proper preservation solution."
    $ default_mouse = "default"
    call screen sample_preservation
    return

# ===== SUCCESS LABELS =====
label incorrect_incision:
    l "That's incorrect, try again."

    jump incision_start 

label incision_complete:
    show scalpel_cut with dissolve
    l "Good. The #10 scalpel makes the cleanest incision."
    jump after_incision  # Explicitly continues the procedure

label incorrect_drill:
    l "That's incorrect, try again."

    jump drill_start 

label drilling_complete:
    show drill_hole with dissolve
    l "Correct tool. The 1cm diameter is perfect."
    jump after_drilling

label incorrect_sample:
    l "That's incorrect, try again."

    jump sample_start 

label biopsy_complete:
    show hole_punch with dissolve
    l "Excellent tissue preservation and sizing with the punch."
    jump after_sampling



screen checklist:

    frame:

        background None
        padding (0, 0)
        xpos 710
        ypos 283
        has vbox

        label "{b}Peripheral Injuries:{/b}"

        textbutton "{b}[ '◼' if injury_hematoma else '◻' ] Hematoma":
            action ToggleVariable("injury_hematoma")
            text_color "#000000"

        textbutton "{b}[ '◼' if injury_puncture else '◻' ] Puncture wound":
            action ToggleVariable("injury_puncture")
            text_color "#000000"

        textbutton "{b}[ '◼' if injury_avulsion else '◻' ] Avulsion":
            action ToggleVariable("injury_avulsion")
            text_color "#000000"

        textbutton "{b}[ '◼' if injury_swelling else '◻' ] Swelling":
            action ToggleVariable("injury_swelling")
            text_color "#000000"

        textbutton "{b}[ '◼' if injury_knuckles else '◻' ] Bloody knuckles":
            action ToggleVariable("injury_knuckles")
            text_color "#000000"

        textbutton "{b}[ '◼' if injury_dental else '◻' ] Dental injury":
            action ToggleVariable("injury_dental")
            text_color "#000000"

        textbutton "{b}[ '◼' if injury_laceration else '◻' ] Laceration":
            action ToggleVariable("injury_laceration")
            text_color "#000000"





        # textbutton "{b}Back{/b}":
        #     action Return()
        #     text_color "#000000"

        textbutton "{b}Continue{/b}":
            action Return()
            text_color "#000000"



