from .entity import Entity


class Bat(Entity):
    def __init__(self):
        super().__init__("murciélago")

    def draw(self) -> str:
        return """
      ,*-~"`^"*u_                                _u*"^`"~-*,
   p!^       /  jPw                            w9j \        ^!p
 w^.._      /      "\_                      _/"     \        _.^w
      *_   /          \_      _    _      _/         \     _* 
        q /           / \q   ( `--` )   p/ \          \   p
        jj5****._    /    ^\_) o  o (_/^    \    _.****6jj
                 *_ /   "==) ;; (=="         \ _*
                  `/.w***,   /(    )\   ,***w.\"
                   ^ ilmk ^c/ )    ( \c^      ^
                           'V')_)(_('V'
                               `` ``
        """
