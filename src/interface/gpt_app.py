import rhinoinside
from flask import Flask, request, jsonify, send_file, render_template, redirect, url_for
import os
import sys

# Load Rhino.Inside to run Rhino in the Python environment
rhinoinside.load()
import Rhino

# Initialize Flask app
app = Flask(__name__)

# Route for generating parameterized model
@app.route('/generate', methods=['POST'])

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('gpt_index.html')  # This renders 'index.html' from the 'templates' folder


def generate_model():
    # Get parameters from the request (default values if not provided)
    data = request.json
    height = data.get('height', 10)  # Default height = 10
    width = data.get('width', 10)    # Default width = 10
    depth = data.get('depth', 10)    # Default depth = 10

    # Create a Rhino document in memory using Rhino.Inside
    Rhino.RhinoApp.Wait()

    print(Rhino.RhinoDoc.ActiveDoc, file=sys.stderr)

    # Use Rhino.Inside to create a new Rhino document
    doc = Rhino.RhinoDoc.ActiveDoc  # This accesses the active Rhino document in Rhino.Inside


    # Create a simple box based on the parameters (height, width, depth)
    corner1 = Rhino.Geometry.Point3d(0, 0, 0)
    corner2 = Rhino.Geometry.Point3d(width, depth, height)
    box = Rhino.Geometry.Box(Rhino.Geometry.Interval(0, width),
                              Rhino.Geometry.Interval(0, depth),
                              Rhino.Geometry.Interval(0, height))

    # Add the box to the Rhino document
    doc.Objects.AddBox(box)

    # Save the model (you can choose other formats such as .obj, .3dm)
    output_path = "generated_model.3dm"
    doc.SaveAs(output_path)

    # Send the generated file as a response
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
