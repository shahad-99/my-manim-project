from manim import *

class CodeAnimation(Scene):
    def construct(self):
        # Define your code snippets as strings
        code_snippets = [
            # Example:
            "import numpy as np",
            "import matplotlib.pyplot as plt",
            "",
            "def my_function(x):",
            "  return x**2",
            "",
            "x = np.linspace(-5, 5, 100)",
            "y = my_function(x)",
            "",
            "plt.plot(x, y)",
            "plt.xlabel('x')",
            "plt.ylabel('y')",
            "plt.title('My Function')",
            "plt.show()"
        ]

        # Create a code object with the first line
        code = Code(code_snippets[0], language="python", font_size=24)
        self.play(FadeIn(code))

        # Animate the typing of the remaining lines
        for snippet in code_snippets[1:]:
            # Create a new line object for the current snippet
            new_line = Code(snippet, language="python", font_size=24)

            # Move the cursor to the end of the existing code
            self.play(code.move_to, code.get_center() + RIGHT * 0.1)

            # Play the typing animation
            self.play(Create(new_line), run_time=1.5)

            # Append the new line to the existing code
            code.add(new_line)

        # Wait for a few seconds before ending the animation
        self.wait(3)
