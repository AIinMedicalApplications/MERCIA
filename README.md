# MERCIA
Tool for the manual mesh extraction of intracranial aneurysms (MERCIA) by using MeVisLab.
Please cite our paper (see bottom)

### Usage
* Install MeViaLab from [www.mevislab.de/download](https://www.mevislab.de/de/download)
* Copy MERCIA files into folder, double click on START_MERCIAv4_LOCAL.mlab to open the MeVisLab network:
 ![grafik](https://github.com/user-attachments/assets/508415f7-b070-47c7-99c9-9df8cc56c191)

* Now double click on the orange module to start MERCIA

#### Load Data
* The first screen allows for loading the data, you can either load a single image (i.e. a single *.dcm file) or a stack of images (i.e. a folder with the single slices)
* You can also account for t-z-dimension switches, in case the directory input produces a dataset with z-dimension = 1 and e.g. 512 time points
* Once you are satisfied, click on "Exctract Initial Mesh"

#### Extract Initial Mesh
* Please carefully adapt the windowing parameters by clicking and holding the right mouse button
  * up and down -> change center of windowing
  * left and right -> change width of windowing
  * ctrl + moving of pressed mouse wheel -> zoom in and out
  * shift + moving pressed mouse wheel -> pan / translate
  * include small vessels but avoid surrounding tissue (see example): ![grafik](https://github.com/user-attachments/assets/53fad388-8808-4fa2-a07f-1e72d82ae8a2)
 
  * once you are satisfied, set parameter for width to 0.05 or smaller in order to produce a binary segmentation: ![grafik](https://github.com/user-attachments/assets/1227bc25-0acf-4e04-bb4a-e37483e54b91)
  * select "build initial mesh" (mesh extraction take a few seconds)
 
#### Check Result
* sometimes the view is not centered, fix it by pressing "View All" (1): ![grafik](https://github.com/user-attachments/assets/31c01ec0-70f7-46bd-9a53-a8cfe64ba45b)
* You can remove smaller, unconnected parts of the mesh, a "+" and a "-" indicates whether the parts are contained or not: ![grafik](https://github.com/user-attachments/assets/b1be3678-c398-4663-843a-d3c66ad887f6)
* You can save the mesh as *.obj file now

#### Cut Mesh
* You can also edit your mesh by using some of MeVisLab's functionalities again -> Press "Cut Mesh" Button
* Navigation is the same: ctrl + moving pressed mouse wheel -> zoom in and out; shift + moving pressed mouse wheel -> pan/translate; ESC -> change between object and select mode
* If you don't see your model press the "View All" button ![grafik](https://github.com/user-attachments/assets/57942b5d-29df-4693-b3d7-ae6210a6b0cb)

![grafik](https://github.com/user-attachments/assets/8a83c8be-6888-4cc8-94e8-189d88967d50)

![grafik](https://github.com/user-attachments/assets/cb276f91-b279-4fc1-8708-66fc392f16f4)

* Save the resulting mesh: ![grafik](https://github.com/user-attachments/assets/b7e07449-18c1-45a1-afa1-703717aeb593)


## Reference
If you can use MERCIA for mesh extraction and if you create a publication, please cite our [paper](https://link.springer.com/article/10.1007/s11548-018-1848-x):
* Saalfeld, S., Berg, P., Niemann, A. et al. Semiautomatic neck curve reconstruction for intracranial aneurysm rupture risk assessment based on morphological parameters. Int J CARS 13, 1781–1793 (2018). https://doi.org/10.1007/s11548-018-1848-x
* @article{saalfeld2018semiautomatic,
  title={Semiautomatic neck curve reconstruction for intracranial aneurysm rupture risk assessment based on morphological parameters},
  author={Saalfeld, Sylvia and Berg, Philipp and Niemann, Annika and Luz, Maria and Preim, Bernhard and Beuing, Oliver},
  journal={International journal of computer assisted radiology and surgery},
  volume={13},
  pages={1781--1793},
  year={2018},
  number={13},
  doi={https://doi.org/10.1007/s11548-018-1848-x}
}








  

