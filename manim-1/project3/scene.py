from manim import *
import numpy as np
import random

class VectorScene(ThreeDScene):
    def construct(self):
        # Set the camera orientation to view all three axes clearly
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

        # Create 3D axes
        axes = ThreeDAxes()

        # Define the vector length to be 75% of the grid size (assuming unit grid)
        vector_length = 0.75

        # Define three vectors with distinct directions for maximum separation
        vector_angles = [PI/6, 5*PI/12, PI/3]

        vectors_end_points = [
            [
                vector_length * np.cos(angle) * np.cos(index * 2 * PI / 3),
                vector_length * np.cos(angle) * np.sin(index * 2 * PI / 3),
                vector_length * np.sin(angle)
            ]
            for index, angle in enumerate(vector_angles)
        ]

        main_vectors = [
            Arrow3D(start=[0, 0, 0], end=end_point, color=BLUE).scale(1.5)  # Bold and large font
            for end_point in vectors_end_points
        ]

        # Add the main vectors to the scene
        self.add(axes, *main_vectors)

        # For each main vector, add 3 additional vectors near it
        for end_point in vectors_end_points:
            for i in range(3):
                offset = 0.1 * (i + 1)
                additional_vector = Arrow3D(
                    start=[0, 0, 0],
                    end=[end_point[0] + offset, end_point[1] + offset, end_point[2] + offset],
                    color=GREEN
                )
                self.add(additional_vector)

        # Add the word "vector" centered near the bottom in the fixed frame
        vector_label = Text("vector").scale(0.5).move_to(DOWN * 2.5)
        self.add_fixed_in_frame_mobjects(vector_label)  # Ensure the text is in the fixed frame

        # Label the axes
        x_label = Text("X").scale(0.5).next_to(axes.x_axis, RIGHT)
        y_label = Text("Y").scale(0.5).next_to(axes.y_axis, UP)
        z_label = Text("Z").scale(0.5).next_to(axes.z_axis, UP)
        self.add(x_label, y_label, z_label)

        # ... [rest of the code remains unchanged]
