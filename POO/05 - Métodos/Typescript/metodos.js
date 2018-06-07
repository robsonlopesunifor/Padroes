//------------------------ padrao ------------------------------
function nomeDaFuncao2(parametro: number, parametro2: number = 1): number{
      return parametro + parametro2;
}

nomeDaFuncao2(1)
//------------------------ mais usada -----------------------------
let nomeDaFuncao = function(parametro: number) : boolean {
      let maior = parametro < 12
      //nao e aspas simple ( '' ), e crase ( `` )
      console.log(` ${valor} e maior que 12 ? ${maior}`);
}

nomeDaFuncao(valor)
//------------------------- resumida ---------------------------------
let call = (parametro: string) => console.log(`${parametro}`)

call('valor do parametro');
