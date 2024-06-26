from functools import cache

from base.constant import BINARY_SCALE, BASE_CRITICAL_POWER


@cache
def defense_result(shield_base, shield_gain, shield_ignore, shield_constant):
    shield = shield_base
    shield += int(shield * shield_gain / BINARY_SCALE)
    shield -= int(shield * shield_ignore / BINARY_SCALE)
    shield = max(0, shield)
    return int(shield * BINARY_SCALE / (shield + shield_constant))


@cache
def base_result(damage_base, damage_rand):
    damage = int(damage_base) + damage_rand / 2
    return int(damage)


@cache
def attack_power_result(attack_power_cof, attack_power):
    damage = attack_power * attack_power_cof
    return int(damage)


@cache
def weapon_damage_result(weapon_damage_cof, weapon_damage):
    damage = weapon_damage * weapon_damage_cof
    return int(damage)


@cache
def surplus_result(surplus_cof, surplus):
    damage = surplus * surplus_cof
    return int(damage)


@cache
def init_result(damage_base, damage_rand,
                attack_power_cof, attack_power,
                weapon_damage_cof, weapon_damage,
                surplus_cof, surplus):
    return (base_result(damage_base, damage_rand) +
            attack_power_result(attack_power_cof, attack_power) +
            weapon_damage_result(weapon_damage_cof, weapon_damage) +
            surplus_result(surplus_cof, surplus))


@cache
def damage_addition_result(damage, damage_addition):
    return int(damage * (1 + damage_addition / BINARY_SCALE))


@cache
def overcome_result(damage, overcome, shield_base, shield_gain, shield_ignore, shield_constant):
    overcome = int(overcome * BINARY_SCALE)
    defense = defense_result(shield_base, shield_gain, shield_ignore, shield_constant)
    rate = (BINARY_SCALE + overcome) - int((BINARY_SCALE + overcome) * defense / BINARY_SCALE)
    return int(damage * rate / BINARY_SCALE)


@cache
def critical_result(damage, base_critical_power, critical_power_gain):
    critical_power = int(base_critical_power * BINARY_SCALE)
    critical_power += critical_power_gain
    rate = critical_power / BINARY_SCALE
    return int(damage * BASE_CRITICAL_POWER) + int(damage * rate)


@cache
def level_reduction_result(damage, level_reduction):
    return int(damage * (1 - level_reduction))


@cache
def strain_result(damage, base_strain, strain_gain):
    strain = int(base_strain * BINARY_SCALE) + strain_gain
    return int(damage * (1 + strain / BINARY_SCALE))


@cache
def pve_addition_result(damage, pve_addition):
    return int(damage * (1 + pve_addition / BINARY_SCALE))


@cache
def vulnerable_result(damage, vulnerable):
    return int(damage * (1 + vulnerable / BINARY_SCALE))
