(function(){
    let createDiv = (i,main) => {
        let div = document.createElement('div');
        let h1 = document.createElement('h1')
                    .innerHTML = 'Etiqueta numero '+i;
        div.append(h1);
        main.append(div);
    }

    let recursion = (main,n) => {
        if (n == 0) {
            return false;
        }
        createDiv(n,main);
        return recursion(main, n-1);
    }

    recursion(document.getElementById('main'),2);
}())