
import time
import view
import controller
import model

while True:
    time.sleep(1/100)
    controller.events()
    model.update()
    view.weiv()