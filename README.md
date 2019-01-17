# resume-maker-web
webpage/api to resume-maker



# Desenvolvimento: front-end

No diretório `/static` existem os arquivos que compõem o *client* da aplicação, bem como os testes dos módulos. Para iniciar o desenvolvimento é necessário ter o [Node][1] instalado e, pode-se utilizar o próprio `npm` para gerenciar as dependências do projeto ou (preferivelmente) utilizar o [Yarn][2]. Na raiz do projeto, execute o comando para instalar as dependências:

```sh
yarn install
```

Uma vez preparado o ambiente, os scripts disponíveis são:

### Desenvolvimento

Irá compilar e servir os arquivos da aplicação em `http://localhost:1234` com [*hot-module-replacement*][3] ativado:

```sh
yarn dev
```

### Build

Irá compilar os arquivos para produção, aplicando minificação e [*tree shaking*][4]. Ao final, será criado um diretório `/dist` com os arquivos que serão renderizados e consumidos pelo servidor.

```sh
yarn build
```

### Testes

Irá executar os testes existentes em `/static/tests`.

```sh
yarn test
```


[1]:https://nodejs.org/
[2]:https://yarnpkg.com/
[3]:https://parceljs.org/hmr.html
[4]:https://medium.com/@devongovett/parcel-v1-9-0-tree-shaking-2x-faster-watcher-and-more-87f2e1a70f79