# scheduler

easy 24x7 js widget scheduler all with a simple flask app to load and save db, the db is a 7x(24*4) matrix with the scheduled values and a array with the scheduled values

in index.html a simple html and js control to schedule temps may be to use with arduino

examples


  scheduler1=new Sliders("sc1",[["lightgray","spento"],["#ff0000","18°"],["#00ff00","20°"],["#0000ff","22°"]],["Lunedì","Martedì","Mercoledì","Giovedi","Venderdi","Sabato","Domenica"],1);
  scheduler2=new Sliders("sc2",[["lightgray","spento"],["#ffff00","16°"],["#00ffff","17°"]],["Lun-Ven","Sab-Dom"],4);
  scheduler3=new Sliders("sc3",[["lightgray","spento"],["#ff0000","18°"],["#00ff00","20°"],["#0000ff","22°"],["#000000","24°"]],["Lun-Ven","Sab-Dom"],2);

  $("#save1").on("click",()=>scheduler1.save());
  $("#save2").on("click",()=>scheduler2.save());
  $("#save3").on("click",()=>scheduler3.save());

![image info](scheduler.JPG)
