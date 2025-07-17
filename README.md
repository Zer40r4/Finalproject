Safety-checker
My safety checker is designed to identify how safe individuals are in the hazardous construction workspace of today. tIt helps to idntify if construction workers are wearing the appropriate PPE's for the job to avoid unnecesary injuries that can be fatal. To ensure al workers are safer from struck by incidents my code ensures for the amount of class "Humans" identified in the imagethere should be more or equal to the amout of class "Hard_hats" identified. the code will output that the environment is unsaf eif the requirments are not met.

https://drive.google.com/file/d/1oSqTON-Kp22VLzZWUttScIU3_5hC_I6l/view?usp=sharing

The Algorithm
The code works by detecting thhe safety ppes present in the image which would be the classes"Hard_hats ,Ear_protector, Visor, Vest" as well as the worker - class "Humans". For the code to work it requires input.. To implement in the real world a real time video would be ideal. This code though currently only accepts images.
The code depends on how many  "Hard_hats" and "Humans" are mentioned in the image as mentioned earlier.

Running this project

  1.Install - pytorch 2.1.0, torchvision 0.16.0, numpy 2.13.0, ultralytics and roboflow
  2.The user must first run the code - Safety check that can be navigated to through:
  /home/nvidia/Finalproject/Safety-checker.py
  3.The user must declare that they would like to use image detection by entering the number "1".
  4.Afterwards the  user must navigate too the saved image.
  5.The path of the image to the construction worker saved on the orin must be copied and pasted when prompted to enter the image path.
-- The codes output will then show the annotations made and decide whether the worker is safe based on the number of "Hard_hats" and "Humans" present

Video  - https://drive.google.com/file/d/1A8efCUqFDeuJZ0mgq_GJusR36Qc1Lqce/view?usp=sharin
Document - https://docs.google.com/document/d/1XoENdbjhRbJiIEfQJdH_ypSvIksPv7wqNpN3oY4UTGs/edit?usp=sharing
