import time

import controller2
import view
import controller
import model
import view2

while True:
    time.sleep(1 / 100)
    if model.scena == "menu":
        controller2.events()
    else:
        print(model.speedx)
        controller.events()
        model.update()
        view.weiv()
