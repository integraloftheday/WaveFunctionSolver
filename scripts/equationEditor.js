class EquationEditor {
  
  constructor(name, div,defaultNum = 1){
    this.name = name
    this.numEq = 1
    this.equationsHTML = [];
    this.div = div
    this.equations = new Equations();
    for(var i = 0; i<defaultNum; i++){
      this.addEquation();
    }
  }
  
  addEquation() {
      var baseHTML = `
                      <h5>
                      Equation ${this.numEq}
                      </h5>
                      <div class="input-group input-group-sm mb-3">
                        <div class="input-group-prepend">
                          <span class="input-group-text" id="inputGroup-sizing-sm" data-toggle="popover" title="V(x) Potential Energy Function" 
                          data-content="Enter f(x). Standard math functions can be used i.e. sqrt() and sin()">V(x) = </span>
                        </div>
                        <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" id="Eq-${this.name}-${this.numEq}">
                      </div>
                      <div class="input-group mb-3">
                        <div class="input-group-prepend">
                          <div class="input-group-text" data-toggle="popover" title="xMin" data-content="The minimum value for the function above. If checked the xMin value will be inclusive">
                            <input type="checkbox" aria-label="Checkbox for following text input" id="MinInclusive-${this.name}-${this.numEq}">
                            &nbsp;xMin
                          </div>
                        <input type="number" class="form-control" aria-label="Text input with checkbox" id ="Min-${this.name}-${this.numEq}">
                        </div>
                        
                       <div class="input-group-prepend">
                          <div class="input-group-text" data-toggle="popover" title="xMin" data-content="The minimum value for the function above. If checked the xMax value will be inclusive">
                            <input type="checkbox" aria-label="Checkbox for following text input" id="MaxInclusive-${this.name}-${this.numEq}">
                            &nbsp;xMax
                          </div>
                        <input type="number" class="form-control" aria-label="Text input with checkbox" id ="Max-${this.name}-${this.numEq}">
                        </div>
                      </div>
                         `; 
    
    this.equationsHTML.push(baseHTML);
    this.numEq = this.equationsHTML.length+1;
    this.dispHTML();
  }
  
  removeEquation(){
    this.equationsHTML.splice(-1,1);
    this.numEq = this.equationsHTML.length +1;
    this.dispHTML();
  }
  
  dispHTML(){
    var allHTML = this.equationsHTML.join(""); 
    document.getElementById(this.div).innerHTML = allHTML;
  }
  
  getHTMLData(index){
    var eqString = document.getElementById(`Eq-${this.name}-${index}`).value; 
    var xMin = document.getElementById(`Min-${this.name}-${index}`).value;
    var xMinInclusive = document.getElementById(`MinInclusive-${this.name}-${index}`).checked;
    var xMax = document.getElementById(`Max-${this.name}-${index}`).value;
    var xMaxInclusive = document.getElementById(`MaxInclusive-${this.name}-${index}`).checked;
    return([eqString,parseFloat(xMin),parseFloat(xMax),xMinInclusive,xMaxInclusive]);
  }
  
  parseEquations(){
    for(var i = 1; i<this.equationsHTML.length+1; i++){
      var data = this.getHTMLData(i);
      this.equations.addEq(new Equation(data[0],data[1],data[2],data[3]));
    }
  }
  
}