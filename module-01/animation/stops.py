"""Pause points for the slide player.

Each scene calls mark(self) whenever a new caption starts, and write(self, name) at the end
of construct(). That writes <name>_stops.js next to this file: the times (seconds) where the
slide player pauses and asks "Got it, next?". The first caption (t = 0) is not a stop.
The times come from the render itself, so they stay right after any edit and re-render.
"""
import json
import os


def mark(scene):
    scene.__dict__.setdefault("_stops", []).append(round(scene.renderer.time, 3))


def write(scene, name):
    stops = sorted(set(t for t in scene.__dict__.get("_stops", []) if t > 0.01))
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{name}_stops.js")
    with open(path, "w") as f:
        f.write("window.VIDEO_STOPS = window.VIDEO_STOPS || {};\n")
        f.write(f'window.VIDEO_STOPS["{name}"] = {json.dumps(stops)};\n')
