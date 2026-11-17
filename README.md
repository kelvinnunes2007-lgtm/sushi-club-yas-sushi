# sushi-club-yas-sushi
Sistema de fidelização de clientes do YAS SUSHI, desenvolvido para a disciplina de Projeto de Software ## Funcionalidades planejadas do Sushi Club

O Sushi Club é um sistema de fidelização de clientes do restaurante YAS SUSHI, desenvolvido como projeto acadêmico da disciplina de Projeto de Software.

### Cadastro de clientes
Permitirá cadastrar e identificar clientes participantes do programa de fidelidade.

### Registro de compras
Permitirá registrar compras realizadas pelos clientes para calcular a pontuação adquirida.

### Controle de pontos
A cada R$ 10,00 em compras, o cliente receberá 1 ponto. O sistema permitirá consultar o saldo de pontos acumulados.

### Resgate de recompensas
Os clientes poderão solicitar recompensas utilizando os pontos disponíveis. As solicitações ficarão sujeitas à aprovação do estabelecimento.

### Situação do projeto
MVP em desenvolvimento. As funcionalidades descritas ainda precisam ser implementadas e testadas.

## Revisão técnica do MVP

### Arquitetura e refatoração
O projeto Sushi Club possui o código principal no arquivo `sushi_club.py` e testes nos arquivos `test_sushi_club.py` e `test_recompensas.py`.

A documentação apresenta as funcionalidades de cadastro de clientes, registro de compras, pontuação e recompensas. Como melhoria de arquitetura, proponho separar essas responsabilidades em funções ou módulos e centralizar as regras de pontuação, facilitando manutenção e testes.

### Qualidade e segurança
A revisão identificou a importância da validação dos dados dos clientes, da conferência dos valores das compras e da verificação do saldo de pontos antes de autorizar recompensas.

Também foram identificadas oportunidades de melhoria na apresentação de mensagens de erro, proteção dos dados pessoais e ampliação dos testes automatizados. Esses itens deverão ser verificados na implementação.
