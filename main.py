import glfw
from OpenGL.GL import *
import numpy as np



# Define the vertices of the triangle
vertices = np.array([
    -0.5, -0.5, 0.0,  
    0.5, -0.5, 0.0,   
    0.0, 0.5, 0.0     
], dtype=np.float32)

# Define the colors of the vertices
colors = np.array([
    1.0, 0.0, 0.0,  # Red
    0.0, 1.0, 0.0,  # Green
    0.0, 0.0, 1.0   # Blue
], dtype=np.float32)

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # GLFW window hints
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)


    window = glfw.create_window(800, 600, "PyGLFW Window", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)


    glfw.swap_interval(1)

    glViewport(0, 0, 800, 600)



    # Vertex Array Object (VAO) and Vertex Buffer Object (VBO)
    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    # Bind VAO
    glBindVertexArray(vao)

    # Bind VBO and set vertex data
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes + colors.nbytes, None, GL_STATIC_DRAW)
    glBufferSubData(GL_ARRAY_BUFFER, 0, vertices.nbytes, vertices)
    glBufferSubData(GL_ARRAY_BUFFER, vertices.nbytes, colors.nbytes, colors)


    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # VAO and VBO
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glBindVertexArray(vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glBindVertexArray(0)

        glfw.swap_buffers(window)

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
