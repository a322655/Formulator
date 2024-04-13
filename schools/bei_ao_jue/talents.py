from typing import Dict

from base.attribute import Attribute
from base.gain import Gain


class 冥鼓(Gain):
    def add(self, other):
        if isinstance(other, dict):
            for skill_id in [16760, 16382, 20991]:
                other[skill_id].skill_damage_addition += 205
                other[skill_id].skill_shield_gain -= 512
            other[32823].skill_shield_gain = [0, 0, -512, -512]

    def sub(self, other):
        if isinstance(other, dict):
            for skill_id in [16760, 16382, 20991]:
                other[skill_id].skill_damage_addition -= 205
                other[skill_id].skill_shield_gain += 512
            other[32823].skill_shield_gain = 0


class 阳关(Gain):
    def add(self, other):
        if isinstance(other, dict):
            for skill_id in [16803, 16802, 16801, 16800, 17043, 19423, 19424]:
                other[skill_id].skill_damage_addition += 154
                other[skill_id].skill_shield_gain -= 205
            other[32859].skill_damage_addition += 154

    def sub(self, other):
        if isinstance(other, dict):
            for skill_id in [16803, 16802, 16801, 16800, 17043, 19423, 19424]:
                other[skill_id].skill_damage_addition -= 154
                other[skill_id].skill_shield_gain += 205
            other[32859].skill_damage_addition -= 154


class 星火(Gain):
    def add(self, other):
        if isinstance(other, Attribute):
            other.strength_gain += 102

    def sub(self, other):
        if isinstance(other, Attribute):
            other.strength_gain -= 102


class 绝河(Gain):
    def add(self, other):
        if isinstance(other, dict):
            other[20991].skill_damage_addition += 307

    def sub(self, other):
        if isinstance(other, dict):
            other[20991].skill_damage_addition -= 307


class 绝期(Gain):
    def add(self, other):
        if isinstance(other, dict):
            other[11447].attack_power_cof_gain += 0.7

    def sub(self, other):
        if isinstance(other, dict):
            other[11447].attack_power_cof_gain -= 0.7


TALENT_GAINS: Dict[int, Gain] = {
    16691: Gain("龙息"),
    16847: Gain("归酣"),
    26904: 冥鼓("冥鼔"),
    17042: 阳关("阳关"),
    16799: Gain("霜天"),
    25633: Gain("含风"),
    32857: Gain("见尘"),
    17047: Gain("分疆"),
    25258: Gain("掠关"),
    16728: 星火("星火"),
    34677: 绝河("绝河"),
    16737: Gain("楚歌"),
    17056: 绝期("绝期"),
    16893: Gain("重烟"),
    21858: Gain("降麒式")
}

TALENTS = [
    [16691],
    [16847],
    [26904, 17042],
    [16799],
    [25633],
    [32857],
    [17047],
    [25258, 16728, 34677],
    [16737],
    [17056],
    [16893],
    [21858]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}