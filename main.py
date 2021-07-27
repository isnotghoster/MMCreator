#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import ruamel.yaml

from ruamel.yaml.scalarstring import PreservedScalarString as pss
from pprint import pformat
from PyQt5 import QtWidgets

from help_wind import Ui_hw
from main_wind import Ui_Designer
from mob_wind import Ui_Mob
from ma_wind import Ui_mob_acc


class MainMM(QtWidgets.QMainWindow, Ui_Designer):
    def __init__(self):
        super(MainMM, self).__init__()
        self.ui = Ui_Designer()
        self.ui.setupUi(self)

        self.ui.help.clicked.connect(self.help_click)
        self.ui.New_mob.clicked.connect(self.me_click)
        self.ui.exit.clicked.connect(self.exit)

        self.mob_wind = None
        self.help_wind = None

    def help_click(self):
        if not self.help_wind:
            self.help_wind = HelpMM()
        self.close()
        self.help_wind.show()

    def me_click(self):
        if not self.mob_wind:
            self.mob_wind = EditMM()
        self.close()
        self.mob_wind.show()

    def exit(self):
        self.close()


class HelpMM(QtWidgets.QMainWindow, Ui_hw):
    def __init__(self):
        super(HelpMM, self).__init__()
        self.ui = Ui_hw()
        self.ui.setupUi(self)

        self.ui.back.clicked.connect(self.back_click)

        self.main_wind = None

    def back_click(self):
        if not self.main_wind:
            self.main_wind = MainMM()
        self.close()
        self.main_wind.show()


class EditMM(QtWidgets.QMainWindow, Ui_Mob):
    def __init__(self):
        super(EditMM, self).__init__()
        self.ui = Ui_Mob()
        self.ui.setupUi(self)

        self.to_yaml: None

        self.ui.next.clicked.connect(self.next_click)
        self.ui.back.clicked.connect(self.back_click)

        self.ui.b_enable_2.toggled.connect(self.bb_clicked)

        self.ui.PODrop_2.toggled.connect(self.drop_clicked)

        self.ui.Despawn_2.toggled.connect(self.despawn_clicked)

        self.enable_bb = False
        self.enable_drop = False
        self.enable_despawn = False

        self.main_wind = None
        self.mob_accept = None

    def back_click(self):
        if not self.main_wind:
            self.main_wind = MainMM()
        self.close()
        self.main_wind.show()

    def next_click(self):
        title = self.ui.b_title_2.text()
        range = int(self.ui.b_range_2.value())
        color = str(self.ui.b_color_2.currentText())
        style = str(self.ui.b_style_2.currentText())
        self.ui.debag.setText(f"{str(self.enable_despawn), str(self.enable_drop), str(self.enable_bb)}")

        self.to_yaml = pss("""\
        mobius:
            Type: {0}
            Display: '{1}'
            Health: {2}
            Damage: {3}
            Faction: {4}
            Mount: {5}
            Options:
                MovementSpeed: {6}
                PreventOtherDrops: {7}
                MaxCombatDistance: {8}
                KnockbackResistance: {9}
                Despawn: {10}
            Equipment:
                - {11} HEAD
                - {12} CHEST
                - {13} LEGS
                - {14} FEET
                - {15} HAND
                - {16} OFFHAND
            BossBar:
                Enabled: {17}
                Title: '{18}'
                Range: {19}
                Color: {20}
                Style: {21}
        """.format(self.ui.npc_type.currentText(),  # 0
                   self.ui.display_2.text(),  # 1
                   self.ui.health_2.value(),  # 2
                   self.ui.damage_2.value(),  # 3
                   self.ui.faction_2.currentText(),  # 4
                   self.ui.mount_2.currentText(),  # 5
                   self.ui.MoveSpeed_2.value(),  # 6
                   self.enable_drop,  # 7
                   self.ui.MCDist_2.value(),  # 8
                   self.ui.KBResist_2.value(),  # 9
                   self.enable_despawn,  # 10
                   self.ui.mount_2.currentText(),  # 11
                   self.ui.chestplate.currentText(),  # 12
                   self.ui.leggings.currentText(),  # 13
                   self.ui.boots.currentText(),  # 14
                   self.ui.hand.currentText(),  # 15
                   self.ui.offhand.currentText(),  # 16
                   self.enable_bb,  # 17
                   title,  # 18
                   range,  # 19
                   color,  # 20
                   style  # 21
                   ))

        if not self.mob_accept:
            self.mob_accept = AcceptMM(self.to_yaml)
        self.close()
        self.mob_accept.show()

    def bb_clicked(self):
        if self.ui.b_enable_2.isChecked():
            self.enable_bb = True
            self.ui.b_enable_2.setText("true")
        else:
            self.enable_bb = False
            self.ui.b_enable_2.setText("false")

    def drop_clicked(self):
        if self.ui.PODrop_2.isChecked():
            self.enable_drop = True
            self.ui.PODrop_2.setText("true")
        else:
            self.enable_drop = False
            self.ui.PODrop_2.setText("false")

    def despawn_clicked(self):
        if self.ui.Despawn_2.isChecked():
            self.enable_despawn = True
            self.ui.Despawn_2.setText("true")
        else:
            self.enable_despawn = False
            self.ui.Despawn_2.setText("false")


class AcceptMM(QtWidgets.QMainWindow, Ui_mob_acc):
    def __init__(self, cfg_yml):
        super(AcceptMM, self).__init__()
        self.ui = Ui_mob_acc()
        self.ui.setupUi(self)

        self.to_yaml = cfg_yml

        self.ui.abort.clicked.connect(self.back_click)
        self.ui.save.clicked.connect(self.save)
        self.ui.label.setText(pformat(self.to_yaml))

        self.mob_wind = None

    def back_click(self):
        if not self.mob_wind:
            self.mob_wind = EditMM()
        self.close()
        self.mob_wind.show()

    def save(self):
        with open('./MOB.yml', 'w') as f:
            def fixing():
                file = open('./MOB.yml', 'r')
                replace_text = file.read()
                file.close()

                f = open('./MOB.yml', 'w')
                f.write(replace_text.replace("|2-", "noting"))
                f.close()

            yaml = ruamel.yaml.YAML()
            yaml.default_flow_style = False
            yaml.dump(self.to_yaml, f)
            f.close()

            fixing()

            self.ui.label.setText("ВСЁ")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainMM()
    main.show()
    app.exec_()

# to_yaml = """\
#                 {}:
#                     Type: {}
#                     Display: '{}'
#                     Health: {}
#                     Damage: {}
#                     Faction: {}
#                     Mount: {}
#                     Equipment:
#                         - {} HEAD
#                         - {} CHEST
#                         - {} LEGS
#                         - {} FEET
#                         - {} HAND
#                         - {} OFFHAND
#                     BossBar:
#                         Enabled: {}
#                         Title: '{}'
#                         Range: {}
#                         Color: {}
#                         Style: {}
#                 """.format(self.ui.name_class_2.text(),
#                            self.ui.npc_type.currentText(),
#                            self.ui.display_2.text(),
#                            self.ui.health_2.value(),
#                            self.ui.damage_2.value(),
#                            self.ui.faction_2.currentText(),
#                            self.ui.mount_2.currentText(),
#                            self.ui.mount_2.currentText(),
#                            self.ui.chestplate.currentText(),
#                            self.ui.leggings.currentText(),
#                            self.ui.boots.currentText(),
#                            self.ui.hand.currentText(),
#                            self.ui.offhand.currentText(),
#                            self.enable,
#                            title,
#                            range,
#                            color,
#                            style
#                            )

# yaml = ruamel.yaml.YAML()
# yaml.preserve_quotes = True

# yaml_str = """\
# a: "hello world"
# """
#
# yaml = ruamel.yaml.YAML()
# yaml.preserve_quotes = True
# data = yaml.load(yaml_str)
# yaml.dump(data, sys.stdout)
# self.to_yaml = pss(
# "\nname:"
# "\n    Type: "+str(self.ui.npc_type.currentText)+""
# "\n    Display: '"+str(self.ui.display_2.text)+"'"
# "\n    Health: "+str(self.ui.health_2.value)+""
# "\n    Damage: "+str(self.ui.damage_2.value)+""
# "\n    Faction: "+str(self.ui.faction_2.currentText)+""
# "\n    Mount: "+str(self.ui.mount_2.currentText)+""
# "\n    Equipment:\n"
# "\n        - "+str(self.ui.mount_2.currentText)+" HEAD"
# "\n        - "+str(self.ui.chestplate.currentText)+" CHEST"
# "\n        - "+str(self.ui.leggings.currentText)+" LEGS"
# "\n        - "+str(self.ui.boots.currentText)+" FEET"
# "\n        - "+str(self.ui.hand.currentText)+" HAND"
# "\n        - "+str(self.ui.offhand.currentText)+" OFFHAND"
# "\n    BossBar:\n"
# "\n        Enabled: "+self.enable+""
# "\n        Title: '"+title+"'"
# "\n        Range: "+str(range)+""
# "\n        Color: "+color+""
# "        Style: "+style)

# to_yaml = pss(
#     dict(
#         Mob=dict(
#             Type=self.ui.npc_type.currentText,
#             Display='{self.ui.display_2.text}',
#             Health=self.ui.health_2.value,
#             Damage=self.ui.damage_2.value,
#             Faction=self.ui.faction_2.currentText,
#             Mount=self.ui.mount_2.currentText,
#             Equipment=dict([
#                 "self.ui.mount_2.currentText() HEAD",
#                 "self.ui.chestplate.currentText() CHEST",
#                 "self.ui.leggings.currentText() LEGS",
#                 "self.ui.boots.currentText() FEET",
#                 "self.ui.hand.currentText() HAND",
#                 "self.ui.offhand.currentText() OFFHAND",
#             ]),
#             BossBar=dict(
#                 Enabled=self.enable,
#                 Title='title',
#                 Range=range,
#                 Color=color,
#                 Style=style
#             )
#         )
#     )
# )
