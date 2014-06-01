IM Presence indication system using RGB LEDs - http://hackaday.io/project/1014-IM-Status-Indicator-Nameplates

I share a bullpen-style office with 3 other people, and while I love the set up, I found people would walk down our hallway only to find one of us away from our desks. In a (noble and selfless) effort to save everyone up to 8 seconds per day, I decided to visually indicate our presence using our IM status (Green = Available, Yellow = Away, Red = Busy). We have a nice side window by our door and transparent name plates, so the lights are very visible.

The hardware is simple - A Raspberry Pi, 4 RGB LEDs, some leftover perfboard, and a ribbon cable. What was intended to be a rough prototype has remained in place since its installation, further supporting my mantra: Nothing is truly temporary.

The PoC used finch driven by Python over DBus. It was more baling wire than cement, but people wanted to see it, so here it is. Many more details are available at the HackADay project page.
