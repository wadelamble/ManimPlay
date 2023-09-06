from manim import *
import random

class AnimatedVectors(ThreeDScene):
    def construct(self):
        # Set the camera orientation to view all three axes clearly
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # Create 3D axes
        axes = ThreeDAxes()

        # Define three vectors with distinct directions and colors
        vector_length = 2

        # Vector 1: 30 degrees from the Z-axis, red color
        vector1_end_point = [
            vector_length * np.cos(PI/6) * np.cos(0), 
            vector_length * np.cos(PI/6) * np.sin(0), 
            vector_length * np.sin(PI/6)
        ]
        vector1 = Arrow3D(start=[0, 0, 0], end=vector1_end_point, color=RED)

        # Vector 2: 45 degrees from the Z-axis, blue color
        vector2_end_point = [
            vector_length * np.cos(PI/4) * np.cos(PI/4), 
            vector_length * np.cos(PI/4) * np.sin(PI/4), 
            vector_length * np.sin(PI/4)
        ]
        vector2 = Arrow3D(start=[0, 0, 0], end=vector2_end_point, color=BLUE)

        # Vector 3: 60 degrees from the Z-axis, green color
        vector3_end_point = [
            vector_length * np.cos(PI/3) * np.cos(PI/2), 
            vector_length * np.cos(PI/3) * np.sin(PI/2), 
            vector_length * np.sin(PI/3)
        ]
        vector3 = Arrow3D(start=[0, 0, 0], end=vector3_end_point, color=GREEN)

        # Add the axes and vectors to the scene
        self.add(axes, vector1, vector2, vector3)

       # Add the word "vector" centered near the bottom in the fixed frame
        vector_label = Text("vector").scale(0.5).move_to(DOWN * 2.5)
        self.add_fixed_in_frame_mobjects(vector_label)  # Ensure the text is in the fixed frame


        # Label the axes
        x_label = Text("X").scale(0.5).next_to(axes.x_axis, RIGHT)
        y_label = Text("Y").scale(0.5).next_to(axes.y_axis, UP)
        z_label = Text("Z").scale(0.5).next_to(axes.z_axis, UP)
        self.add(x_label, y_label, z_label)


        # Random scaling and direction change for each vector
        def randomize_vector(vector_end_point):
            # Random scaling
            scale_factor = random.uniform(0.8, 1.2)
            scaled_vector = [coord * scale_factor for coord in vector_end_point]

            # Random direction change
            direction_change = [random.uniform(-1, 1) for _ in range(3)]
            new_end_point = [coord + change for coord, change in zip(scaled_vector, direction_change)]
            return new_end_point

        vector1_target = randomize_vector(vector1_end_point)
        vector2_target = randomize_vector(vector2_end_point)
        vector3_target = randomize_vector(vector3_end_point)
        # ... [rest of the code remains unchanged]

  # ... [rest of the code remains unchanged]

        self.play(
            vector1.animate.put_start_and_end_on([0, 0, 0], vector1_target),
            vector2.animate.put_start_and_end_on([0, 0, 0], vector2_target),
            vector3.animate.put_start_and_end_on([0, 0, 0], vector3_target),
            run_time=5  # 3 times the default run_time of 3 seconds
        )
        self.wait(2)

