import time
import buttons

print("MP3 Player")
print("Button test started.")

while True:
  if buttons.play_pressed():
    print("Play/Pause")
    time.sleep_ms(200)
  if buttons.next_pressed():
    print("Next")
    time.sleep_ms(200)
  if buttons.prev_pressed():
    print("Previous")
    time.sleep_ms(200)
  if buttons.menu_pressed():
    print("Menu")
    time.sleep_ms(200)
  if buttons.power_pressed():
    print("Power")
    time.sleep_ms(200)

  time.sleep(0.1)

  


