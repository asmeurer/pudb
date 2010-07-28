def get_palette(may_use_fancy_formats):
    if may_use_fancy_formats:
        def add_setting(color, setting):
            return color+","+setting
    else:
        def add_setting(color, setting):
            return color

    return [
        ("header", "black", "light gray", "standout"),

        ("breakpoint source", "yellow", "dark red"),
        ("breakpoint focused source", "black", "dark red"),
        ("current breakpoint source", "black", "dark red"),
        ("current breakpoint focused source", "white", "dark red"),

        ("variables", "white", "default"),
        ("variable separator", "dark cyan", "light gray"),

        ("var label", "dark blue", "default"),
        ("var value", "white", "default"),
        ("focused var label", "dark blue", "dark green"),
        ("focused var value", "black", "dark green"),

        ("highlighted var label", "white", "dark cyan"),
        ("highlighted var value", "black", "dark cyan"),
        ("focused highlighted var label", "white", "dark green"),
        ("focused highlighted var value", "black", "dark green"),

        ("return label", "white", "dark blue"),
        ("return value", "black", "dark cyan"),
        ("focused return label", "light gray", "dark blue"),
        ("focused return value", "black", "dark green"),

        ("return label", "white", "dark blue"),
        ("return value", "black", "dark cyan"),
        ("focused return label", "light gray", "dark blue"),
        ("focused return value", "black", "dark green"),

        ("stack", "white", "default"),

        ("frame name", "white", "default"),
        ("focused frame name", "black", "dark green"),
        ("frame class", "dark blue", "default"),
        ("focused frame class", "dark blue", "dark green"),
        ("frame location", "light cyan", "default"),
        ("focused frame location", "light cyan", "dark green"),

        ("current frame name", add_setting("white", "bold"),
            "default"),
        ("focused current frame name", add_setting("white", "bold"),
            "dark green", "bold"),
        ("current frame class", "dark blue", "default"),
        ("focused current frame class", "dark blue", "dark green"),
        ("current frame location", "light cyan", "default"),
        ("focused current frame location", "light cyan", "dark green"),

        ("breakpoint", "default", "default"),
        ("focused breakpoint", "black", "dark green"),

        ("selectable", "black", "dark cyan"),
        ("focused selectable", "black", "dark green"),

        ("button", "white", "dark blue"),
        ("focused button", "light cyan", "black"),

        ("background", "black", "light gray"),
        ("hotkey", add_setting("black", "underline"), "light gray", "underline"),
        ("focused sidebar", "yellow", "light gray", "standout"),

        ("warning", add_setting("white", "bold"), "dark red", "standout"),

        ("label", "black", "light gray"),
        ("value", "yellow", "dark blue"),
        ("fixed value", "light gray", "dark blue"),

        ("search box", "default", "default"),
        ("search not found", "white", "dark red"),

        ("dialog title", add_setting("white", "bold"), "dark cyan"),

        # highlighting
        ("source", "white", "default"),
        ("focused source", "black", "dark green"),
        ("highlighted source", "white", "light cyan"),
        ("current source", "white", "light gray"),
        ("current focused source", "white", "brown"),
        ("current highlighted source", "white", "dark cyan"),

        ("keyword", "dark magenta", "default"),
        ("kw_namespace", "dark magenta", "default"),
        ("literal", "dark cyan", "default"),
        ("string", "light red", "default"),
        ("punctuation", "white", "default"),
        ("comment", "dark green", "default"),
        ("classname", "dark cyan", "default"),
        ("funcname", "white", "default"),

        ]

