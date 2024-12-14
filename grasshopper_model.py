import rhinoinside
import os

# Load Rhino.Inside
rhinoinside.load()
import Rhino


import clr

# Try loading Grasshopper from the clr module
clr.AddReference('Grasshopper')
import Grasshopper
print("Grasshopper Loaded Successfully!")

# Create a new Rhino document in memory
doc = Rhino.RhinoDoc.CreateHeadless(None)

# Define the path to your Grasshopper definition
gh_definition_path = "template\flowerpot_design.gh"

# Load the Grasshopper definition
gh = grasshopper.Kernel.GH_Document()
gh_file = open(gh_definition_path, 'rb')
gh.ReadFromFile(gh_file)
gh_file.close()

# Set parameters (if any) using the Grasshopper API
# For example, setting a slider value or input parameter
segments = gh.FindParameter('Segments')
segments.SetData(10)  # Set the value of the parameter to 10 (example)
angle = gh.FindParameter('angle')
angle.SetData(2)  # Set the value of the parameter to 2 (example)
twist_angle = gh.FindParameter('twist angle')
twist_angle.SetData(29)  # Set the value of the parameter to 2 (example)



# Run the Grasshopper definition
gh.NewSolution(False)

# Find the geometry you want to bake
# For this example, assume the geometry is output from a parameter called 'Geometry'
output_geometry_param = gh.FindParameter('final_geometry')  # Replace with actual output parameter name
if output_geometry_param:
    geometry = output_geometry_param.GetData()

# Bake the geometry into the Rhino document (this will add the geometry to Rhino)
if geometry:
    # Check if the geometry is a list (common in Grasshopper outputs)
    if isinstance(geometry, list):
        for item in geometry:
            if isinstance(item, Rhino.Geometry.GeometryBase):
                doc.Objects.Add(item)  # Add each geometry to the document
    elif isinstance(geometry, Rhino.Geometry.GeometryBase):
        doc.Objects.Add(geometry)  # Add the geometry to the document

# Save the model as a .3dm file
output_path = os.path.join(os.getcwd(), "generated_model.3dm")
doc.SaveAs(output_path)

print(f"Model saved as {output_path}")
