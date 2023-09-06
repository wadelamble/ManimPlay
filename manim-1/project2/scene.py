from manim import *

class RotatingDNA(ThreeDScene):
    def construct(self):
        # Set the camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Parameters for the DNA strand
        turns = 5
        distance = 3
        radius = 1
        angle = 2 * PI / turns

        # Create the DNA strands using ParametricFunction
        dna1 = ParametricFunction(
            lambda t: np.array([
                radius * np.cos(t * angle),
                radius * np.sin(t * angle),
                distance * t / turns
            ]),
            color=BLUE
        ).set_t_min(0).set_t_max(turns)

        dna2 = ParametricFunction(
            lambda t: np.array([
                radius * np.cos(t * angle + PI),
                radius * np.sin(t * angle + PI),
                distance * t / turns
            ]),
            color=RED
        ).set_t_min(0).set_t_max(turns)

        # Create the base pairs connecting the strands
        base_pairs = VGroup()
        for t in np.linspace(0, turns, turns * 10):
            start = np.array([
                radius * np.cos(t * angle),
                radius * np.sin(t * angle),
                distance * t / turns
            ])
            end = np.array([
                radius * np.cos(t * angle + PI),
                radius * np.sin(t * angle + PI),
                distance * t / turns
            ])
            base_pair = Line(start, end, color=YELLOW)
            base_pairs.add(base_pair)

        # Add the DNA strands and base pairs to the scene
        self.add(dna1, dna2, base_pairs)

        # Rotate the DNA strand
        self.play(Rotating(dna1, radians=2*PI, axis=[0, 0, 1], about_point=[0, 0, 0]),
                  Rotating(dna2, radians=2*PI, axis=[0, 0, 1], about_point=[0, 0, 0]),
                  Rotating(base_pairs, radians=2*PI, axis=[0, 0, 1], about_point=[0, 0, 0]),
                  run_time=5)
        self.wait(2)
