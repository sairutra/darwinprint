# DARWINproject

## Overview

DARWINproject is an interactive 3D model designed to teach Darwin’s theory of evolution to primary school students. This project was developed in collaboration with AMS Institute to provide an engaging and educational experience using computational design techniques.

## Features

- **Dynamic 3D Evolution Model**: Generates visual representations of evolutionary changes.
- **User-Centric Design**: Developed and iteratively tested with students to ensure usability and educational effectiveness.
- **Extensible Architecture**: Simplified and documented workflow to facilitate future enhancements.

## Tech Stack

**Python, Rhino, Grasshopper, Rhino-API**

## Development Highlights

- Full software development lifecycle, from requirement gathering to implementation.
- Designed and refined an interactive 3D evolution model based on Darwin’s principles.
- Conducted iterative testing and trials to optimize student engagement and learning outcomes.
- Documented the workflow comprehensively for future research and development.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/sairutra/darwinprint.git
   ```  
   or
   Download as ZIP and unpack:
   <!-- ![Download_ZIP](img/download_zip.png) -->
   <img src="img/download_zip.png" alt="Description" width="350">
2. Open:
   Open ``open_in_rihno/darwinprint.3dm`` in Rhino 8.
   Lunch grasshopper and pen ``open_in_grasshopper/evolution_algorithm.gh``. Loading this file might take a while.

## How to use:

#### Get Rhino Controle Panel
Inside Grasshopper activate Remote Panel, if not active:
Mac: ``View > Remote Controle Panel``
Win: ``???``

Inside Rhino activate Grasshopper Container, if not active:
Mac: ``Window > Container > Grasshopper``
Win: ``???``

## Q&A:

Why is the model preview for gen 0 missing?
If model preview of Gen 0 is missing click "Reload Evolution" and "Delete Evolution".

How do I change the size of the plane grid?
Mac: ``File > Settings > Grid > Grid line count``
Win: ``???``
A value of 3000 should be sufficient.


# Administration:

## Extend to 4 Models:
- Duplicate origin plane from the green group, offset Y position by ~200
   - connect plane to the same tools using SHIFT
- Duplicate gen 0 silders from the green group
   - connect sliders to py cluster to the same tools using SHIFT
<img src="img/plane-and-sliders.png" alt="Description" width="350">
- Duplicate voting slider from green group
<img src="img/voting-slider.png" alt="Description" width="200">
- Extend "Bang!" by zooming and clicking "+" for more outputs
- Duplicate gene pool generation from green group 
   - connect new voting slider and extended "Bang!" output to new "Dup"
- Add aditional "Weaver"
   - connect "Dup" output to "Weaver" and "Weaver" output to "Panel"
<img src="img/gene-pool.png" alt="Description" width="350">
<img src="img/4-models.png" alt="Description" width="350">

## Switch the Model or Slider count:
#### prerequisite/requierments:
- Model origin needs to be based on one plane
- all variables need to be definable by "Number Sliders"
- Model output needs atleast one Preview "Brep" defenition
- create a cluster out of the model and define all "Number Sliders" as Cluster-IN and the Brep as Cluster-OUT

#### Switching
- Adjust Slider count and settings
<img src="img/Slider-count.png" alt="Description" width="300">
- extend the "PyScript" and "Graft" for the Model Preview
<img src="img/ExtractionPy-Graft.png" alt="Description" width="300">
- switch model Clusters 
   - attach correct inputs
   - link the preview output the same way as the previous model
- extened or reduce the outputs of the EvoScirpt "Py3" according to the Model and link it
<img src="img/Evo-values.png" alt="Description" width="350">

## Changing Position and Text:
Further options to change the position of the text can be found as Sliders inside the Grasshopper file:
<img src="img/text-options.png" alt="Description" width="350">


#### Disable Text:

In the "Dynamic Labes"-Group disable the preview for "TextSrf" (grouped in yellow).
 using SHIFT

## Contributing

??

## License

??

## Contact

For questions or collaboration opportunities, please reach out via [GitHub Issues](https://github.com/sairutra/darwinprint/issues).

