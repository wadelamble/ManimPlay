from manim import *
import numpy as np
import random

class VectorScene(Scene):
    def construct(self):
        # Create a 2D grid
        grid = NumberPlane()
        self.add(grid)

        # Define the first vector with a magnitude of 4 and rotated 45 degrees counterclockwise
        vec1_direction = np.array([4 * np.cos(PI/4), 4 * np.sin(PI/4), 0])
        vec1 = Arrow(ORIGIN, vec1_direction, buff=0)

        # Define the rotation matrix for 150 degrees
        rotation_matrix_150 = np.array([
            [np.cos(PI * 150/180), -np.sin(PI * 150/180)],
            [np.sin(PI * 150/180), np.cos(PI * 150/180)]
        ])

        # Rotate the direction of the first vector using the rotation matrix to get the direction of the second vector
        vec2_direction = np.matmul(rotation_matrix_150, vec1_direction[:2])  # Only take the x and y components
        vec2 = Arrow(ORIGIN, np.append(vec2_direction, 0), buff=0)  # Append a 0 for the z-component

        # Add the main vectors to the scene
        self.add(vec1, vec2)

        # Define colors for the supplementary vectors
        colors = [RED, GREEN, BLUE]

        # Function to generate a random rotation matrix within a specified range (e.g., +/- 5 degrees)
        def random_rotation_matrix():
            random_angle = random.uniform(-PI * 5/180, PI * 5/180)  # Random angle between -5 and 5 degrees
            return np.array([
                [np.cos(random_angle), -np.sin(random_angle)],
                [np.sin(random_angle), np.cos(random_angle)]
            ])

        # Add random supplementary vectors for vec1
        for color in colors:
            supplementary_direction = np.matmul(random_rotation_matrix(), vec1_direction[:2])
            supplementary_vector = Arrow(ORIGIN, np.append(supplementary_direction, 0), color=color, buff=0, stroke_opacity=0.5)
            self.add(supplementary_vector)

        # Add random supplementary vectors for vec2
        for color in colors:
            supplementary_direction = np.matmul(random_rotation_matrix(), vec2_direction[:2])
            supplementary_vector = Arrow(ORIGIN, np.append(supplementary_direction, 0), color=color, buff=0, stroke_opacity=0.5)
            self.add(supplementary_vector)

        self.wait(5)
