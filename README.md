# Rectangle Tool ▭

This is a simple Python "sidecar" application that calculates the geometric properties of a rectangle. It's designed to be called by a parent process (like our Tauri app) and communicates over standard input/output using JSON.

## How It Works

1.  The script enters an infinite loop, waiting for input.
2.  It reads a single line from `stdin`.
3.  It parses the line as a JSON object (e.g., `{"payload": {"width": 100, "height": 50}, "metadata": {"center": {"x": 150, "y": 150}}}`).
4.  It uses the `calculator` module to compute the rectangle's area and perimeter.
5.  It formats the result as a JSON object.
6.  It prints the resulting JSON string to `stdout`, followed by a newline, to signal completion.
