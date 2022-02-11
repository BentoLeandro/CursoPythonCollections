
from collections import Counter


texto1 = """
Provavelmente, toda pessoa desenvolvedora, quando confrontada com um problema complicado, já pensou empolgadamente: “Aposto que existe uma biblioteca que eu posso utilizar para resolver isso!”. 
O pensamento não está errado, pois traz consigo a promessa de economia de tempo, complexidade abstraída e eficiência adquirida. Entretanto, esse pensamento, se utilizado de maneira excessiva, pode acarretar em vários problemas, como o inferno de dependências.
Enfrentou ou está enfrentando o inferno de dependências e está buscando uma forma automática de atualizar as dependências do seu projeto?
Neste artigo, vamos falar sobre o inferno de dependências e como enfrentá-lo utilizando o Dependabot. Descobriremos como utilizá-lo em repositórios do GitHub e o quanto ele facilita a vida das pessoas desenvolvedoras.
O inferno de dependências é um termo utilizado para definir os problemas enfrentados pelas pessoas desenvolvedoras, quando o software - ou um pacote de software - depende de terceiro e não consegue acessar essa dependência adicional para funcionar corretamente. 
Resumindo: quando o software funciona de forma anormal, exibindo erros e bugs devido a um software/aplicativo integrado no sistema que foi desenvolvido por terceiros, temos o inferno de dependências!
O problema pode assumir muitas formas e ocorrer por várias causas, como, por exemplo, a necessidade de instalar bibliotecas de software complementares, a necessidade de longas cadeias de instalações, problemas com um programa conflitante, a criação de dependências 
circulares, dependências desatualizadas que são mantidas no projeto e muito mais.
"""

texto2 = """
É cada vez mais comum utilizar a expressão ''dar um Google'' para se referir ao ato de realizar uma busca. Isso porque a plataforma processa mais de 3,5 bilhões de pesquisas por dia, totalizando mais de 1,2 trilhão de pesquisas por ano.
Cerca de 46% das pesquisas por produtos são feitas no Google, o que torna o buscador ideal para investir em anúncios e divulgar uma marca ou serviço.
Mas, quem nunca teve dificuldades na hora de elaborar o título de uma campanha do Google Ads? Pois é! O espaço reduzido e o grande número de anúncios que cercam os usuários dificultam os resultados da sua ação.
Mais do que isso, elaborar um bom título é fundamental para passar todas as ideias da sua marca e conquistar o "clique" de um cliente em potencial.
Além disso, como sua campanha virá sempre em conjunto com outros anúncios, um bom copy é essencial para se destacar e chamar a atenção do público.
Por isso, separamos as principais informações para você criar bons títulos e garantir o sucesso da sua campanha. Se liga nessas dicas!
Pode até não parecer, mas pensar no número de caracteres no momento de planejar o seu anúncio é essencial para o planejamento do seu conteúdo.
Para o título, o número máximo de caracteres é 30, podendo conter até três títulos por anúncio. Já para a descrição, podendo haver até duas, é possível colocar até 90 caracteres.
É importante se lembrar que o título sempre ficará em destaque, por isso, nele devem ser utilizadas palavras que as pessoas geralmente utilizam em suas pesquisas. Para isso, uma boa estratégia de SEO pode te auxiliar.
Na descrição, destaque os detalhes sobre seu serviço e adicione uma chamada para ação, como "Compre agora" ou "Matricule-se já!".
"""

def analisa_frequencia_letras(texto):
    contador_texto1 = Counter(texto.lower())
    total_aparicoes = sum(contador_texto1.values())
    proporcoes = [(letra, frequencia/total_aparicoes) for letra, frequencia in contador_texto1.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10) 
    for caractere, proporcao in mais_comuns:
        print(f'{caractere} = {proporcao*100:.2f}')

print("Analise do texto 1")
analisa_frequencia_letras(texto1)  

print()
print("Analise do texto 2")
analisa_frequencia_letras(texto2)

    
