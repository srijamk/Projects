import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.swing.*;


public class Background extends JPanel{
 JFrame frame;
 
 public Background() {
  
 }

 public void paintComponent(Graphics g) {
  drawBackground(g);
  drawHealthBar(g);
  drawfish(g);
 }
 
 public void drawBackground(Graphics g){
   g.drawImage(Test.backgroundpic, 0, 0, this.getWidth(), this.getHeight(), null);
 }
 
 public void drawfish(Graphics g){
  if (Test.fishy.orientation==1)
   g.drawImage(Test.fish1pic, Test.fishy.minX, Test.fishy.minY, 50, 25, null);
  else
   g.drawImage(Test.flippedfish1pic, Test.fishy.minX, Test.fishy.minY, 50, 25, null);
 }
 
 public void drawHealthBar(Graphics g){
  g.setColor(Color.green);
  g.fillRect(0, 0, (800*Test.fishy.health/100), 25);
  g.setColor(Color.red);
  g.fillRect((800*Test.fishy.health/100), 0, 800-(800*Test.fishy.health/100), 25);
 }
}


