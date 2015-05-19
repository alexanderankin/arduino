void setup() {
  Serial.begin(9600); 
}

double error;

#define al 60

void loop() {
  int iters = 60;
  
  double a = 0.0;
  double inc = 2 * PI / 60;
  
  double gooddata[al];
  double baddata[al];
  double fixeddata[al];
  for (int i = 0; i < iters; i++) {
    if (i % 5 != 0) continue;
    gooddata[i] = generate(a, i, inc);
    baddata[i] = worsen(gooddata[i]); // 5% error
    fixeddata[i] = algorithm(baddata[i]);
    Serial.print(fixeddata[i] - gooddata[i]);
    Serial.print("\n");
  }
  
  Serial.print("done");
  delay(100000);

}

double generate (double a, int i, double inc) {
  return sin(a + (i * inc));
}

double worsen(double a) {
  double m_error = (random(-1,1) * .05);
  error = m_error;
  return a + m_error;
}
double algorithm(double a) {
  return a - error;
}
