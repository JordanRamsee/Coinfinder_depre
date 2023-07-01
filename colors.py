"""
├──────┴────────────────────┴───────┴──────────────────────┤
│                       Description                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│                                                          │
└──────────────────────────────────────────────────────────┘
"""


class Colors__:
    def __init__(self):
        self.color()
        pass

    def color():
        color_library = {
            "navigation bar": {"bg": "#1d1d2c",
                                "fg": {"normal": "#71718c", "hover": "#a9a9b5", "selected": "#ffffff"},
                                "selected tab": "#171721"
                                },
            "working space": {"bg": "#171721",
                            },
            "task" : {"bg": "#1a192b",
                      "fg" : "#717174",
                      "active fg" : "#b8b8ba",
                      "separator" : "#5a5a5b",
                      "action bg" : "#151422",
                    },


        }


        return color_library



# print(Colors__.color()["navigation bar"]["bg"])