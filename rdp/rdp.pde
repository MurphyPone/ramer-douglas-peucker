void settings() {
  size(800, 600);
}

ArrayList<PVector> allPoints = new ArrayList<PVector>();
float epsilon = 0;

void setup() { 
 for(int x = 0; x < width; x++) {
   float xval = map(x, 0, width, 0, 5);
   float yval = exp(-xval) * cos(TWO_PI * xval);
   float y = map(yval, -1, 1, height, 0);
   allPoints.add(new PVector(x, y));
 }
}

void rdp(int startIndex, int endIndex, ArrayList<PVector> allPoints, ArrayList<PVector> rdpPoints) {
 int nextIndex = findFurthest(allPoints, startIndex, endIndex);
 if ( nextIndex > 0) {
   if(startIndex != nextIndex) {
     rdp(startIndex, nextIndex, allPoints, rdpPoints);
   }
   rdpPoints.add(allPoints.get(nextIndex));
   if(nextIndex != endIndex) {
     rdp(nextIndex, endIndex, allPoints, rdpPoints);
   }
 }
}

// Find the distance from point c to the line formed by a,b
float distFromLine(PVector c, PVector a, PVector b) {
  PVector normalPoint = scalarProj(c, a, b);
  return PVector.dist(c, normalPoint);
}

PVector scalarProj(PVector p, PVector a, PVector b) {
  PVector ap = PVector.sub(p, a);
  PVector ab = PVector.sub(b, a);
  ab.normalize(); // normalize the line
  ab.mult(ap.dot(ab));
  PVector normalPoint = PVector.add(a, ab);
  return normalPoint;
}


// finds the index of the furthest element in points between indices a, b
int findFurthest(ArrayList<PVector> points, int a, int b) {
  float recordDistance = -1;
  PVector start = points.get(a);
  PVector end = points.get(b);
  int furthest = -1;
  
  for(int i = a+1; i < b; i++) {
    PVector curr = points.get(i);
    float d = distFromLine(curr, start, end); 
    if(d > recordDistance) {
      recordDistance = d;
      furthest = i;
    }
  }
  
  if (recordDistance > epsilon) {
    return furthest;
  } else {
     return -1;
   }
  
}

void draw() {
  background(0);
  
  ArrayList<PVector> rdpPoints = new ArrayList<PVector>();
  
  int total = allPoints.size();
  PVector start = allPoints.get(0);
  PVector end = allPoints.get(total-1);
  rdpPoints.add(start);
  rdp(0, total-1, allPoints, rdpPoints);
  rdpPoints.add(end);
  
  epsilon += 0.1;
  if(epsilon > 100) {
    epsilon = 0;
  }
  
  // draw target line
  stroke(255);
  strokeWeight(4);
  noFill();
  beginShape();
  for(PVector v : allPoints) {
    vertex(v.x, v.y);
  }
  endShape();
  
  // Draw rdp approx
  stroke(255, 0, 255);
  strokeWeight(2);
  beginShape();
  for(PVector v : rdpPoints) {
    vertex(v.x, v.y);
  }
  endShape();
  
  // draw info
  fill(255);
  textSize(24);
  text("epsilon: " + nf(epsilon,2,2), 20, 20);
  text("n: " + rdpPoints.size(), 20, 40);
}
