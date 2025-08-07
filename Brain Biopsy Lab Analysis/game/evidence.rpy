init python:
    class Evidence_v2:
        """A custom data type that represents data for an evidence."""
        name: str
        processed: bool
        available: bool
        image: str
        description: str
        xpos: float
        ypos: float

        def __init__(self, name: str, image: str = "", description: str = "", xpos: float = 0, ypos: float = 0) -> None:
            """Initialize a new Evidence_v2 object."""
            self.name = name
            self.processed = False
            self.available = True
            self.image = image
            self.description = description
            self.xpos = xpos
            self.ypos = ypos
        
        def update_name(self, new_name: str) -> None:
            self.name = new_name
        
        def process_evidence(self) -> None:
            self.processed = True
        
        def disable_evidence(self) -> None:
            self.available = False
        
        def enable_evidence(self) -> None:
            self.available = True
        
        def update_image(self, new_image: str) -> None:
            self.image = new_image
        
        def update_description(self, new_desc: str) -> None:
            self.description = new_desc
        
        def update_xpos(self, new_xpos: float) -> None:
            self.xpos = new_xpos
        
        def update_ypos(self, new_ypos: float) -> None:
            self.ypos = new_ypos
        
    def update_evidence(evidence: Evidence_v2, image: str = "", desc: str = "") -> None:
        """Updates a piece of evidence in the inventory and notifies the player.
        If provided, the image and the description are updated as well.
        """
        if image != "": 
            evidence.update_image(image)
        if desc != "": 
            evidence.update_description(desc) 
        renpy.say(None, "The {evidence.name} has been updated.")

    def create_evidence(name: str, image: str = "", description: str = "", xpos: float = 0, ypos: float = 0) -> Evidence_v2:
        """Creates a new piece of evidence with the provided attributes.
        """
        return Evidence_v2(
            name = name,
            image = image,
            description = description,
            xpos = xpos,
            ypos = ypos
        )

    def label_function() -> None:
        global location
        global imported_print
        global oven
        if location == "fumehood":
            hide_all_inventory()
            renpy.jump("fumehood_label_v2")
        elif location == "oven" and oven.state == "preheated" and label.dipped:
            hide_all_inventory()
            renpy.jump("label_placed_in_oven")
        elif location == "afis" and label.processed:
            imported_print = "print_4"
            renpy.jump("import_print")

    def label_function_alt() -> None:
        global location
        global imported_print
        global oven
        if location == "fumehood":
            renpy.hide_screen("casefile_physical")
            renpy.jump("fumehood_label_v2")
        elif location == "oven" and oven.state == "preheated" and label.dipped:
            renpy.hide_screen("casefile_physical")
            renpy.jump("label_placed_in_oven")
        elif location == "afis" and label.processed:
            imported_print = "print_4"
            renpy.jump("import_print")

    gin = Evidence_v2(
        name = "gin bottle",
        image = "gin %s",
        description = "The gin bottle collected from the table at the crime scene. The label may contain some prints."
    )

    label = Evidence_v2(
        name = "label",
        image = "label_%s",
        description = "The label collected from the gin bottle. May contain prints."
    )

    # Additional attribute for label
    label.dipped = False
