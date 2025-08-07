# initial screen
screen lab_hallway_screen:
    image "lab_hallway_dim"
    hbox:
        xpos 0.20 yalign 0.5
        imagebutton:
            idle "data_analysis_lab_idle"
            hover "data_analysis_lab_hover"
            hovered Notify("Data Analysis Lab")
            unhovered Notify('')
            action Jump('data_analysis_lab')
    hbox:
        xpos 0.55 yalign 0.48
        imagebutton:
            idle "materials_lab_idle"
            hover "materials_lab_hover"
            hovered Notify("Materials Lab")
            unhovered Notify('')
            action Jump('materials_lab')

############################## DATA ANALYSIS ##############################
screen data_analysis_lab_screen:
    image "afis_interface"
    hbox:
        xpos 0.25 yalign 0.25
        imagebutton:
            idle "afis_software_idle"
            hover "afis_software_hover"
            action Jump('afis')

screen afis_screen:
    default afis_bg = "software_interface"
    default interface_import = False
    default interface_imported = False
    default interface_search = False
    image afis_bg

    hbox:
        xpos 0.35 ypos 0.145
        textbutton('Import'):
            style "afis_button"
            action [
                ToggleLocalVariable('interface_import'),
                Show("inventory"), Hide("toolbox"),
                SetLocalVariable('interface_imported', False),
                SetLocalVariable('interface_search', False),
                SetLocalVariable('afis_bg', 'software_interface'),
                Function(set_cursor, '')]
    
    hbox:
        xpos 0.55 ypos 0.145
        textbutton('Search'):
            sensitive not interface_search
            style "afis_button"
            action [
                ToggleLocalVariable('interface_search'),
                SetLocalVariable('afis_bg', 'software_search'),
                Function(calculate_afis, current_evidence),
                Function(set_cursor, '')]
    
    showif interface_import:
        imagemap:
            idle "software_interface"
            hover "software_import_hover"
            
            ## add in sensitive when clicked on evidence 

            hotspot (282,241,680,756) action [
                SetLocalVariable('interface_import', False), 
                SetLocalVariable('interface_imported', True),
                Function(set_cursor, '')]

    showif interface_imported:
        hbox:
            xpos current_evidence.afis_details['xpos'] ypos current_evidence.afis_details['ypos']
            image current_evidence.afis_details['image']
    
    showif interface_search:
        if afis_search:
            for i in range(len(afis_search)):
                hbox:
                    xpos afis_search_coordinates[i]['xpos'] ypos afis_search_coordinates[i]['ypos']
                    hbox:
                        text("{color=#000000}"+afis_search[i].name+"{/color}")
                hbox:
                    xpos afis_search_coordinates[i]['score_xpos'] ypos afis_search_coordinates[i]['ypos']
                    hbox:
                        text("{color=#000000}"+afis_search[i].afis_details['score']+"{/color}")
            
        else:
            hbox:
                xpos 0.57 yalign 0.85
                hbox:
                    text("{color=#000000}No match found in records.{/color}")

    

    
#################################### MATERIALS ####################################
screen materials_lab_screen:
    image "materials_lab"

    hbox:
        xpos 0.15 yalign 0.5
        imagebutton:
            idle "fumehood_idle" at Transform(zoom=0.8)
            hover "fumehood_hover"
            hovered Notify("Fume Hood")
            unhovered Notify('')
            action [SetVariable("location", "fumehood"), Jump("fumehood")]
    hbox:
        #xpos 0.4 yalign 0.5
        xpos 0.33 yalign 0.47
        imagebutton:
            # idle "fingerprint_development_idle" at Transform(zoom=0.8)
            # hover "fingerprint_development_hover"
            auto "oven_%s" at Transform(zoom=0.43)
            hovered Notify("Oven")
            unhovered Notify('')
            action Jump("oven")
        # text "Dry Oven" xpos 0.31 ypos 0.66
    
    hbox:
        #xpos 0.4 yalign 0.5
        xpos 0.48 yalign 0.53
        imagebutton:
            idle "lab_bench_idle" at Transform(zoom=0.8)
            hover "lab_bench_hover"
            hovered Notify("Lab Bench")
            unhovered Notify('')
            action NullAction()
    
    hbox:
        xpos 0.62 yalign 0.5
        imagebutton:
            idle "analytical_instruments_idle"
            hover "analytical_instruments_hover"
            hovered Notify("Analytical Instruments")
            unhovered Notify('')
            action Jump('analytical_instruments')

screen fumehood_screen:
    image "fumehood"

screen analytical_instruments_screen:
    image "lab_bench"

    hbox:
        xpos 0.2 yalign 0.30
        imagebutton:
            idle "compound_microscope_idle" at Transform(zoom=0.8)
            hover "compound_microscope_hover"
            hovered Notify("Compound Microscope")
            unhovered Notify('')
            action Jump('compound_microscope')

    hbox:
        xpos 0.45 yalign 0.30
        imagebutton:
            idle "stereo_microscope_idle" at Transform(zoom=0.8)
            hover "stereo_microscope_hover"
            hovered Notify("Stereo Microscope")
            unhovered Notify('')
            action Jump('stereo_microscope')
    
    hbox:
        xpos 0.7 yalign 0.30
        imagebutton:
            idle "magnifying_glass_idle" at Transform(zoom=0.8)
            hover "magnifying_glass_hover"
            hovered Notify("Magnifying Glass")
            unhovered Notify('')
            action Jump('magnifying_glass')





###########################  Microscopy Section  ###############################################
################################################################################################

screen stereo_microscope_plug_screen:
    imagemap:
        ground "stereo_microscope_unplugged"
        hover "stereo_microscope_unplugged_hover"
        
        # Stereo microscope
        hotspot (400, 300, 200, 200) action Jump("stereo_microscope_plugged")

screen stereo_microscope_setup_screen:
    imagemap:
        ground "stereo_microscope_plugged"
        hover "stereo_microscope_no_sample_hover"

        # Stereo microscope
        hotspot (620, 400, 600, 400) action Function(_check_mouse_state1)


########## Function to check mouse = slide ##########
init python:
    def _check_mouse_state1():
        renpy.notify(f"default_mouse is: {default_mouse}")
        if default_mouse == "slide":
            renpy.jump("stereo_microscope_exam")
            
#####################################################


screen stereo_microscope_exam:
    imagemap:
        ground "stereo_microscope_exam"
        hover "stereo_microscope_exam_hover"

        hotspot (700, 0, 400, 450) action Jump("view_microscope")


screen microscope_focus_screen:
    modal True
    zorder 100

    add "microscope_focus_[microscope_focus]"  # dynamic image name

    vbox:
        xalign 0.9
        yalign 0.8
        spacing 10

        text "Adjust Focus" color "#fff"

        textbutton "Focus In" action If(microscope_focus < 6, SetVariable("microscope_focus", microscope_focus + 1))
        textbutton "Focus Out" action If(microscope_focus > 1, SetVariable("microscope_focus", microscope_focus - 1))
        textbutton "Done" action Jump("phone_segment")


screen phone_setup_screen:
    if default_mouse == "phone":
        timer 0.1 action Jump("attach_segment") repeat False

screen attach_screen:
    imagemap:
        ground "phone_on_table"
        hover "phone_on_table_hover"

        hotspot (700, 100, 600, 1050) action Function(_check_mouse_state2)


####### Function to check mouse = phone_holder #######
init python:
    def _check_mouse_state2():
        renpy.notify(f"default_mouse is: {default_mouse}")
        if default_mouse == "phone_holder":
            renpy.jump("photo_segment")
            
#####################################################


screen remove_lens_cap_screen:
    imagemap:
        ground "microscope_closeup"
        hover "microscope_closeup_hover"

        hotspot (700, 0, 400, 450) action [SetVariable("default_mouse", "default"), Jump("place_phone_loop")]

screen place_phone_loop:
    if default_mouse == "phone_secure":
        timer 0.1 action Jump("place_phone")

screen place_phone_screen:
    imagemap:
        ground "microscope_with_phone"
        hover "microscope_with_phone_hover"

        hotspot (400, 0, 1000, 650) action Jump("phone_focus")


screen phone_focus_screen:
    modal True
    zorder 100

    add "phone_focus_[phone_focus]"  # dynamic image name

    vbox:
        xalign 0.9
        yalign 0.8
        spacing 10

        text "Adjust Phone" color "#fff"

        textbutton "Move Up" action If(phone_focus < 5, SetVariable("phone_focus", phone_focus + 1))
        textbutton "Move Down" action If(phone_focus > 1, SetVariable("phone_focus", phone_focus - 1))
        textbutton "Take Photo" action Function(_check_photo)


############# Function to photo quality #############
init python:
    def _check_photo():
        if phone_focus != 3:
            renpy.notify("Come on, you can do better than that!")
            renpy.call_in_new_context("phone_focus")
            return

        renpy.call_in_new_context("finished_microscopy")
            
#####################################################


################################################################################################
################################################################################################



###########################  Wet Lab Section  ##################################################
################################################################################################
