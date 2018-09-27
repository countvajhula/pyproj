from something import Keyboard, Mouse


PERIPHERALS = (
    Keyboard,
    Mouse,
)


def use_peripheral(peripheral):
    print("Using {}!".format(peripheral))

def use_things():
    for p in PERIPHERALS:
        use_peripheral(p)
