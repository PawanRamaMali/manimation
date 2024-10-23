from manim import *

class PCAVisualization(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True,
            **kwargs
        )

    def construct(self):
        # Step 1: Plot original data points
        original_points = [
            np.array([2, 1]),
            np.array([3, 2]),
            np.array([4, 1]),
            np.array([5, 3]),
            np.array([6, 2])
        ]
        dots = VGroup(*[Dot(self.plane.coords_to_point(p[0], p[1])) for p in original_points])
        self.add(dots)
        self.wait()

        # Step 2: Center the data
        centered_points = [p - np.mean(original_points, axis=0) for p in original_points]
        centered_dots = VGroup(*[Dot(self.plane.coords_to_point(p[0], p[1]), color=BLUE) for p in centered_points])
        self.play(Transform(dots, centered_dots))
        self.wait()

        # Step 3: Show direction of maximum variance (first principal component)
        principal_direction = Vector([1, 0.5], color=YELLOW).scale(2)
        self.add(principal_direction)
        self.wait()

        # Step 4: Apply PCA transformation (rotate the data to align with the principal direction)
        pca_matrix = [[0.8, 0.6], [-0.6, 0.8]]  # Example transformation matrix from eigenvectors
        self.apply_matrix(pca_matrix)
        self.wait()

        # Step 5: Project the data onto the principal component
        projected_points = [np.dot(p, pca_matrix) for p in centered_points]
        projected_dots = VGroup(*[Dot(self.plane.coords_to_point(p[0], p[1]), color=GREEN) for p in projected_points])
        self.play(Transform(centered_dots, projected_dots))
        self.wait()

        # Add labels for clarity
        label1 = MathTex(r"PC_1").next_to(principal_direction, RIGHT)
        self.add(label1)

        # Pause to show the final result
        self.wait(2)
