class Equation {
  
  constructor(stringEq, min = -1,max = 1, minInclusive = false, maxInclusive = false){
      this.functionCompile = math.compile(stringEq);
      this.interval = new Interval(min,max,minInclusive,maxInclusive);
  }
  
  eval(xVal){
    if(this.interval.isIn(xVal)){
      var scope = {
        x:xVal
      }
      return this.functionCompile.evaluate(scope);
    }
    else{
      return null; 
    }
  }
}