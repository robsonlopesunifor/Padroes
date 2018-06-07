
// classes e interface

class NomeDaClasse{

  public atributoNumerico: number
  private atributoString: string // tambem vai no parametro


  constructor (atributoString: string){}
  // outra for é
  // constructor (public propusor: string){}

  metodo(){
    console.log(`Imprimir texto ${this.atributoString}`)
  }

}
