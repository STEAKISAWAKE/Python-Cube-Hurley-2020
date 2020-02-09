# Copyright (C) Cube^3 

#The people who use our program could be parents or guardians trying to occupy children or perhaps by a teacher to entertain young students around Kindergarten age
#The target device would be a computer but the code could be used on virtually any modern device
#The program could also be used as a desktop background

# Sources
# https://github.com/samheather/3DVision/blob/master/old/pyglet-cube.py

import pyglet

# Creates the window with a 800 by 800 size
cubeWindow = pyglet.window.Window(width = 800, height = 800)

# Execute the on_show function when the window has an event
@cubeWindow.event
def on_show():
    # Clear the window
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT | pyglet.gl.GL_DEPTH_BUFFER_BIT)

    # Set up projection matrix.
    pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
    
    # Set the Projection matrix to 0
    pyglet.gl.glLoadIdentity()

    # Set the projection to a perspective(3d) matrix not ortho(2d)
    pyglet.gl.gluPerspective(45.0, float(cubeWindow.width)/cubeWindow.height, 0.1, 360)

# Execute the on_draw function when the window has an event to draw
@cubeWindow.event
def on_draw():

    # Make it so that the python compiler understands where the yaw, pitch and roll variables are
    global yaw
    global pitch
    global roll
    
    # The the matrix to the model view so we can draw stuff
    pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
    pyglet.gl.glLoadIdentity()
    
    # Move the world further back so we can see the cube
    pyglet.gl.glTranslatef(0, 0, -6)
     
    # Rotate the cube
    yaw += 1
    pitch += 0.5
    roll += 0.1
    
    # Rotate the cube in a euler rather than as a quaternion
    pyglet.gl.glRotatef(yaw, 1.0, 0.0, 0.0);
    pyglet.gl.glRotatef(pitch, 0.0, 1.0, 0.0);
    pyglet.gl.glRotatef(roll, 0.0, 0.0, 1.0);
    
    # Clear the window
    cubeWindow.clear()
    
    # Change the drawing color
    pyglet.gl.glColor4f(1.0,0,0,1.0)

    # Draw a cube with the specified positions of verts
    pyglet.graphics.draw_indexed(8, pyglet.gl.GL_LINES, [0, 1, 1, 2, 2, 3, 3, 0,# front square
                                                         4, 5, 5, 6, 6, 7, 7, 4,# back square
                                                         0, 4, 1, 5, 2, 6, 3, 7],# connectors
                           ('v3f', (-1, -1, 0,
                                    1, -1, 0,
                                    1, 1, 0,
                                    -1, 1, 0,
                                    -1, -1, -1,
                                    1, -1, -1,
                                    1, 1, -1,
                                    -1, 1, -1)))

# The yaw, pitch, and roll 
yaw = 0.0
pitch = 0.0
roll = 0.0

# HACK Updates the program to get the window to redraw
def update(dt):
    pass

# HACK Set the update schedule for the hack
pyglet.clock.schedule_interval(update, 1/144.0)

# This is what calls the begining of the program
pyglet.app.run()