import rhinoinside
import os

# Load Rhino.Inside
rhinoinside.load()
import Rhino


# Set up Rhino environment
doc = Rhino.RhinoDoc.CreateHeadless(None)

# Define the parameters
height = 20  # Example height
width = 10   # Example width
depth = 10    # Example depth (we're creating a 2D square on the XY plane)

# Create a square (rectangle) in Rhino based on the given width and height
corner1 = Rhino.Geometry.Point3d(0, 0, 0)
corner2 = Rhino.Geometry.Point3d(width, depth, height)
bounding_box = Rhino.Geometry.BoundingBox(corner1, corner2)
box = Rhino.Geometry.Box(bounding_box)

# Add the box to the document
doc.Objects.AddBox(box)

# Save the generated model as a .3dm file
output_path = os.path.join(os.getcwd(), "generated_square.3dm")
doc.SaveAs(output_path)

print(f"Model saved as {output_path}")
