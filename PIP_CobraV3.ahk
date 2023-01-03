;(C) CDD_Juriy[PYRO]
#NoEnv
#UseHook On
#IfWinActive ahk_class FrontierDevelopmentsAppWinClass
;#IfWinActive ahk_class Notepad
setkeydelay, 30, 10 ; Pause, Press
#MaxThreadsperHotkey 3

WinGetPos, , , Width, Height, Program Manager
Width := Width-200
Height := Height-30
CustomColor = EEAA99
Gui, +AlwaysOnTop +LastFound +Owner -Caption
Gui, Color, %CustomColor%
Gui, Font, s9, Arial
Gui, Add, Text, cyellow, Combat mode:
Gui, Add, Text, vMyText ys cyellow, XXX
WinSet, TransColor, %CustomColor% 150
Gosub, Num
Gui, Show,  x%Width% y%Height%
SetTimer, Num, 60000

;==================================================
sewmode := ["240", "420"]
;sewmode[1] := 240 ; Default SEW=[2-4-0] For max speed
;sewmode[2] := 420 ; Alternative SEW=[4-2-0] For max shields
f1 := 1
;==================================================
; The [SYS-ENG-WEP] value when fired.
wep1 := ["024", "204"]	; The [SEW] value for prim.group in the sewmode[1], sewmode[2].
wep2 := ["024", "204"]	; The [SEW] value for sec.group in the sewmode[1], sewmode[2].
;==================================================
; Charging time [WEP] after a shot (msec).
time1 := [2500, 2500] ; for prim.group in the sewmode[1], sewmode[2].
time2 := [2000, 2000] ; for sec.group in the sewmode[1], sewmode[2].
;===================================================
; Automatic selection of [Power Plant] when capturing a target in combat mode
~T::
if Statenum = D ;Combat mode check
{
Sleep 5500
Send {y}{y}{y}{y}{y}{y}
}return

;=============Switching Mode FAon/Faoff==============
~Space::
if Statenum = D ;Combat mode check
{
Send {F6} ;Switching the [Fa-off/Alternative] mouse control
}return

;===================================================
;Switching pips by pressing [F1]
;F1 - 240/420
;===================================================
F1::
f1 := f1+1
if f1>=3
	f1:= 1
;MsgBox, % sewmode[f1]
Gosub, % sewmode[f1]
return
;==================================================
;  Here you can prescribe any PIP presets
;
;==================================================
240:
sew := "240"
Send {Down}{up}{up}{Left}{up}
return

;==================================================
330:
sew := "330"
Send {Down}{up}{up}{Left}{Left}
return

;==================================================
420:
sew := "420"
Send {Down}{Left}{Left}{up}{Left}
return

;==================================================
402:
sew := "402"
Send {Down}{Left}{Left}{Right}{Left}
return

;==================================================
042:
sew := "042"
Send {Down}{Up}{Up}{Right}{Up}
return

;==================================================
204:
sew := "204"
Send {Down}{Right}{Right}{Left}{Right}
return

;==================================================
024:
sew := "024"
Send {Down}{Right}{Right}{Up}{Right}
return

;==================================================
033:
sew := "033"
Send {Down}{Right}{Right}{Up}{Up}
return

;==================================================
303:
sew := "303"
Send {Down}{Right}{Right}{Left}{Left}
return

;==================================================
222:
sew := "222"
Send {Down}
return
;===================================================
; Switching Combat Mode - NumLock
~NumLock::
Sleep 500
Gosub, Num
return

;===================================================
; Charging the [WEP] when firing
;===================================================
~LButton:: ;RailGun
if Statenum = D
{
Sleep 900
while GetKeyState("LButton")
{
   if sew <> % wep1[f1]
   Gosub, % wep1[f1]
   Break
}
}
return

~LButton Up::
if Statenum = D
{
  Sleep % time1[f1]
  GetKeyState, rbut, RButton, P
  if rbut <> U
  return
  GetKeyState, lbut, LButton, P
  if lbut <> U
  return
;  if (%rbut%=U and %lbut%=U)
  {
     if sew = % wep1[f1]
     Gosub, % sewmode[f1]
  }
}
return

;===================================================
~RButton:: ; Plasm, Laser ...
if Statenum = D
{
  if sew <> % wep2[f1]
  Gosub, % wep2[f1]
}
return

~RButton Up::
if Statenum = D
{
Sleep time2[f1]
  GetKeyState, lbut, LButton, P
  if lbut <> U
  return
GetKeyState, rbut, RButton, P
if rbut=U
{
  if sew = % wep2[f1]
  {
   Gosub, % sewmode[f1]
   }
}
}
return
;=======================OSD==========================
Num:
GetKeyState, statenum, NumLock, T
if statenum = D
  stat = oN
if statenum = U
  stat = oFF
IfWinActive ahk_class FrontierDevelopmentsAppWinClass
GuiControl,, MyText, %stat%
return