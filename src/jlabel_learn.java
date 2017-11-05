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
  drawfish(g);
 }
 
 public void drawBackground(Graphics g){
  try {
   BufferedImage img = ImageIO.read(new File("Pictures//underwater.jpeg"));
   g.drawImage(img, 0, 0, this.getWidth(), this.getHeight(), null);
  } catch(Exception e) {

  }
 }
 
 public void drawfish(Graphics g){
  try {
   BufferedImage img = ImageIO.read(new File("Pictures//Fish1.gif"));
   g.drawImage(img, Test.fishy.minX, Test.fishy.minY, 50, 25, null);
  } catch(Exception e) {

  }
 }

}
