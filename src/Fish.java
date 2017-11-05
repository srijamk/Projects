import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.swing.*;

public class Fish {

 int minX;
 int minY;
 int maxX;
 int maxY;
 int size;
 int height;
 int width;
 int orientation;
 int health;


 public Fish(int ystart, int xstart, int newSize){
  minX=xstart;
  minY=ystart;
  orientation=1;
  health=100;
     setBorderOfBox();
     size = newSize;
 }

    public void setBorderOfBox() {
        maxX = minX + Test.fish1pic.getWidth() - (size*8);
        maxY = minY + Test.fish1pic.getHeight() - (size*8);
        width = maxX - minX;
        height = maxY - minY;
       }

       public void setSize(int newSize) {
        size = newSize;
       }
       
 public void movement(int direction){
  if (direction==1){
   minX+=5;
   orientation=1;
  }else if (direction==2){
   minX-=5;
   orientation=2;
  }else if (direction==3){
   minY-=5;
  }else if (direction==4){
   minY+=5;
  }
  if (minX<50)
   minX=50;
  if (minY<50)
   minY=50;
  if (minX>750)
   minX=750;
  if (minY>750)
   minY=750;
 }


}




