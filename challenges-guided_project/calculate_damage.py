def calculate_damage(armor, weapon="fist"):
    if weapon == 'dagger':
        damage = 10
    elif weapon == 'sword':
        damage = 15
    elif weapon == 'fist':
        damage = 5
    else:
        damage = 0
    return damage - armor


# Don't touch below this line


def test(armor, weapon):
    dmg = 0
    if weapon is None:
        dmg = calculate_damage(armor)
        weapon = "fist"
    else:
        dmg = calculate_damage(armor, weapon)
    print(
        f"A soldier with {armor} armor was hit by a {weapon}! {dmg} damage was inflicted."
    )


test(5, "sword")
test(2, "dagger")
test(3, "dagger")
test(2, None)
test(2, "spell")
