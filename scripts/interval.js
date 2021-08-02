class Interval { 

  constructor(min,max, minInclusive, maxInclusive){
    this.min = min; 
    this.max = max;
    this.minInclusive = minInclusive;
    this.maxInclusive = maxInclusive;
  } 
  
  isIn(xVal){
    if((this.min < xVal && xVal < this.max) || this.min == xVal && this.minInclusive || this.max == xVal && this.maxInclusive){
      return true;
       }
    else{
      return false; 
    }
  }

}