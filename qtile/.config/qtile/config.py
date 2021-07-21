# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger

# Importando os para manipular el sistema operativo
import os

Colors = {
    "activeFocus": "#f1ffff",
    "inactiveFocus": "#4c566a",
    "focusActive": "#a151d3",
    "focusInactive": "#F07178",
    "inactiveOther": "#252525"
}

# Definiendo teclas maestras (super, alt)
mod = "mod4"
alt = "mod1"

terminal = "tilix"


widgets_space = 1; # Espaciado de los witgets
keys = [

    # /----/ /----/ /---- Manipular Ventanas ----/ /----/ /----/

    # Moverse entre ventanas 
    Key([mod], "h", lazy.layout.left(), 
    desc="Mover el enfoque a la izquierda"),
    Key([mod], "l", lazy.layout.right(), 
    desc="Mover el enfoque a la derecha"),
    Key([mod], "j", lazy.layout.down(), 
    desc="Mover el enfoque hacia abajo"),
    Key([mod], "k", lazy.layout.up(), 
    desc="Mover el enfoque hacia arriba"),
    Key([mod], "space", lazy.layout.next(),
        desc="Se enfoca en la siguiente ventana"),

    # Intercambiar ventanas de la pila
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Mover ventana a la izquierda"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Mover ventana a la derecha"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Mover ventana hacia abajo"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), 
        desc="Mover ventana hacia arriba"),

    # Modificar tamaño de las ventanas (modo colums)
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Hacer crecer la ventana a la izquierda"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Hacer crecer la ventana a la derecha"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Hacer crecer la ventana hacia abajo"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), 
        desc="Hacer crecer la ventana hacia arriba"),
    Key([mod], "n", lazy.layout.normalize(), 
        desc="Formatear el tamaño de las ventanas"),

    # Modificar tamaño de las ventanas 
    Key([mod, "control"], "h", lazy.layout.grow(),
        desc="Hacer crecer la ventana"),
    Key([mod, "control"], "l", lazy.layout.shrink(),
        desc="Hacer encogerse la ventana"),
    Key([mod, "control"], "n", lazy.layout.normalize(),
        desc="Volver al estado normal de las ventanas"),
    Key([mod, "control"], "o", lazy.layout.maximize(),
        desc="Intercambiar el tamaño entre dos ventanas"),
    Key([mod, "control"], "space", lazy.layout.flip(),
        desc="Intercambiar horizontalmente, la posicion de las ventanas"),
    
    Key([mod], "Tab", lazy.next_layout(), desc="Cambiar gentre layouts"),

    Key([mod], "z", lazy.window.kill(), desc="Cerrar la ventana actual"),

    Key([mod, "control"], "r", lazy.restart(), desc="Reiniciar Qtile"),

    Key([mod, "control"], "q", lazy.shutdown(), desc="Cerrar Qtile"),

    # Cambiar entre monitores
    Key([mod], "period", lazy.next_screen(), desc="Cambiar gentre layouts"),
    Key([mod], "comma", lazy.prev_screen(), desc="Cambiar gentre layouts"),
    
    # /----/ /----/ /---- Aplicaciones ----/ /----/ /----/
        
    # Menu de aplicaciones
    Key([alt], "d", lazy.spawn("rofi -show drun")),

    # Ejecutar terminal
    Key([mod], "Return", lazy.spawn("kitty"),
        desc="Ejecuta la terminal"),

    Key([alt], "p", lazy.spawn("flameshot gui"),
        desc="Captura de pantalla"),

]

# Lista de grupos
groups = [Group(i) for i in [
    "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Mod + un numero,  me lleva a ese escritorio
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Mod + shift + un numero,  mueve la ventana seleccionada a ese escritorio
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layouts = [
    # layout.Columns(border_focus_stack='#d75f5f'),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_width=3, # borde de la ventana
        border_focus=Colors["focusInactive"], # Color del borde de la ventana
        border_normal=Colors["inactiveFocus"],
        single_border_width=0,
        margin=8,
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Configurar fuente y espaciado de la barra
widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(
                        font='UbuntuMono Nerd Font',
                        fontsize=16,
                        margin_y=3,
                        margin_x=0,
                        padding_y=8,
                        padding_x=5,
                        borderwidth=1,
                        active=Colors["activeFocus"], # Color del logo, del escritorio activo
                        inactive=Colors["inactiveFocus"], # Color del logo, del escritorio inactivo
                        rounded=False, 
                        highlight_method='block',
                        urgent_alert_method='block',
                        this_current_screen_border=Colors["focusActive"], # Color del escritorio seleccionado de la pantalla enfocada
                        this_screen_border=Colors["focusInactive"], # Color del escritorio seleccionado de la pantalla no enfocada
                        other_current_screen_border=Colors["inactiveOther"], # Color del escritorio no seleccionado de la pantalla no enfocada
                        other_screen_border=Colors["inactiveOther"], # Color del escritorio no seleccionado de la pantalla enfocada
                        disable_drag=True
                ),
                widget.WindowName(
                    fontsize=12,
                    background=Colors["focusActive"],
                    empty_group_string="Null",
                    padding=10,
                ),
                # widget.Battery(
                #     fontsize=14,
                #     discharge_char='  ',
                #     charge_char='  ',
                #     full_char='  ',
                #     foreground=Colors["inactiveFocus"],
                #     format='{char} {percent:2.0%}'
                #),
                # widget.Spacer( length=widgets_space ),
                # widget.TextBox(
                #     "|",
                #     name="separador-1",
                #     foreground=Colors["inactiveFocus"],
                #     fontsize=18
                #),
                widget.Spacer( length=12),
                widget.CPU(
                    fontsize=14,
                    foreground=Colors["inactiveFocus"],
                    format='  {load_percent}%'
                ),
                widget.Spacer( length=widgets_space ),
                widget.TextBox(
                    "|",
                    name="separador-1",
                    foreground=Colors["inactiveFocus"],
                    fontsize=18
                ),
                widget.Spacer( length=widgets_space ),
                widget.Memory(
                    fontsize=14,
                    format='  {MemUsed: .0f}Mb /{MemTotal: .0f}Mb',
                    foreground=Colors["inactiveFocus"],
                ),
                widget.Spacer( length=widgets_space ),
                widget.TextBox(
                    "|",
                    name="separador-1",
                    foreground=Colors["inactiveFocus"],
                    fontsize=18
                ),
                widget.Spacer( length=widgets_space ),
                widget.Clock(
                    fontsize=14,
                    foreground=Colors["inactiveFocus"],
                    format='  %Y-%m-%d   %I:%M'
                ),
                widget.Spacer( length=widgets_space ),
                widget.TextBox(
                    "|",
                    name="separador-1",
                    foreground=Colors["inactiveFocus"],
                    fontsize=18
                ),
                widget.Spacer( length=widgets_space ),
                widget.KeyboardLayout(
                    fontsize=14,
                    foreground=Colors["inactiveFocus"],                    
                ),
                widget.Spacer( length=widgets_space ),
            ],
            28, # Grosor de la barra
            background="#0f101a",
            opacity=1
        ),
    ),
Screen(
        top=bar.Bar(
            [
                # widget.CurrentLayout(),
                widget.GroupBox(
                        font='UbuntuMono Nerd Font',
                        fontsize=19,
                        margin_y=3,
                        margin_x=0,
                        padding_y=8,
                        padding_x=5,
                        borderwidth=1,
                        active=Colors["activeFocus"], # Color del logo, del escritorio activo
                        inactive=Colors["inactiveFocus"], # Color del logo, del escritorio inactivo
                        rounded=False, 
                        highlight_method='block',
                        urgent_alert_method='block',
                        this_current_screen_border=Colors["focusActive"], # Color del escritorio seleccionado de la pantalla enfocada
                        this_screen_border=Colors["focusInactive"], # Color del escritorio seleccionado de la pantalla no enfocada
                        other_current_screen_border=Colors["inactiveOther"], # Color del escritorio no seleccionado de la pantalla no enfocada
                        other_screen_border=Colors["inactiveOther"], # Color del escritorio no seleccionado de la pantalla enfocada
                        disable_drag=True
                ),
                widget.WindowName(
                    fontsize=14,
                    background=Colors["focusActive"],
                    empty_group_string="Null",
                    padding=10,
                ),
                widget.Battery(
                    fontsize=16,
                    discharge_char='  ',
                    charge_char='  ',
                    full_char='  ',
                    foreground=Colors["inactiveFocus"],
                    format='{char} {percent:2.0%}'
                ),
                widget.Spacer( length=widgets_space ),
                widget.TextBox(
                    "|",
                    name="separador-1",
                    foreground=Colors["inactiveFocus"],
                    fontsize=18
                ),
                widget.Spacer( length=widgets_space ),
                widget.CPU(
                    fontsize=16,
                    foreground=Colors["inactiveFocus"],
                    format='  {load_percent}%'
                ),
                widget.Spacer( length=widgets_space ),
                widget.TextBox(
                    "|",
                    name="separador-1",
                    foreground=Colors["inactiveFocus"],
                    fontsize=18
                ),
                widget.Spacer( length=widgets_space ),
                widget.Memory(
                    format='  {MemUsed: .0f}Mb /{MemTotal: .0f}Mb',
                    foreground=Colors["inactiveFocus"],
                ),
                widget.Spacer( length=widgets_space ),
                widget.TextBox(
                    "|",
                    name="separador-1",
                    foreground=Colors["inactiveFocus"],
                    fontsize=18
                ),
                widget.Spacer( length=widgets_space ),
                widget.Clock(
                    fontsize=16,
                    foreground=Colors["inactiveFocus"],
                    format='  %Y-%m-%d   %I:%M'
                ),
                widget.Spacer( length=widgets_space ),
                widget.TextBox(
                    "|",
                    name="separador-1",
                    foreground=Colors["inactiveFocus"],
                    fontsize=18
                ),
                widget.Spacer( length=widgets_space ),
                widget.KeyboardLayout(
                    fontsize=16,
                    foreground=Colors["inactiveFocus"],                    
                ),
                widget.Spacer( length=widgets_space ),
            ],
            28, # Grosor de la barra
            background="#0f101a",
            opacity=1
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


# Array con los comandos a ejecutar en el inicio
autostart = [
    "setxkbmap us",
    #"xrandr --output DP1 --mode 1920x1080 --right-of eDP1",
    "feh --bg-fill /home/source/Imágenes/Fondos-de-pantalla/Minimalismo-1.jpg",
    #"picom &",
]


# Ejecutar cada comando del array
for x in autostart:
    os.system(x)

