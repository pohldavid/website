+++
title = 'Raspberry Cat Feeder'
date = 2023-12-17T04:51:52-06:00
draft = false
summary = 'The Raspberry Cat Feeder is a an automatic cat feeder powered by [Raspberry Pi](https://www.raspberrypi.com/ "raspberrypi.com"). '
+++

The Raspberry Cat Feeder is a an automatic cat feeder powered by [Raspberry Pi](https://www.raspberrypi.com/ "raspberrypi.com").  The [rcf] can be programmed to feed at prescribed intervals or on demand through a web interface.  

Design goals for the project include:
- assembled from inexpensive, commonly accessible hardware using simple hand tools available to the average DIYer.
- provide food for extended away intervals
- be reliable and low maintenance
- be rodent and vermin "*proof* "


## Mechanical

{{<img src="/uploads/2023/cat-feeder-still.png" alt="cat feeder image">}}


A short animation showing the mechanical concept can be found [here](https://youtu.be/JP9D95I43UQ).


## Circuit Diagram

A circuit diagram is shown below as well as a list of the major components used in the prototype version built.  The selection of these components was strictly based on parts available on hand at the time.

![Circuit Diagram](/uploads/2023/cat_feeder_circuit_diagram.png "Diagram")

N.B. some of these relay modules may behave differently. Caution should be exercised - transistor driver circuits and or pull up/down resistors may
be required to ensure reliable relay operation and or damage to the pi.

## Software 

### GPIO

The cat feeder code is largely written in Python and utilizes the [GPIOZero](https://gpiozero.readthedocs.io/en/stable/) library for driving the board's input/output. 

Here is an early version of the basic motor control:



```python
#! /usr/bin/python3

from time import sleep
from gpiozero import DigitalOutputDevice
from gpiozero import OutputDevice
from gpiozero import Button

import history

switch = Button(4)

relay = OutputDevice(3,active_high=True,initial_value=True,pin_factory=None)

def motor_off():
    # active low relay so reverse logic
    print("off")
    relay.on()
    history.write_event()

def motor_on():
    # active low relay so reverse logic
    print("on")
    relay.off()

def feed():
    print("feed")

    delay = 24.0
    dwell = 2
    motor_on()
    sleep(dwell) #move off limit switch
    made = switch.wait_for_press()
    print("switch")
    if made:
        motor_off()
```

### Web interface

The web interface uses the NiceGUI framework .... to be continued

{{< alert >}}
**Not Done!** Yes I know - I'll get to it!
{{< /alert >}}

{{< icon "github" >}}  [github repository](https://github.com/pohldavid/cat-feeder.git)

---

