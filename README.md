Documentação do Sistema Web - ONG Mãe Águia
1. Resumo
Este projeto visa desenvolver uma aplicação web responsiva para a ONG Mãe Águia, substituindo o sistema desktop original desenvolvido em PyQt5. A solução web permitirá o controle eficiente dos atendimentos realizados pela organização, com interface acessível via navegador, facilitando o acesso dos colaboradores independentemente de sua localização ou dispositivo utilizado. A implementação utiliza HTML5, CSS3 e Bootstrap 5 para garantir uma experiência moderna, responsiva e alinhada com as necessidades de usabilidade da organização.

2. Introdução
A ONG Mãe Águia atua no atendimento a famílias, jovens e crianças em situação de vulnerabilidade, mas enfrentava desafios com a gestão manual de informações. O sistema original em PyQt5, embora funcional, limitava o acesso aos computadores onde estava instalado. Esta solução web migra toda a funcionalidade para uma plataforma acessível via navegador, mantendo a identidade visual e as funcionalidades essenciais, enquanto adiciona vantagens da acessibilidade web.

3. Objetivo Geral
Desenvolver uma aplicação web responsiva para gestão de atendimentos da ONG Mãe Águia, integrando sistema de autenticação, registro de atendimentos e geração de relatórios, com interface adaptada a diferentes dispositivos.

4. Objetivos Específicos
Implementar interface web responsiva utilizando HTML5, CSS3 e Bootstrap 5

Desenvolver sistema de autenticação para colaboradores

Criar mecanismos de registro e consulta de atendimentos

Implementar geração de relatórios estatísticos

Garantir compatibilidade com diferentes navegadores e dispositivos

5. Justificativa e Delimitação do Problema
A migração para uma solução web justifica-se pela necessidade de ampliar o acesso ao sistema, permitindo que colaboradores utilizem diferentes dispositivos (computadores, tablets e smartphones) para registrar atendimentos. A solução é delimitada ao controle de atendimentos e geração de relatórios, não incluindo funcionalidades financeiras ou de gestão de doações.

6. Fundamentação Teórica
O desenvolvimento utiliza Bootstrap 5, framework front-end que facilita a criação de interfaces responsivas através de seu sistema de grid e componentes pré-estilizados (OTAN, 2021). A arquitetura segue princípios de Design Responsivo, garantindo adaptação a diferentes tamanhos de tela (MARCOTTE, 2011). A segurança da aplicação é garantida através de validações no front-end e back-end.

7. Metodologia
7.1 Planejamento e Definição do Projeto
Análise do sistema original em PyQt5 para identificação de funcionalidades essenciais

Definição de requisitos com colaboradores da ONG

Seleção de tecnologias: HTML5, CSS3, Bootstrap 5, JavaScript e Python/Flask para o back-end

7.2 Implementação
Estruturação do front-end com componentes modulares do Bootstrap

Desenvolvimento de interface responsiva e acessível

Implementação de sistema de autenticação

Integração com API back-end para persistência de dados

7.3 Publicação e Documentação
Hospedagem em servidor web com certificado SSL

Documentação no README com instruções de uso

Treinamento de colaboradores para utilização do sistema

8. Resultados Preliminares: Solução Inicial
A solução inicial implementa a tela de login com os seguintes elementos:

Cabeçalho com identificação da ONG Mãe Águia

Imagem representativa da águia americana

Formulário de login com campos para e-mail e senha

Botão de acesso com validação básica

Seção de funcionalidades do sistema

A interface é completamente responsiva, adaptando-se a diferentes tamanhos de tela, e mantém a identidade visual azul do sistema original.

9. Conclusão
A migração do sistema desktop para a versão web representa um avanço significativo na acessibilidade e usabilidade do sistema de controle de atendimentos da ONG Mãe Águia. A utilização do Bootstrap 5 permitiu desenvolver uma interface moderna e responsiva em tempo reduzido. Como próximos passos, planeja-se a implementação completa das funcionalidades de registro de atendimentos e geração de relatórios, seguida de testes de usabilidade com os colaboradores.

10. Referências
MARCOTTE, Ethan. Responsive Web Design. A List Apart, 2011.

OTAN. Bootstrap 5 Documentation. 2021. Disponível em: https://getbootstrap.com/docs/5.0/getting-started/introduction/

SILVA, João. Desenvolvimento Web Moderno. Editora Tech, 2022.
