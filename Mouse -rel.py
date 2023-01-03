from System import Int16

#############################################################################################################################
# User adjustable parameters                                                                                                #
#############################################################################################################################
                                                                                                                            #
controller = vJoy[0]                             # the reference to the installed vJoy device
absolute_sens = 8                               # absolute mouse mode sensitivity (20)
absolute_curve = 3                               # exponential factor for the ablsolute axises curve (3)
dba = 60				                         # deadband abs (20)
dbr = 0				                         # deadband rel (100)
relative_x_sens = 0                             # relative mouse mode x sensitivity def=50
relative_y_sens = 0                             # relative mouse mode y sensitivity def=50
                                                                                                       						#
#############################################################################################################################

if starting:
    # Init
    system.setThreadTiming(TimingTypes.HighresSystemTimer)
    system.threadExecutionInterval = 5 # loop delay (5)

    max =  Int16.MaxValue*0.5+0.5 - dba/2   #  16384
    min = -Int16.MaxValue*0.5-0.5 + dba/2   # -16384
    mouse_rx = 0; mouse_ry = 0; mouse_x = 0; mouse_y = 0
    m_x_curv = 0; m_y_curv = 0; m_x_curv1 = 0; m_y_curv1 = 0

#Mouse axis definition
mouse_x += mouse.deltaX * absolute_sens          # absolute mouse, lateral
mouse_y += mouse.deltaY * absolute_sens          #                 vertical
mouse_rx += mouse.deltaX * relative_x_sens       # relative mouse, lateral
mouse_ry += mouse.deltaY * relative_y_sens       #                 vertical

# Constraining axises to max values
if (mouse_x > max): mouse_x = max
elif (mouse_x < min): mouse_x = min
if (mouse_y > max): mouse_y = max
elif (mouse_y < min): mouse_y = min

if (mouse_rx > max): mouse_rx = max
elif (mouse_rx < min): mouse_rx = min
if (mouse_ry > max): mouse_ry = max
elif (mouse_ry < min): mouse_ry = min

# DeadBand abs
if (-dba/2 < mouse_x < dba/2): m_x = 0
elif (mouse_x <= -dba/2): m_x = mouse_x + dba/2
elif (mouse_x >= dba/2): m_x = mouse_x - dba/2

if (-dba/2 < mouse_y < dba/2): m_y = 0
elif (mouse_y <= -dba/2): m_y = mouse_y + dba/2
elif (mouse_y >= dba/2): m_y = mouse_y - dba/2
	
# DeadBand rel
if (-dbr/2 < mouse_rx < dbr/2): m_rx = 0
elif (mouse_rx <= -dbr/2): m_rx = mouse_rx + dbr/2
elif (mouse_rx >= dbr/2): m_rx = mouse_rx - dbr/2

if (-dbr/2 < mouse_ry < dbr/2): m_ry = 0
elif (mouse_ry <= -dbr/2): m_ry = mouse_ry + dbr/2
elif (mouse_ry >= dbr/2): m_ry = mouse_ry - dbr/2

# Relative mouse; self centering axis routine
if filters.stopWatch(True, 200):	#Def 100
	mouse_rx = 0
	mouse_ry = 0

# Absolute mouse; lightly exponential curved axis
if (m_x > 0): m_x_curv = math.floor((math.sqrt(m_x ** absolute_curve) /2 ) / 64)
if (m_x < 0): m_x_curv = math.floor(-abs(math.sqrt(abs(m_x ** absolute_curve)) / 2 ) / 64)
if (m_y > 0): m_y_curv = math.floor((math.sqrt(m_y ** absolute_curve) /2 ) / 64)
if (m_y < 0): m_y_curv = math.floor(-abs(math.sqrt(abs(m_y ** absolute_curve)) / 2 ) / 64)

if (m_x > 0): m_x_curv1 = math.floor((m_x ** 2) / 16384)
if (m_x < 0): m_x_curv1 = math.floor(-abs((m_x ** 2) / 16384))
if (m_y > 0): m_y_curv1 = math.floor((m_y ** 2) / 16384)
if (m_y < 0): m_y_curv1 = math.floor(-abs((m_y ** 2) / 16384))

# Writing absolute output to controller
#controller.x = m_x_curv1; controller.y = m_y_curv1
#controller.x = m_x_curv; controller.y = m_y_curv
#controller.x = filters.deadband(mouse_x, 25); controller.y = filters.deadband(mouse_y, 25)
#controller.x = m_x; controller.y = m_y
controller.x = m_x - m_rx; controller.y = m_y - m_ry

# Writing relative output to controller
#controller.rx = filters.deadband(mouse_rx, 30)
controller.rx = m_rx; controller.ry = m_ry
#controller.ry = filters.deadband(mouse_ry, 30)

# Hard Centering (By press an hotkey)
if keyboard.getKeyDown(Key.F6): 
	mouse_x = 0
	mouse_y = 0
	m_x_curv = 0
	m_y_curv = 0
	m_x_curv1 = 0
	m_y_curv1 = 0
	
##### Diagnostics
diagnostics.watch(controller.rx)
diagnostics.watch(controller.ry)
diagnostics.watch(controller.x)
diagnostics.watch(controller.y)
