# ED-PIP-s-Manager
"Smart" (intelligent) PIP-manager. (AHK script)
Hello, friends! In connection with the New Year, I want to make a gift. Namely, a macro for PIP.
So, my script:
1. In normal mode it is no different from many similar ones.
Switching the key [F1] changes your PIP's from 420 to 240 and back again.
The 240 mode is very useful when cruising.
The 420 mode may be needed when manually boarding planets or ports.
;==================================================

sewmode := ["240", "420"]	;sewmode[1] := 240 For max speed

				;sewmode[2] := 420 For max shields
				
It's different when you're in combat mode. For this mode, I set the [NumLock] button.

2. In [NumLock] mode, you get new features: switching PIP's to WEP for a short time when firing.
For [Combat mode: oN] you must select the most realistic PIP's and recharge time parameters.

;==================================================

; The [SYS-ENG-WEP] value when fired.

wep1 := ["024", "204"]	; [SEW] value for prim.group in the sewmode[1], sewmode[2].

wep2 := ["024", "204"]	; [SEW] value for sec.group in the sewmode[1], sewmode[2].

;==================================================

; Charging time [WEP] after a shot (msec).

time1 := [2500, 2500] ; for prim.group in the sewmode[1], sewmode[2].

time2 := [2000, 2000] ; for sec.group in the sewmode[1], sewmode[2].

;===================================================

It all depends on the power of your guns and the capability of the Power Distr.

It might be enough to set 402 or 303 with a recharge time of 800ms. Everything is determined experimentally! Try it!

3. For a change, I used two weapons.

Prim.group - deferred shot weapon: RailGun ... etc. 	 [LButtMouse]

Sec.group - instant weapons: Plasm (PA), Laser's ... etc.	[RButtMouse]

Notice the different behavior of the script in these different conditions!

4. Mode [Fa off/on]         :[Space] key.
 
In [Combat mode: oN] switches to Fa-off control mode and back to Fa-on.

Let me make a little clarification. Here I am using these control settings:

In the ED control settings, the main mode selected is [Mouse fa-off].

This means that the "relative mouse is oN". But then you won't be able to maneuver the cruise properly!

In the ED control settings, I use "alternate control". Key [F6].

Here I use a great script for VJoy by Andrea Spada. https://www.reddit.com/r/EliteDangerous/comments/d3xu04/relative_mouse_mod_guide/

The keys I used:

LeftMouseBut - Prim.Fire

RightMouseBut - Sec.Fire

Key "T" - Targeting

Key "Space" - FA oN-oFF

Key "F1" - Switching 420-240

Key "F6" - switching of alternative control

Key "NumLock" - switch Combat mode oN-oFF


Good luck! 
