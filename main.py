  
import pyglet


cubeWindow = pyglet.window.Window(width = 800, height = 800)

@cubeWindow.event
def on_show():
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT | pyglet.gl.GL_DEPTH_BUFFER_BIT)

    # Set up projection matrix.
    pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
    pyglet.gl.glLoadIdentity()

    pyglet.gl.gluPerspective(45.0, float(cubeWindow.width)/cubeWindow.height, 0.1, 360)

@cubeWindow.event
def on_draw():

    global yaw
    global pitch
    global roll
    # Move the camera back a little.
    # TODO(sam): When you want to start rotating the camera, this should move into on_draw,
    # and there should be a call to gRotatef.
    pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
    pyglet.gl.glLoadIdentity()
    pyglet.gl.glTranslatef(0, 0, -6)
     #seems to rotate c degrees around a point x,y,z???
    yaw += 1
   
    print ("draw")
    pyglet.gl.glRotatef(yaw, 1.0, 0.0, 0.0);
    pyglet.gl.glRotatef(pitch, 0.0, 1.0, 0.0);
    pyglet.gl.glRotatef(roll, 0.0, 0.0, 1.0);
    
    cubeWindow.clear()
  
    pyglet.gl.glColor4f(1.0,0,0,1.0)

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

yaw = 0.0
pitch = 0.0
roll = 0.0

def update(dt):
    pass

pyglet.clock.schedule_interval(update, 1/120.0)
    
pyglet.app.run()
