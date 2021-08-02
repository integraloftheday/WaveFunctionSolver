class Equations { 
  
  constructor(equationArray = []){
    this.equationArray = equationArray;
  }
  
  addEq(eq){
    this.equationArray.push(eq);
  }
  
  clear(){
    this.equationArray = [];
  }
  
  eval(xVal){
    var finalResult = 0;
    for (var i in this.equationArray){
      var result = this.equationArray[i].eval(xVal);
        if(result!= null){
          finalResult = result;
        }
    }
    return(finalResult);
  }
  
}